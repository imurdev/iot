
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_threshold_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Розкрій", callback_data="set_rozkr")],
        [InlineKeyboardButton("Армування", callback_data="set_arm")],
        [InlineKeyboardButton("Зварювання", callback_data="set_zvar")],
        [InlineKeyboardButton("Зачистка", callback_data="set_zach")],
        [InlineKeyboardButton("Скління", callback_data="set_sklo")],
        [InlineKeyboardButton("Контроль якості", callback_data="set_kontrol")]
    ])
