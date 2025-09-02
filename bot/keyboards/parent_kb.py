from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_parent_main_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("👤 Моя дитина", callback_data="parent_child_info"),
        InlineKeyboardButton("💰 Баланс", callback_data="parent_balance")
    )
    kb.add(
        InlineKeyboardButton("📈 Історія платежів", callback_data="parent_history"),
        InlineKeyboardButton("💳 Поповнити баланс", callback_data="parent_topup")
    )
    kb.add(
        InlineKeyboardButton("📨 Повідомлення", callback_data="parent_notifications"),
        InlineKeyboardButton("📞 Контакти", callback_data="parent_contacts")
    )
    return kb

def get_topup_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("💳 Подати заявку на поповнення", callback_data="parent_request_topup"))
    kb.add(InlineKeyboardButton("📋 Мої заявки", callback_data="parent_my_requests"))
    kb.add(InlineKeyboardButton("ℹ️ Інструкція з оплати", callback_data="parent_payment_info"))
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data="parent_back_main"))
    return kb

def get_back_kb(back_to="parent_back_main"):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data=back_to))
    return kb