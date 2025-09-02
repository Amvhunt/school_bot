from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot.keyboards.admin_kb import get_admin_main_kb, get_users_classes_kb, get_finance_kb, get_reports_kb, get_events_kb, get_messages_kb, get_applications_kb, get_back_kb
from bot.database import crud

class AdminStates(StatesGroup):
    main_menu = State()
    add_expense = State()
    create_event = State()
    create_message = State()

async def admin_menu(message: types.Message):
    text = "🔐 **Адмін-панель**\n\n" \
           "Вітаю, адміністраторе! Оберіть потрібний розділ для управління системою:"
    
    await message.answer(text, reply_markup=get_admin_main_kb(), parse_mode="Markdown")

async def handle_admin_callback(callback_query: types.CallbackQuery, state: FSMContext):
    data = callback_query.data
    
    # Main menu sections
    if data == "admin_users_classes":
        text = "👥 **Користувачі та Класи**\n\n" \
               "Управління користувачами, класами та учнями системи"
        await callback_query.message.edit_text(text, reply_markup=get_users_classes_kb(), parse_mode="Markdown")
        
    elif data == "admin_finance":
        text = "💰 **Фінанси**\n\n" \
               "Управління витратами, балансами та фінансовими операціями"
        await callback_query.message.edit_text(text, reply_markup=get_finance_kb(), parse_mode="Markdown")
        
    elif data == "admin_reports":
        text = "📊 **Звіти**\n\n" \
               "Перегляд статистики, балансів та експорт даних"
        await callback_query.message.edit_text(text, reply_markup=get_reports_kb(), parse_mode="Markdown")
        
    elif data == "admin_events":
        text = "🎯 **Збори та Події**\n\n" \
               "Створення та управління зборами, подіями та заходами"
        await callback_query.message.edit_text(text, reply_markup=get_events_kb(), parse_mode="Markdown")
        
    elif data == "admin_messages":
        text = "📨 **Повідомлення**\n\n" \
               "Створення та відправка повідомлень користувачам системи"
        await callback_query.message.edit_text(text, reply_markup=get_messages_kb(), parse_mode="Markdown")
        
    elif data == "admin_applications":
        text = "📋 **Заявки**\n\n" \
               "Обробка заявок на реєстрацію та поповнення балансу"
        await callback_query.message.edit_text(text, reply_markup=get_applications_kb(), parse_mode="Markdown")
    
    # Finance section handlers
    elif data == "admin_pending_payments":
        text = "💳 **Заявки на поповнення**\n\n" \
               "📋 Функція обробки заявок на поповнення в розробці"
        await callback_query.message.edit_text(text, reply_markup=get_back_kb("admin_finance"), parse_mode="Markdown")
    
    # Users section handlers  
    elif data == "admin_users_list":
        text = "👥 **Список користувачів**\n\n" \
               "📋 Функція перегляду користувачів в розробці"
        await callback_query.message.edit_text(text, reply_markup=get_back_kb("admin_users_classes"), parse_mode="Markdown")
    
    elif data == "admin_classes_list":
        text = "🏫 **Список класів**\n\n" \
               "📋 Функція перегляду класів в розробці"
        await callback_query.message.edit_text(text, reply_markup=get_back_kb("admin_users_classes"), parse_mode="Markdown")
    
    # Back navigation
    elif data == "admin_back_main":
        await admin_menu(callback_query.message)
    
    # Placeholder handlers for other actions
    else:
        text = f"🚧 **Функція в розробці**\n\n" \
               f"Функція '{data}' ще не реалізована.\n" \
               f"Незабаром буде додана!"
        await callback_query.message.edit_text(text, reply_markup=get_back_kb(), parse_mode="Markdown")
    
    await callback_query.answer()
