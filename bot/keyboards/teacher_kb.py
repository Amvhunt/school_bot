from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_teacher_main_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🏫 Мій клас", callback_data="teacher_my_class"),
        InlineKeyboardButton("👥 Список учнів", callback_data="teacher_students")
    )
    kb.add(
        InlineKeyboardButton("💰 Фінанси класу", callback_data="teacher_finance"),
        InlineKeyboardButton("📊 Звіти", callback_data="teacher_reports")
    )
    kb.add(
        InlineKeyboardButton("📨 Повідомлення", callback_data="teacher_messages"),
        InlineKeyboardButton("🎯 Події класу", callback_data="teacher_events")
    )
    return kb

def get_teacher_finance_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("💰 Баланс класу", callback_data="teacher_class_balance"))
    kb.add(InlineKeyboardButton("📈 Історія транзакцій", callback_data="teacher_transactions"))
    kb.add(InlineKeyboardButton("💸 Статус платежів учнів", callback_data="teacher_payment_status"))
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data="teacher_back_main"))
    return kb

def get_back_kb(back_to="teacher_back_main"):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data=back_to))
    return kb