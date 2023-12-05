from aiogram import Router, F
import emoji
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery, User
from keyboards.for_question import (start_menu, get_info_for_customer, get_info_about_tour, get_info_for_owner,
                                    get_info_for_employee, get_info_about_personal_boat,
                                    get_location_keyboard, keyboard_inline_boat,)

from handlers.Pay import keyboard_inline1, keyboard_inline2, keyboard_inline3
from Text.Text import Back_to_old_spb, Magic_of_night_spb, North_Venice, Timetable, Boat
from Employees_Admin.Admin import ADMIN
from Employees_Admin.Codes_Name import Codes, Codes_name
from DataBase.DB import (get_by_name_and_data_for_employee, get_by_name_and_data_for_owner,
                         get_by_data_day_from_the_report, get_by_data_to_data_from_the_report)
from handlers.Pay import order, pre_checkout_query, successful_payment
from main import Bot
import datetime

router = Router()


# Start and back
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f'Вас приветствует компания <b>Драйвер</b> Пожалуйства выберите профиль{emoji.emojize(":down_arrow:")}',
        f'Вас приветсвует компания <b>Драйвер</b> \nПожалуйства, выберите профиль{emoji.emojize(":down_arrow:")}',
        reply_markup=start_menu()
    )

@router.message(F.text == "/help")
async def cmd_back(message: Message):
    await message.answer(
        "По любым вопросам обращайтесь к нашему менеджеру @MRX48",
        reply_markup=start_menu()
        )

@router.message(F.text == "Назад")
async def cmd_back(message: Message):
    await message.answer(
        "Возвращаем вас назад",
        reply_markup=start_menu()
        )
###


# get_who_are_you
@router.message(F.text == "Покупатель")
async def cmd_customer(message: Message):
    await message.answer(
        f'Какая вас интересует информация{emoji.emojize(":red_question_mark:")}',
        reply_markup=get_info_for_customer()
    )


@router.message(F.text == "Работник")
async def cmd_employee(message: Message):
    if message.from_user.id in Codes:
        await message.answer(
            f"Что бы вы хотели, {message.from_user.full_name}?",
            reply_markup=get_info_for_employee()
        )
    else:
        await message.answer(
            "<b>Ошибка</b>",
            reply_markup=start_menu()
        )


@router.message(F.text == "Владелец")
async def cmd_owner(message: Message):
    if message.from_user.id in ADMIN:
        await message.answer(
            f"Здравствуйте, {message.from_user.full_name}",
            reply_markup=get_info_for_owner()
        )
    else:
        await message.answer(
            "<b>Ошибка</b>",
            reply_markup=start_menu()
        )
###


# info_for_customer
@router.message(F.text == "Наши экскурсии")
async def cmd_about_tours(message: Message):
    await message.answer(
        "Информацию о какой экскурсии вы бы хотели узнать?",
        reply_markup=get_info_about_tour()
    )


@router.message(F.text == "Индивидуальные катера")
async def cmd_about_tours(message: Message):
    await message.answer(
        "Информацию по какому катеру вы бы хотели узнать?",
        reply_markup=get_info_about_personal_boat()
    )
###


# Payment
router.message.register(order, F.text == "Купить билеты")
router.pre_checkout_query.register(pre_checkout_query)
router.message.register(successful_payment, F.PAYMENT)
###


# info_about_tours
@router.message(F.text == "Северная Венеция")
async def info_about_tour1(message: Message):
    file_ids1 = []
    image = FSInputFile("/Users/victo/PycharmProjects/SuperBot/image1.jpg")
    result = await message.answer_photo(
        image,
        f'{North_Venice}',
        reply_markup=keyboard_inline1
    )
    file_ids1.append(result.photo[-1].file_id)


@router.message(F.text == "Возвращение в старый Петербург")
async def info_about_tour2(message: Message):
    file_ids2 = []
    image = FSInputFile("/Users/victo/PycharmProjects/SuperBot/image2.jpg")
    result = await message.answer_photo(
        image,
        f'{Back_to_old_spb}',
        reply_markup=keyboard_inline2
    )
    file_ids2.append(result.photo[-1].file_id)


@router.message(F.text == "Магия ночного Петербурга")
async def info_about_tour3(message: Message):
    file_ids3 = []
    image = FSInputFile("/Users/victo/PycharmProjects/SuperBot/image3.jpg")
    result = await message.answer_photo(
        image,
        f'{Magic_of_night_spb}',
        reply_markup=keyboard_inline3
    )
    file_ids3.append(result.photo[-1].file_id)

router.message.register(order, F.text == "Расписание рейсов")
router.pre_checkout_query.register(pre_checkout_query)
router.message.register(successful_payment, F.PAYMENT)

@router.callback_query(F.data == 'Покупка1')
async def button_press(callback: CallbackQuery):
    await callback.answer(
        "Переводим вас на покупку",
        # Вызываем функцию order для инициирования оплаты
        await order(callback.message, callback.bot, price=100000,photo_url='https://spbboats.ru/assets/cache_image/upload/images/tours/severnaya-veneziya-marshrut-02_0x0_eb9.jpg')
    )


@router.callback_query(F.data == 'Покупка2')
async def button_press(callback: CallbackQuery):
    await callback.answer(
        "Переводим вас на покупку",
        await order(callback.message, callback.bot, price=120000,photo_url='https://spbboats.ru/assets/cache_image/upload/images/tours/severnaya-veneziya-marshrut-02_0x0_eb9.jpg')
    )


@router.callback_query(F.data == 'Покупка3')
async def button_press(callback: CallbackQuery):
    await callback.answer(
        "Переводим вас на покупку",
        await order(callback.message, callback.bot, price=150000,photo_url='https://drive.google.com/file/d/1FzTrndZnp9kiC7j1JAn_hgHDpAtu3t0W/view?usp=drive_link')
    )
