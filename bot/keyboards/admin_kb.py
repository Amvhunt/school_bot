from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_admin_main_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("👥 Користувачі/Класи", callback_data="admin_users_classes"),
        InlineKeyboardButton("💰 Фінанси", callback_data="admin_finance")
    )
    kb.add(
        InlineKeyboardButton("📊 Звіти", callback_data="admin_reports"),
        InlineKeyboardButton("🎯 Збори/Події", callback_data="admin_events")
    )
    kb.add(
        InlineKeyboardButton("📨 Повідомлення", callback_data="admin_messages"),
        InlineKeyboardButton("📋 Заявки", callback_data="admin_applications")
    )
    return kb

def get_users_classes_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("👥 Список користувачів", callback_data="admin_users_list"))
    kb.add(InlineKeyboardButton("🏫 Список класів", callback_data="admin_classes_list"))
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data="admin_back_main"))
    return kb

def get_finance_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("➕ Додати витрати по класу", callback_data="admin_add_class_expense"))
    kb.add(InlineKeyboardButton("👤 Додати витрати по учню", callback_data="admin_add_student_expense"))
    kb.add(InlineKeyboardButton("💳 Заявки на поповнення", callback_data="admin_pending_payments"))
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data="admin_back_main"))
    return kb

def get_reports_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🏫 Залишки по класу", callback_data="admin_class_balances"),
        InlineKeyboardButton("👤 Баланс учня", callback_data="admin_student_balance")
    )
    kb.add(
        InlineKeyboardButton("📈 Історія транзакцій", callback_data="admin_transactions"),
        InlineKeyboardButton("💸 Хто здав/не здав", callback_data="admin_payment_status")
    )
    kb.add(InlineKeyboardButton("📄 Експорт Excel/CSV", callback_data="admin_export"))
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data="admin_back_main"))
    return kb

def get_events_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("➕ Створити збір/подію", callback_data="admin_create_event"))
    kb.add(InlineKeyboardButton("📋 Список зборів/подій", callback_data="admin_events_list"))
    kb.add(InlineKeyboardButton("🔒 Закрити збір/подію", callback_data="admin_close_event"))
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data="admin_back_main"))
    return kb

def get_messages_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("➕ Створити повідомлення", callback_data="admin_create_message"))
    kb.add(InlineKeyboardButton("📊 Статистика повідомлень", callback_data="admin_message_stats"))
    kb.add(InlineKeyboardButton("⏰ Відкладені повідомлення", callback_data="admin_scheduled_messages"))
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data="admin_back_main"))
    return kb

def get_applications_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📝 Заявки на реєстрацію", callback_data="admin_registration_requests"),
        InlineKeyboardButton("💰 Заявки на поповнення", callback_data="admin_topup_requests")
    )
    kb.add(InlineKeyboardButton("📁 Архів заявок", callback_data="admin_applications_archive"))
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data="admin_back_main"))
    return kb

def get_back_kb(back_to="admin_back_main"):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("↩️ Назад", callback_data=back_to))
    return kb
