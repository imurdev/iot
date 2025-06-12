
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN, AUTHORIZED_USER_ID
from utils.logics import get_status, export_logs, get_settings_menu, get_admin_panel
from utils.thresholds import get_threshold_menu
from utils.charts import generate_chart_image

main_menu = [
    [InlineKeyboardButton("📊 Стан системи", callback_data="status")],
    [InlineKeyboardButton("📈 Графіки", callback_data="charts")],
    [InlineKeyboardButton("⚙️ Пороги", callback_data="thresholds")],
    [InlineKeyboardButton("📁 Вивантаження логів", callback_data="logs")],
    [InlineKeyboardButton("🛠️ Налаштування", callback_data="settings")],
    [InlineKeyboardButton("👑 Адмін панель", callback_data="admin")],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        await update.message.reply_text("⛔ У вас немає доступу.")
        return
    await update.message.reply_text("Головне меню:", reply_markup=InlineKeyboardMarkup(main_menu))

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if query.from_user.id != AUTHORIZED_USER_ID:
        await query.edit_message_text("⛔ У вас немає доступу.")
        return

    if data == "status":
        await query.edit_message_text(get_status())
    elif data == "charts":
        path = generate_chart_image()
        await query.message.reply_photo(photo=open(path, 'rb'))
    elif data == "thresholds":
        await query.edit_message_text("Керування порогами:", reply_markup=get_threshold_menu())
    elif data == "logs":
        file_path = export_logs()
        await query.message.reply_document(InputFile(file_path, filename="log.txt"))
    elif data == "settings":
        await query.edit_message_text("Налаштування:", reply_markup=get_settings_menu())
    elif data == "admin":
        await query.edit_message_text("Адмін панель:", reply_markup=get_admin_panel())

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_menu))
    app.run_polling()

if __name__ == "__main__":
    main()
