<div class="register">
  <div class="register__body" role="img" aria-label="Счётный механизм электросчётчика показывает 001234,5">
    <div class="register__digit"><span>0</span></div>
    <div class="register__digit"><span>0</span></div>
    <div class="register__digit"><span>1</span></div>
    <div class="register__digit"><span>2</span></div>
    <div class="register__digit"><span>3</span></div>
    <div class="register__digit"><span>4</span></div>
    <div class="register__digit register__digit--tenth"><span>5</span></div>
  </div>
  <p class="register__caption"><b>001234,5 кВт·ч</b></p>
</div>

# Учёт электросчётчиков

**Meter Parser** — мобильное приложение для снятия показаний приборов учёта электроэнергии. Вы фотографируете счётчик, приложение распознаёт номер и показание, вы проверяете данные и отправляете их на сервер.

| | |
|---|---|
| Версия | 1.0.0 |
| Платформа | Android 7.0 и новее |
| Нужно | Камера и связь с сервером |

<div class="pair">
<img src="assets/screens/home.jpg" alt="Главный экран: кнопки «Внести показание» и «Посмотреть внесённые показания за сегодня», шестерёнка настроек справа вверху">
<div>

На главном экране — два действия: сфотографировать новый счётчик или посмотреть, что уже отправлено сегодня. Шестерёнка справа вверху — [адрес сервера](guide/first-run.md).

</div>
</div>

## Снятие показаний

<div class="steps">
<div class="step">

### Сфотографировать

<span class="ui">Внести показание</span> → рамкой на табло → спуск. В темноте включите подсветку.

</div>
<div class="step">

### Дождаться распознавания

Номер прибора, показание, тарифность и тип подставятся в поля.

</div>
<div class="step">

### Проверить

Сверьте поля с табло, ошибки исправьте вручную.

</div>
<div class="step">

### Отправить

<span class="ui">Отправить</span> — показание в базе. <span class="ui">Добавить ещё</span> — следующий прибор.

</div>
</div>

<div class="screens">
<figure class="screen">
<img src="assets/screens/camera.jpg" alt="Снимок табло электросчётчика с кнопками «Переснять» и «Отправить»">
<figcaption><b>Снимок</b><br>Кадр смазан или бликует — переснимите.</figcaption>
</figure>
<figure class="screen">
<img src="assets/screens/review.jpg" alt="Экран «Проверка данных»: номер прибора, тип, показание, тарифность и разрядность, распознанные нейросетью">
<figcaption><b>Проверка</b><br>Поля уже заполнены, их можно править.</figcaption>
</figure>
<figure class="screen">
<img src="assets/screens/review-done.jpg" alt="Диалог «Сохранено»: показание успешно сохранено, кнопки «На главную» и «Добавить ещё»">
<figcaption><b>Готово</b><br>Показание сохранено на сервере.</figcaption>
</figure>
</div>

> [!TIP]
> Распознавание может ошибаться. Верны только цифры на табло прибора — при необходимости отредактируйте поля вручную.

## Показания за сегодня

<div class="pair">
<img src="assets/screens/today.jpg" alt="Экран «Показания за сегодня»: список отправленных показаний с поиском по номеру прибора учёта">
<div>

<span class="ui">Посмотреть внесённые показания за сегодня</span> на главном экране открывает список того, что вы уже отправили. Есть поиск по номеру прибора учёта и ссылка на фото каждого показания.

</div>
</div>
