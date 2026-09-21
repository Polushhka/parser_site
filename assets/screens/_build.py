#!/usr/bin/env python3
"""Генератор схем экранов приложения Meter Parser.

Все подписи взяты дословно из строковой таблицы APK (Hermes bytecode,
assets/index.android.bundle), поэтому схемы совпадают с тем, что видит
обходчик на телефоне. Это схемы, а не скриншоты: приложение тёмное,
поэтому схемы тоже тёмные в обеих темах сайта.
"""

import pathlib

OUT = pathlib.Path(__file__).parent

W, H = 280, 570
FONT = "'Golos Text','PT Sans','Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono',ui-monospace,Consolas,'Liberation Mono',monospace"

BEZEL = "#0B0B14"
SCREEN = "#1A1A2E"
SURF = "#262640"
SURF2 = "#20203A"
LINE = "#3A3A5E"
TXT = "#EDECF3"
MUT = "#9095AE"
FAINT = "#6E7391"
RED = "#C8102E"
REDL = "#E8425A"
GRN = "#3E9B6B"


def head(w=W, h=H, label=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" role="img" aria-label="{label}" '
        f'font-family="{FONT}">'
    )


def phone(body, label):
    """Корпус телефона со строкой состояния."""
    return f"""{head(label=label)}
  <rect x="0" y="0" width="{W}" height="{H}" rx="22" fill="{BEZEL}"/>
  <rect x="6" y="6" width="{W-12}" height="{H-12}" rx="17" fill="{SCREEN}"/>
  <rect x="112" y="13" width="56" height="7" rx="3.5" fill="{BEZEL}"/>
  <text x="24" y="38" fill="{FAINT}" font-size="10" font-family="{MONO}">9:41</text>
  <g transform="translate(228,31)">
    <rect x="0" y="0" width="16" height="8" rx="2" fill="none" stroke="{FAINT}" stroke-width="1"/>
    <rect x="2" y="2" width="10" height="4" rx="1" fill="{FAINT}"/>
    <rect x="17" y="2.5" width="2" height="3" rx="1" fill="{FAINT}"/>
  </g>
  {body}
</svg>
"""


def txt(x, y, s, size=12, fill=TXT, weight="400", anchor="start", mono=False, op=1):
    f = f' font-family="{MONO}"' if mono else ""
    o = f' opacity="{op}"' if op != 1 else ""
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
        f'font-weight="{weight}" text-anchor="{anchor}"{f}{o}>{s}</text>'
    )


def box(x, y, w, h, r=8, fill=SURF, stroke=LINE, sw=1):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{st}/>'


def btn(x, y, w, h, label, kind="primary", size=13):
    if kind == "primary":
        fill, stroke, col = RED, "none", "#FFF3F4"
    elif kind == "ghost":
        fill, stroke, col = "none", LINE, TXT
    else:
        fill, stroke, col = SURF, LINE, TXT
    st = f' stroke="{stroke}" stroke-width="1"' if stroke != "none" else ""
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}"{st}/>'
        + txt(x + w / 2, y + h / 2 + 4.5, label, size, col, "600", "middle")
    )


def field(x, y, w, label, value, placeholder=False):
    """Поле ввода: подпись сверху, рамка со значением."""
    col = FAINT if placeholder else TXT
    return (
        txt(x, y, label, 10, MUT, "500")
        + box(x, y + 7, w, 32, 7, SURF2, LINE)
        + txt(x + 11, y + 28, value, 12.5, col, "500", mono=True)
    )


# --------------------------------------------------------------------------
# 1. Главный экран
# --------------------------------------------------------------------------
home = phone(
    f"""
  {txt(24, 90, 'Учёт', 22, TXT, '700')}
  {txt(24, 116, 'электросчётчиков', 22, TXT, '700')}
  {box(226, 70, 30, 30, 8, SURF, LINE)}
  <g stroke="{MUT}" stroke-width="1.3" fill="none">
    <circle cx="241" cy="85" r="4.2"/>
    <path d="M241 77.5v2.4M241 90.1v2.4M233.5 85h2.4M246.1 85h2.4M235.7 79.7l1.7 1.7M244.6 88.6l1.7 1.7M246.3 79.7l-1.7 1.7M237.4 88.6l-1.7 1.7"/>
  </g>
  {txt(24, 158, 'Выберите действие', 12, MUT)}

  {box(24, 176, 232, 78, 11, SURF, LINE)}
  <g transform="translate(42,202)" fill="none" stroke="{REDL}" stroke-width="1.6">
    <rect x="0" y="3" width="22" height="17" rx="3"/>
    <circle cx="11" cy="11.5" r="5"/>
    <path d="M7 3l2-3h4l2 3"/>
  </g>
  {txt(80, 208, 'Внести показание', 14, TXT, '600')}
  {txt(80, 227, 'Сфотографировать счётчик', 11, MUT)}
  {txt(80, 242, 'и отправить показание', 11, MUT)}

  {box(24, 266, 232, 78, 11, SURF, LINE)}
  <g transform="translate(42,292)" fill="none" stroke="{MUT}" stroke-width="1.6">
    <rect x="0" y="0" width="20" height="23" rx="3"/>
    <path d="M5 7h10M5 12h10M5 17h6"/>
  </g>
  {txt(80, 298, 'Посмотреть внесённые', 13.5, TXT, '600')}
  {txt(80, 317, 'Показания за сегодня', 11, MUT)}
  {txt(80, 332, 'с поиском по номеру', 11, MUT)}

  <line x1="24" y1="380" x2="256" y2="380" stroke="{LINE}" stroke-width="1"/>
  {txt(24, 402, 'Шестерёнка справа вверху открывает', 10.5, FAINT)}
  {txt(24, 417, 'настройки адреса сервера.', 10.5, FAINT)}
""",
    "Главный экран приложения",
)

