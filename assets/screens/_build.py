#!/usr/bin/env python3
"""Генератор схемы обмена приложения с сервером.

Экраны приложения в руководстве — настоящие скриншоты (assets/screens/*.jpg),
не схемы. Этот скрипт рисует только flow.svg — диаграмму того, какие запросы
уходят на бэкенд; для неё скриншота не бывает.
"""

import pathlib

OUT = pathlib.Path(__file__).parent

FONT = "'Golos Text','PT Sans','Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono',ui-monospace,Consolas,'Liberation Mono',monospace"

SCREEN = "#1A1A2E"
SURF = "#262640"
LINE = "#3A3A5E"
TXT = "#EDECF3"
MUT = "#9095AE"
FAINT = "#6E7391"
RED = "#C8102E"
REDL = "#E8425A"


def head(w, h, label=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" role="img" aria-label="{label}" '
        f'font-family="{FONT}">'
    )


def txt(x, y, s, size=12, fill=TXT, weight="400", anchor="start", mono=False, op=1):
    f = f' font-family="{MONO}"' if mono else ""
    o = f' opacity="{op}"' if op != 1 else ""
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
        f'font-weight="{weight}" text-anchor="{anchor}"{f}{o}>{s}</text>'
    )


def node(x, y, w, h, title, sub, accent=False):
    col = RED if accent else LINE
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{SURF}" '
        f'stroke="{col}" stroke-width="{1.6 if accent else 1}"/>'
        + txt(x + w / 2, y + 27, title, 13.5, TXT, "600", "middle")
        + txt(x + w / 2, y + 46, sub, 10.5, MUT, "normal", "middle")
    )


def arrow(x1, x2, y, label, sub="", rtl=False):
    mid = (x1 + x2) / 2
    if rtl:
        line = (
            f'<path d="M{x2} {y} L{x1+7} {y}" stroke="{REDL}" stroke-width="1.4" fill="none"/>'
            f'<path d="M{x1+8} {y-4} L{x1} {y} L{x1+8} {y+4}z" fill="{REDL}"/>'
        )
    else:
        line = (
            f'<path d="M{x1} {y} L{x2-7} {y}" stroke="{REDL}" stroke-width="1.4" fill="none"/>'
            f'<path d="M{x2-8} {y-4} L{x2} {y} L{x2-8} {y+4}z" fill="{REDL}"/>'
        )
    return (
        line
        + txt(mid, y - 11, label, 10.5, REDL, "600", "middle", mono=True)
        + (txt(mid, y + 21, sub, 9.5, FAINT, "normal", "middle") if sub else "")
    )


FW, FH = 816, 348

flow = f"""{head(FW, FH, 'Схема обмена приложения с сервером')}
  <rect x="0" y="0" width="{FW}" height="{FH}" rx="10" fill="{SCREEN}"/>

  {txt(28, 36, 'Как показание попадает на сервер', 15.5, TXT, '700')}
  {txt(28, 57, 'Одно показание — два обращения к бэкенду. Список за день запрашивается отдельно.', 11, MUT)}

  {node(28, 92, 140, 66, 'Камера', 'снимок счётчика')}
  {node(318, 92, 160, 66, 'Проверка данных', 'поля можно править', True)}
  {node(628, 92, 160, 66, 'Сохранено', 'запись создана')}

  {arrow(168, 318, 125, 'POST /api/upload', 'фото → распознавание')}
  {arrow(478, 628, 125, 'POST /api/confirm', 'подтверждённые поля')}

  <line x1="28" y1="204" x2="788" y2="204" stroke="{LINE}" stroke-width="1"/>

  {node(28, 228, 190, 60, 'Показания за сегодня', 'список с поиском')}
  {arrow(218, 400, 258, 'GET /api/today', 'записи текущего дня', rtl=True)}
  {node(582, 228, 206, 60, 'Бэкенд', 'meter.mosoblenergo.ru')}

  {txt(28, 328, 'Адрес бэкенда задаётся в настройках и хранится на телефоне под ключом @meter_parser_api_url', 10, FAINT)}
</svg>
"""

(OUT / "flow.svg").write_text(flow, encoding="utf-8")
print("написано flow.svg", len(flow), "байт")
