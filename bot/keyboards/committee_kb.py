from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_committee_main_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("=e >@8ABC20GV/;0A8", callback_data="committee_users_classes"),
        InlineKeyboardButton("=° $V=0=A8", callback_data="committee_finance")
    )
    kb.add(
        InlineKeyboardButton("=Ê 2VB8", callback_data="committee_reports"),
        InlineKeyboardButton("<¯ 1>@8/>4VW", callback_data="committee_events")
    )
    kb.add(
        InlineKeyboardButton("=è >2V4><;5==O", callback_data="committee_messages"),
        InlineKeyboardButton("=Ë 0O2:8", callback_data="committee_applications")
    )
    return kb

def get_committee_finance_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("• >40B8 28B@0B8 ?> :;0AC", callback_data="committee_add_class_expense"))
    kb.add(InlineKeyboardButton("=d >40B8 28B@0B8 ?> CG=N", callback_data="committee_add_student_expense"))
    kb.add(InlineKeyboardButton("=³ 0O2:8 =0 ?>?>2=5==O", callback_data="committee_pending_payments"))
    kb.add(InlineKeyboardButton("=° 3;O4 DV=0=AV2", callback_data="committee_finance_overview"))
    kb.add(InlineKeyboardButton("© 0704", callback_data="committee_back_main"))
    return kb

def get_committee_reports_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("<ë 0;8H:8 ?> :;0A0E", callback_data="committee_class_balances"),
        InlineKeyboardButton("=È 030;L=0 AB0B8AB8:0", callback_data="committee_general_stats")
    )
    kb.add(
        InlineKeyboardButton("=¸ >=B@>;L ?;0B56V2", callback_data="committee_payment_control"),
        InlineKeyboardButton("=Ä :A?>@B 72VBV2", callback_data="committee_export")
    )
    kb.add(InlineKeyboardButton("© 0704", callback_data="committee_back_main"))
    return kb

def get_back_kb(back_to="committee_back_main"):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("© 0704", callback_data=back_to))
    return kb