# --------------------------------------------------------------------------
# 2. Камера
# --------------------------------------------------------------------------
corner = lambda x, y, sx, sy: (
    f'<path d="M{x} {y+22*sy} L{x} {y} L{x+22*sx} {y}" fill="none" '
    f'stroke="{REDL}" stroke-width="2.4" stroke-linecap="round"/>'
)

camera = phone(
    f"""
  <rect x="6" y="6" width="{W-12}" height="{H-12}" rx="17" fill="#0F1018"/>
  {txt(24, 38, '9:41', 10, FAINT, mono=True)}
  {txt(24, 74, 'Назад', 13, TXT, '500')}
  <path d="M16 66l-5 4 5 4" fill="none" stroke="{TXT}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" transform="translate(-4,0)"/>

  <rect x="24" y="150" width="232" height="140" rx="10" fill="#15161F" stroke="#23242F" stroke-width="1"/>
  <rect x="44" y="184" width="192" height="52" rx="4" fill="#0A0B10"/>
  <g font-family="{MONO}" font-size="26" font-weight="700" fill="#E9E6DC">
    <text x="60" y="222">0</text><text x="82" y="222">0</text><text x="104" y="222">1</text>
    <text x="126" y="222">2</text><text x="148" y="222">3</text><text x="170" y="222">4</text>
  </g>
  <rect x="188" y="186" width="24" height="48" rx="2" fill="#8E0C22"/>
  <text x="200" y="222" font-family="{MONO}" font-size="26" font-weight="700" fill="#FFECEC" text-anchor="middle">5</text>
  {txt(44, 262, 'кВт·ч', 9.5, '#7A7C88', mono=True)}
  {txt(236, 262, '№ 1234567890', 9, '#7A7C88', 'normal', 'end', mono=True)}

  {corner(24, 150, 1, 1)}
  {corner(256, 150, -1, 1)}
  {corner(24, 290, 1, -1)}
  {corner(256, 290, -1, -1)}

  {txt(140, 322, 'Наведите на экран счётчика', 12.5, TXT, '500', 'middle')}
  {txt(140, 340, 'Держите телефон ровно, без бликов', 10.5, MUT, 'normal', 'middle')}

  {box(80, 362, 120, 30, 15, 'none', LINE)}
  <g transform="translate(94,370)" fill="none" stroke="#E3C07B" stroke-width="1.3">
    <path d="M3 0h6v5.5l2.5 3.5a5 5 0 11-11 0L3 5.5z"/>
  </g>
  {txt(116, 381, 'Вкл подсветку', 11.5, TXT, '500')}

  <circle cx="140" cy="452" r="31" fill="none" stroke="{TXT}" stroke-width="2.2"/>
  <circle cx="140" cy="452" r="24" fill="{TXT}"/>
  {txt(140, 506, 'Нажмите, чтобы сделать снимок', 10.5, FAINT, 'normal', 'middle')}
""",
    "Экран камеры",
)

# --------------------------------------------------------------------------
# 3. Проверка данных
# --------------------------------------------------------------------------
review = phone(
    f"""
  {txt(24, 74, 'Проверьте данные', 17, TXT, '700')}
  {box(24, 88, 232, 40, 7, '#1F2A24', '#2E5C45')}
  {txt(36, 104, 'Данные распознаны нейросетью.', 10, '#7FD1A5')}
  {txt(36, 118, 'Отредактируйте при необходимости.', 10, '#7FD1A5')}

  {field(24, 146, 232, '№ прибора учёта', '1234567890')}
  {field(24, 200, 232, 'Показание', '001234')}
  {field(24, 254, 110, 'Тарифность', 'T1')}
  {field(146, 254, 110, 'Разрядность', '1')}
  {field(24, 308, 232, 'Тип прибора', 'Меркурий 230')}

  {btn(24, 366, 232, 42, 'Отправить')}
  {btn(24, 418, 110, 36, 'Посмотреть фото', 'ghost', 10.5)}
  {btn(146, 418, 110, 36, 'Переснять', 'ghost', 11.5)}

  {txt(140, 482, 'Нужно заполнить хотя бы номер', 10, FAINT, 'normal', 'middle')}
  {txt(140, 496, 'прибора или показание', 10, FAINT, 'normal', 'middle')}
""",
    "Экран проверки распознанных данных",
)

