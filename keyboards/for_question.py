from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Start menu
def start_menu() -> ReplyKeyboardMarkup:
    kd = ReplyKeyboardBuilder()
    kd.button(text="Покупатель")
    kd.button(text="Работник")
    kd.button(text="Владелец")
    kd.adjust(3)
    return kd.as_markup(resize_keyboard=True)
###


# Inline boat
InlineButton_boat = InlineKeyboardButton(
    text="Контакнты для бронирования",
    callback_data="Кнопка была нажата",
    url='https://t.me/MRX48',
    reply_markup=""
)

keyboard_inline_boat = InlineKeyboardMarkup(
    inline_keyboard=[[InlineButton_boat]]
)
###


# Get info for
def get_info_for_customer() -> ReplyKeyboardMarkup:
    kd = ReplyKeyboardBuilder()
    kd.button(text="Наши экскурсии")
    kd.button(text="Индивидуальные катера")
    kd.button(text="Назад")
    kd.adjust(1, 2)
    return kd.as_markup(resize_keyboard=True)


def get_info_for_employee() -> ReplyKeyboardMarkup:
    kd = ReplyKeyboardBuilder()
    kd.button(text="Информация об отработанных сменах")
    kd.button(text="Начать смену")
    kd.button(text="Расписание рейсов")
    kd.button(text="Назад")
    kd.adjust(1)
    return kd.as_markup(resize_keyboard=True)


def get_info_for_owner() -> ReplyKeyboardMarkup:
    kd = ReplyKeyboardBuilder()
    kd.button(text="Узнать об отработке сотрудника")
    kd.button(text="Получить информацию за день")
    kd.button(text="Получить информацию за срок")
    kd.button(text="Назад")
    kd.adjust(1)
    return kd.as_markup(resize_keyboard=True)
###


# For customer
def get_info_about_tour() -> ReplyKeyboardMarkup:
    kd = ReplyKeyboardBuilder()
    kd.button(text="Северная Венеция")
    kd.button(text="Возвращение в старый Петербург")
    kd.button(text="Магия ночного Петербурга")
    kd.button(text="Назад")
    kd.adjust(2)
    return kd.as_markup(resize_keyboard=True)


def get_info_about_personal_boat() -> ReplyKeyboardMarkup:
    kd = ReplyKeyboardBuilder()
    kd.button(text="Спутник")
    kd.button(text="Торпеда")
    kd.button(text="Абсолют")
    kd.button(text="Граф")
    kd.button(text="Гермес")
    kd.button(text="Назад")
    kd.adjust(2)
    return kd.as_markup(resize_keyboard=True)


# For owner
def about_salary_for_employee() -> ReplyKeyboardMarkup:
    kd = ReplyKeyboardBuilder()
    return kd.as_markup(resize_keyboard=True)
###


# For employee
def get_location_keyboard() -> ReplyKeyboardMarkup:
    kd = ReplyKeyboardBuilder()
    kd.button(text="Отправить мою геолокацию", request_location=True)
    kd.button(text="Назад")
    kd.adjust(2)
    return kd.as_markup(resize_keyboard=True)
