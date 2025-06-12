
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import datetime

def get_status():
    return "Стан системи: ✅ Усе стабільно. Температура: 43°C, Вологість: 60%"

def export_logs():
    log_path = "log.txt"
    with open(log_path, "w") as f:
        f.write("== Лог зміни ==\n")
        f.write(f"Дата: {datetime.datetime.now()}\n")
        f.write("Температура: 43°C\nВологість: 60%\n\nОператор: Семен Сичов")
    return log_path

def get_settings_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Мова", callback_data="lang")],
        [InlineKeyboardButton("Частота оновлення", callback_data="refresh")]
    ])

def get_admin_panel():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Додати користувача", callback_data="add_user")],
        [InlineKeyboardButton("Перегляд логів", callback_data="logs")]
    ])
