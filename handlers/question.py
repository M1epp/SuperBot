from aiogram import Router, F
import emoji
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from keyboards.for_question import (get_info_for_customer, get_info_about_tour, get_info_for_owner,
                                    get_info_for_employee, get_info_about_personal_boat,
                                    get_location_keyboard, keyboard_inline_boat, keyboard_inline1,
                                    keyboard_inline2, keyboard_inline3)
from Text.Text import Back_to_old_spb, Magic_of_night_spb, North_Venice, Timetable, Boat, Timetable_for_customer
from DataBase.DB_google_sheets import (get_by_name_and_data_for_employee, get_by_name_and_data_for_owner,
                                       get_by_data_day_from_the_report, get_by_data_to_data_from_the_report)
from DataBase.DB_SQL_ import (who_is_user, user_is_admin, user_is_employee, get_name_for_employee, get_list_of_employee,
                              add_delete_employee_bd, DataB)
from handlers.Pay import order
from main import Bot
import datetime
import asyncio

router = Router()
db = DataB("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/DataBase/DB_SQL.db")


# Start, back, help
@router.message(Command("start"))
async def cmd_start(message: Message):
    if message.chat.type == 'private':
        if not db.user_exist(message.from_user.id):
            db.add_user(message.from_user.id)
    user: int = who_is_user(int(message.from_user.id))
    if user == 0:
        await message.answer(
            f"Здравствуйте, {message.from_user.full_name}",
            reply_markup=get_info_for_owner()
        )
    elif user == 1:
        await message.answer(
            f'Здравствуйте, {message.from_user.full_name}! Что бы вы хотели ?',
            reply_markup=get_info_for_employee()
        )
    else:
        await message.answer(
            f'Вас приветсвует компания <b>Драйвер</b> \nПожалуйства, выберите интересующую вас информацию{emoji.emojize(":down_arrow:")}',
            reply_markup=get_info_for_customer()
        )


@router.message(F.text == "Назад")
async def cmd_back(message: Message):
    user: int = who_is_user(int(message.from_user.id))
    if user == 0:
        await message.answer(
            "Возвращаем вас назад",
            reply_markup=get_info_for_owner()
            )
    elif user == 1:
        await message.answer(
            "Возвращаем вас назад",
            reply_markup=get_info_for_employee()
        )
    else:
        await message.answer(
            "Возвращаем вас назад",
            reply_markup=get_info_for_customer()
        )


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "По любым вопросам обращайтесь к нашему менеджеру @MRX48"
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


@router.message(F.text == "Нужна помощь")
async def cmd_about_tours(message: Message):
    await message.answer(
        "По любым вопросам обращайтесь к нашему менеджеру @MRX48",
    )
###


# info_about_tours
@router.message(F.text == "Северная Венеция")
async def info_about_tour1(message: Message):
    file_ids1 = []
    image = FSInputFile("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/image1.jpg")
    result = await message.answer_photo(
        image,
        f'{North_Venice}',
        reply_markup=keyboard_inline1
    )
    file_ids1.append(result.photo[-1].file_id)


@router.message(F.text == "Возвращение в старый Петербург")
async def info_about_tour2(message: Message):
    file_ids2 = []
    image = FSInputFile("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/image2.jpg")
    result = await message.answer_photo(
        image,
        f'{Back_to_old_spb}',
        reply_markup=keyboard_inline2
    )
    file_ids2.append(result.photo[-1].file_id)


@router.message(F.text == "Магия ночного Петербурга")
async def info_about_tour3(message: Message):
    file_ids3 = []
    image = FSInputFile("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/image3.jpg")
    result = await message.answer_photo(
        image,
        f'{Magic_of_night_spb}',
        reply_markup=keyboard_inline3
    )
    file_ids3.append(result.photo[-1].file_id)


@router.message(F.text == "Расписание")
async def timetable_def(message: Message):
    await message.answer(
        Timetable_for_customer,
        reply_markup=get_info_about_tour()
    )
#


