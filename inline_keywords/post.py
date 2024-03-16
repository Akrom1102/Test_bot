from aiogram import types

inline_keyword_1 = types.InlineKeyboardMarkup(row_width=2)
button1 = types.InlineKeyboardButton(text="Option 1", callback_data="option1")
button2 = types.InlineKeyboardButton(text="Option 2", callback_data="option2")
button3 = types.InlineKeyboardButton(text="Option 3", callback_data="option3")
button4 = types.InlineKeyboardButton(text="Option 4", callback_data="option4")

inline_keyword_1.add(button1, button2, button3, button4)

inline_keyword_1_click = types.InlineKeyboardMarkup(row_width=2)
inline_keyword_1_click.add(button1, button2)