###


# info_about_private_boat
@router.callback_query(F.data == 'Кнопка была нажата')
async def button_press(callback: CallbackQuery):
    await callback.answer(
        "Переводим вас в переписку с админом",
        show_alert=True
    )


@router.message(F.text == "Спутник")
async def info_about_boat1(message: Message):
    file_ids4 = []
    image = FSInputFile("/Users/victo/PycharmProjects/SuperBot/image4.jpg")
    result = await message.answer_photo(
        image,
        f'{Boat[0]}',
        reply_markup=keyboard_inline_boat
    )
    file_ids4.append(result.photo[-1].file_id)


@router.message(F.text == "Торпеда")
async def info_about_boat2(message: Message):
    file_ids5 = []
    image = FSInputFile("/Users/victo/PycharmProjects/SuperBot/image5.jpg")
    result = await message.answer_photo(
        image,
        f'{Boat[1]}',
        reply_markup=keyboard_inline_boat
    )
    file_ids5.append(result.photo[-1].file_id)


@router.message(F.text == "Абсолют")
async def info_about_boat3(message: Message):
    file_ids6 = []
    image = FSInputFile("/Users/victo/PycharmProjects/SuperBot/image6.jpg")
    result = await message.answer_photo(
        image,
        f'{Boat[2]}',
        reply_markup=keyboard_inline_boat
    )
    file_ids6.append(result.photo[-1].file_id)


@router.message(F.text == "Граф")
async def info_about_boat4(message: Message):
    file_ids7 = []
    image = FSInputFile("/Users/victo/PycharmProjects/SuperBot/image7.jpg")
    result = await message.answer_photo(
        image,
        f'{Boat[3]}',
        reply_markup=keyboard_inline_boat
    )
    file_ids7.append(result.photo[-1].file_id)


@router.message(F.text == "Гермес")
async def info_about_boat5(message: Message):
    file_ids8 = []
    image = FSInputFile("/Users/victo/PycharmProjects/SuperBot/image8.jpg")
    result = await message.answer_photo(
        image,
        f'{Boat[4]}',
        reply_markup=keyboard_inline_boat
    )
    file_ids8.append(result.photo[-1].file_id)
###


# info_for_owner
@router.message(F.text == "Узнать об отработке сотрудника")
async def get_info_about_employee(message: Message):
    if message.from_user.id in ADMIN:
        await message.answer(
            "Введите данные в формате: Мазориев Умар 01.01.2000",
        )

        @router.message(F.text.regexp(r'^\w+\s\w+\s\d{2}\.\d{2}\.\d{4}$'))
        async def get_info_about_salary_for_owner(message2: Message):
            a = message2.text.split(" ")
            name = a[0] + " " + a[1]
            data = a[2]
            await message2.answer(
                str(get_by_name_and_data_for_owner(name, data))
            )


@router.message(F.text == "Получить информацию за день")
async def get_info_about_day(message: Message):
    if message.from_user.id in ADMIN:
        await message.answer(
            "Введите дату в формате: 01.01.2000",
        )

        @router.message(F.text.regexp(r'^\d{2}\.\d{2}\.\d{4}$'))
        async def get_info_about_day2(message2: Message):
            if message.from_user.id in ADMIN:
                await message2.answer(
                    str(get_by_data_day_from_the_report(message2.text))
                )


@router.message(F.text == "Получить информацию за срок")
async def get_info_about_week(message: Message):
    if message.from_user.id in ADMIN:
        await message.answer(
            "Введите даты в формате: 01.01.2000 10.01.2000",
        )

        @router.message(F.text.regexp(r'\d{2}\.\d{2}\.\d{4}\s\d{2}\.\d{2}\.\d{4}'))
        async def get_info_about_week2(message2: Message):
            new_message = message2.text.split(" ")
            data1 = new_message[0]
            data2 = new_message[1]
            await message2.answer(
                str(get_by_data_to_data_from_the_report(data1, data2))
            )
###


# info_for_employee
@router.message(F.text == "Информация об отработанных сменах")
async def get_info_about_salary_for_employee(message: Message):
    if message.from_user.id in Codes:
        await message.answer(
            "Введите дату в формате: 01.01.2000",
        )

        @router.message(F.text)
        async def get_info_about_salary_for_employee2(message2: Message):
            await message2.answer(
                str(get_by_name_and_data_for_employee(Codes_name[message2.from_user.id], message2.text))
            )


@router.message(F.text == "Расписание рейсов")
async def get_info_about_timetable(message: Message):
    if message.from_user.id in Codes:
        await message.answer(
            Timetable
        )


@router.message(F.text == "Начать смену")
async def get_location_for_admin(message: Message, bot : Bot):
    await message.answer(
        "Для начала смены, пожалуйста, отправьте свою геолокацию.",
        reply_markup=get_location_keyboard()
    )

@router.message(F.location)
async def handle_location(message: Message, bot : Bot):
    # Получение данных о местоположении пользователя
    location = message.location
    # ID админа, которому нужно отправить геолокацию
    admin_id1 = 761433187  # Замените на ID первого админа
    admin_id2 = 1733570869
    # Отправка геолокации админу
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = message.from_user
    user_name = user.full_name
    caption = f"Геолокация от {user_name}\nВремя начала смены: {current_time}"
    await bot.send_venue(admin_id1, location.latitude, location.longitude,title="Смена начата", address=caption)
    #await bot.send_location(admin_id2, location.latitude, location.longitude,caption=caption)
    # Ваш ответ пользователю после получения геолокации
    await message.answer("Спасибо за предоставленную геолокацию! Смена начата.")
###




