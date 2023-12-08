from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


# Payment
async def order(message: Message, bot: Bot, price: int, photo_url: str, description: str):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Покупка билетов",
        description=description,
        payload="Payment through a bot",
        provider_token='381764678:TEST:71711',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Доступ к секретной информации',
                amount=price
            ),
            LabeledPrice(
                label='Ндс',
                amount=0
            ),
            LabeledPrice(
                label='Скидка',
                amount=-0
            ),
            LabeledPrice(
                label='Бонус',
                amount=-0
            ),

        ],
        max_tip_amount=50000,
        suggested_tip_amounts=[5000, 10000,20000, 30000],
        start_parameter='nztcoder',
        provider_data=None,
        photo_url=photo_url,
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
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency},'
    await message.answer(msg)
###