# Callback for pay
@router.callback_query(F.data == 'Покупка1')
async def button_press(callback: CallbackQuery):
    await callback.answer(
        "Переводим вас на покупку",
        await order(callback.message,
                    callback.bot,
                    price=100000,
                    photo_url='https://spbboats.ru/assets/cache_image/upload/images/tours/severnaya-veneziya-marshrut-02_0x0_eb9.jpg',
                    description='Ваш выбор - Северная Венеция')
    )


@router.callback_query(F.data == 'Покупка2')
async def button_press(callback: CallbackQuery):
    await callback.answer(
        "Переводим вас на покупку",
        await order(callback.message,
                    callback.bot,
                    price=120000,
                    photo_url='https://spbboats.ru/assets/cache_image/upload/images/tours/severnaya-veneziya-marshrut-02_0x0_eb9.jpg',
                    description='Ваш выбор - Возвращение в старый Петербург')
    )


@router.callback_query(F.data == 'Покупка3')
async def button_press(callback: CallbackQuery):
    await callback.answer(
        "Переводим вас на покупку",
        await order(callback.message,
                    callback.bot,
                    price=150000,
                    photo_url='https://www.driver-river.ru/images/141.jpg',
                    description='Ваш выбор - Магия ночного Петербурга ')
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
    image = FSInputFile("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/image4.jpg")
    result = await message.answer_photo(
        image,
        f'{Boat[0]}',
        reply_markup=keyboard_inline_boat
    )
    file_ids4.append(result.photo[-1].file_id)


@router.message(F.text == "Торпеда")
async def info_about_boat2(message: Message):
    file_ids5 = []
    image = FSInputFile("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/image5.jpg")
    result = await message.answer_photo(
        image,
        f'{Boat[1]}',
        reply_markup=keyboard_inline_boat
    )
    file_ids5.append(result.photo[-1].file_id)


@router.message(F.text == "Абсолют")
async def info_about_boat3(message: Message):
    file_ids6 = []
    image = FSInputFile("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/image6.jpg")
    result = await message.answer_photo(
        image,
        f'{Boat[2]}',
        reply_markup=keyboard_inline_boat
    )
    file_ids6.append(result.photo[-1].file_id)


@router.message(F.text == "Граф")
async def info_about_boat4(message: Message):
    file_ids7 = []
    image = FSInputFile("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/image7.jpg")
    result = await message.answer_photo(
        image,
        f'{Boat[3]}',
        reply_markup=keyboard_inline_boat
    )
    file_ids7.append(result.photo[-1].file_id)


@router.message(F.text == "Гермес")
async def info_about_boat5(message: Message):
    file_ids8 = []
    image = FSInputFile("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/image8.jpg")
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
    user = user_is_admin(int(message.from_user.id))
    if user:
        await message.answer(
            "Введите данные в формате: Мазориев Умар 01.01.2000",
        )

        @router.message(F.text.regexp(r'^\w+\s\w+\s\d{2}\.\d{2}\.\d{4}$'))
        async def get_info_about_salary_for_owner(message2: Message):
            if user:
                a = message2.text.split(" ")
                name = a[0] + " " + a[1]
                data = a[2]
                await message2.answer(
                    str(get_by_name_and_data_for_owner(name, data))
                )


@router.message(F.text == "Получить информацию за день")
async def get_info_about_day(message: Message):
    user = user_is_admin(int(message.from_user.id))
    if user:
        await message.answer(
            "Введите дату в формате: 01.01.2000",
        )

        @router.message(F.text.regexp(r'^\d{2}\.\d{2}\.\d{4}$'))
        async def get_info_about_day2(message2: Message):
            if user:
                await message2.answer(
                    str(get_by_data_day_from_the_report(message2.text))
                )


@router.message(F.text == "Получить информацию за срок")
async def get_info_about_week(message: Message):
    user = user_is_admin(int(message.from_user.id))
    if user:
        await message.answer(
            "Введите даты в формате: 01.01.2000 10.01.2000",
        )

        @router.message(F.text.regexp(r'\d{2}\.\d{2}\.\d{4}\s\d{2}\.\d{2}\.\d{4}'))
        async def get_info_about_week2(message2: Message):
            if user:
                new_message = message2.text.split(" ")
                data1 = new_message[0]
                data2 = new_message[1]
                await message2.answer(
                    str(get_by_data_to_data_from_the_report(data1, data2))
                )


@router.message(F.text == "Добавить/удалить сотрудника")
async def add_delete_employee(message: Message):
    user = user_is_admin(int(message.from_user.id))
    if user:
        await message.answer(
            "Введите telegram_id и имя сотрудника в формате: 1111111111 Мазориев Умар"
        )

        @router.message(F.text.regexp(r'\d{9,10}\s\w+\s\w+'))
        async def add_delete_employee2(message2: Message):
            if user:
                new_message = message2.text.split(" ")
                t_id: int = int(new_message[0])
                name: str = new_message[1] + " " + new_message[2]
                add_delete_employee_bd(t_id, name)
                if user:
                    await message2.answer(
                        "Сотрудник добавлен"
                    )


@router.message(F.text == "Список сотрудников")
async def list_of_employees(message: Message):
    if user_is_admin(int(message.from_user.id)):
        await message.answer(
            str(get_list_of_employee())
        )


@router.message(F.text == "Рассылка сообщения пользователям")
async def get_location_for_admin(message: Message):
    if user_is_admin(int(message.from_user.id)):
        await message.answer(
            "Для того чтобы начать рассылку пришлите фотографию и текст к ней, перед текстом напишите команду /send_all",
            reply_markup=get_info_for_owner()
        )


async def send_broadcast(bot, file_id, caption):
    users = db.get_users()
    for user in users:
        user_id, active = user
        if active:
            try:
                # Отправляем фотографию напрямую
                await bot.send_photo(user_id, file_id, caption=caption)

                await asyncio.sleep(1)  # Пауза между отправкой сообщений (по желанию)
            except Exception as e:
                print(f"Ошибка при отправке рассылки для пользователя {user_id}: {e}")


@router.message(Command('send_all'))
async def cmd_send_all(message: Message, bot: Bot):
    if message.chat.type == 'private' and user_is_admin(int(message.from_user.id)):
        file_id = None
        caption = "Ваш текст под фотографией"

        if message.photo:
            file_id = message.photo[-1].file_id

        if message.caption:
            caption = message.caption.removeprefix('/send_all').strip()

        if not file_id:
            await bot.send_message(message.from_user.id,
                                   "Фотография не прикреплена. Пожалуйста, отправьте фотографию вместе с командой.")
            return

        if caption:
            await bot.send_message(message.chat.id, caption)
        if message.text and message.text.startswith("/send_all"):
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        await send_broadcast(bot, file_id, caption)
        await bot.send_message(message.from_user.id, "Рассылка выполнена успешно!")
###


# info_for_employee
@router.message(F.text == "Информация об отработанных сменах")
async def get_info_about_salary_for_employee(message: Message):
    user = user_is_employee(int(message.from_user.id))
    if user:
        await message.answer(
            "Введите дату в формате: 01.01.2000",
        )

        @router.message(F.text)
        async def get_info_about_salary_for_employee2(message2: Message):
            if user:
                name_employee = get_name_for_employee(message2.from_user.id)
                await message2.answer(
                    str(get_by_name_and_data_for_employee(name_employee, message2.text))
                )


@router.message(F.text == "Расписание рейсов")
async def get_info_about_timetable(message: Message):
    if user_is_employee(int(message.from_user.id)):
        await message.answer(
            Timetable
        )


@router.message(F.text == "Начать смену")
async def get_location_for_admin(message: Message):
    if user_is_employee(int(message.from_user.id)):
        await message.answer(
            "Для начала смены, пожалуйста, отправьте свою геолокацию.",
            reply_markup=get_location_keyboard()
        )


@router.message(F.location)
async def handle_location(message: Message, bot: Bot):
    if user_is_employee(int(message.from_user.id)):
        location = message.location
        admin_id1 = 1733570869
        admin_id2 = 1278314485
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = message.from_user
        user_name = user.full_name
        caption = f"Геолокация от {user_name}\nВремя : {current_time}"
        await bot.send_venue(admin_id1, location.latitude, location.longitude, title="Смена начата", address=caption)
        await bot.send_venue(admin_id2, location.latitude, location.longitude, title="Смена начата", address=caption)
        await message.answer("Спасибо за предоставленную геолокацию! Смена начата.")
###