# --------------------------------------------------------------------------
# 4. Показания за сегодня
# --------------------------------------------------------------------------


def record(y, num, reading, tariff, mtype):
    return (
        box(24, y, 232, 92, 9, SURF, LINE)
        + txt(36, y + 22, "№ прибора:", 10, MUT)
        + txt(244, y + 22, num, 11.5, TXT, "600", "end", mono=True)
        + f'<line x1="36" y1="{y+32}" x2="244" y2="{y+32}" stroke="{LINE}" stroke-width="1"/>'
        + txt(36, y + 50, "Показание:", 10, MUT)
        + txt(244, y + 50, reading, 13, TXT, "700", "end", mono=True)
        + txt(36, y + 70, "Тариф:", 10, MUT)
        + txt(120, y + 70, tariff, 10.5, TXT, "500", "end", mono=True)
        + txt(140, y + 70, "Тип:", 10, MUT)
        + txt(244, y + 70, mtype, 10.5, TXT, "500", "end")
        + txt(36, y + 84, "Фото", 9.5, REDL, "500")
    )


today = phone(
    f"""
  {txt(24, 74, 'Показания за сегодня', 17, TXT, '700')}
  {box(24, 88, 232, 34, 8, SURF2, LINE)}
  <g transform="translate(37,98)" fill="none" stroke="{FAINT}" stroke-width="1.3">
    <circle cx="5" cy="5" r="4.5"/><path d="M8.5 8.5L12 12"/>
  </g>
  {txt(58, 110, 'Поиск по № прибора учёта...', 11.5, FAINT)}
  {txt(24, 140, 'Найдено: 3', 11, MUT, '600')}

  {record(150, '1234567890', '001234,5', 'T1', 'Меркурий 230')}
  {record(254, '1234567891', '008912,0', 'T2', 'СЕ 208')}
  {record(358, '1234567892', '045003,2', 'T1', 'Нева 324')}

  {btn(24, 470, 232, 40, 'На главную', 'ghost')}
""",
    "Экран показаний за сегодня",
)

# --------------------------------------------------------------------------
# 5. Настройки сервера
# --------------------------------------------------------------------------
settings = phone(
    f"""
  {txt(24, 74, 'Настройки сервера', 17, TXT, '700')}
  {txt(24, 100, 'Укажите адрес бэкенда.', 11, MUT)}
  {txt(24, 116, 'По умолчанию — продакшен', 11, MUT)}
  {txt(24, 132, 'https://meter.mosoblenergo.ru', 10.5, FAINT, mono=True)}

  {txt(24, 170, 'Адрес сервера', 10, MUT, '500')}
  {box(24, 177, 232, 36, 7, SURF2, LINE)}
  {txt(35, 200, 'https://meter.mosoblenergo.ru', 10.5, TXT, '500', mono=True)}
  {txt(24, 230, '(например https://meter.mosoblenergo.ru)', 9.5, FAINT)}

  {btn(24, 250, 232, 42, 'Сохранить')}
  {btn(24, 302, 232, 38, 'Сбросить к заводским', 'ghost')}

  {box(24, 362, 232, 58, 7, '#1F2A24', '#2E5C45')}
  {txt(36, 385, 'Адрес сохранён', 11.5, '#7FD1A5', '600')}
  {txt(36, 404, 'Соединение с сервером установлено', 10, '#7FD1A5')}

  <line x1="24" y1="448" x2="256" y2="448" stroke="{LINE}" stroke-width="1"/>
  {txt(24, 470, 'Приложение проверяет адрес сразу', 10.5, FAINT)}
  {txt(24, 485, 'при сохранении и сообщает,', 10.5, FAINT)}
  {txt(24, 500, 'дозвонилось ли оно до сервера.', 10.5, FAINT)}
""",
    "Экран настроек сервера",
)

# --------------------------------------------------------------------------
# 6. Схема обмена с сервером
# --------------------------------------------------------------------------
FW, FH = 816, 348


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

for name, data in [
    ("home.svg", home),
    ("camera.svg", camera),
    ("review.svg", review),
    ("today.svg", today),
    ("settings.svg", settings),
    ("flow.svg", flow),
]:
    (OUT / name).write_text(data, encoding="utf-8")
    print("написано", name, len(data), "байт")
