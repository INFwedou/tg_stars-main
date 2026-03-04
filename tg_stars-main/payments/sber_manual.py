SBER_CARD_NUMBER = "2202 2088 3370 8689"

def get_payment_instructions(amount: int) -> str:
    return (
        f"💳 <b>Оплата через Сбер карту</b>\n\n"
        f"Переведите <b>{amount}₽</b> на карту:\n"
        f"<code>{SBER_CARD_NUMBER}</code>\n\n"
        "После перевода отправьте чек или скрин в чат.\n"
        "Админ проверит и зачислит баланс вручную."
    )
