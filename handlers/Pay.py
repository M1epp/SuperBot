from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardMarkup, InlineKeyboardButton

# Inline for buy
InlineButton1 = InlineKeyboardButton(
    text="Покупка",
    callback_data="Покупка1"
)
keyboard_inline1 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineButton1]]
)


InlineButton2 = InlineKeyboardButton(
    text="Покупка",
    callback_data="Покупка2",
    pay=True
)
keyboard_inline2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineButton2]]
)


InlineButton3 = InlineKeyboardButton(
    text="Покупка",
    callback_data="Покупка3"
)
keyboard_inline3 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineButton3]]
)
###


# Payment 1
async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Покупка через тг бота",
        description="Учимся принимать платежи через тг бота",
        payload="Payment through a bot",
        provider_token='381764678:TEST:71711',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Доступ к секретной информации',
                amount=99000
            ),
            LabeledPrice(
                label='Ндс',
                amount=20000
            ),
            LabeledPrice(
                label='Скидка',
                amount=-20000
            ),
            LabeledPrice(
                label='Бонус',
                amount=-40000
            ),

        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='nztcoder',
        provider_data=None,
        photo_url='https://spbboats.ru/assets/cache_image/upload/images/tours/venice-of-the-north-01_1280x720_c46.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_email_to_provider=False,
        send_phone_number_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id,ok=True)


async def successful_payment(message : Message):
    msg = f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency},'
    await message.answer(msg)
###
