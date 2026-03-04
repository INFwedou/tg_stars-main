from aiogram import Router, types, F

router = Router()

# Список админов
ADMIN_IDS = [8569905611, 8080409008]

# Обработка кнопки "Сбер карта"
@router.callback_query(F.data == "payment_sber")
async def sber_manual_payment(callback: types.CallbackQuery):
    text = (
        "💳 Пополнение через Сбер карту\n\n"
        "Переведите сумму на карту:\n"
        "`2202 2088 3370 8689`\n\n"
        "После перевода отправьте сюда чек или скрин.\n"
        "Администратор проверит и вручную зачислит средства."
    )
    await callback.message.answer(text, parse_mode="Markdown")

# Пересылка чека админу
@router.message(F.photo | F.document)
async def handle_payment_proof(message: types.Message):
    for admin_id in ADMIN_IDS:
        await message.forward(admin_id)
    await message.answer("✅ Чек отправлен администратору. Ожидайте подтверждения.")
