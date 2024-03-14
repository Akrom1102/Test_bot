from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from test import Database


phone_keyword = ReplyKeyboardMarkup([
      [KeyboardButton("Telefonlar"), KeyboardButton("Noutbuklar")]
    ], resize_keyboard=True)

# 1-usul databasedan o'qib olish
# phone_details = ReplyKeyboardMarkup(resize_keyboard=True)
# query = "SELECT * FROM phone"
# for i in Database.connect(query, "select"):
#     phone_details.add(KeyboardButton(i[1]))
# phone_details.add(KeyboardButton("Back 🚪🏃"))

# 2-usul shunchaki yozish
phone_details = ReplyKeyboardMarkup([
        [KeyboardButton("Redmi"), KeyboardButton("Iphone")],
        [KeyboardButton("Samsung"), KeyboardButton("Honor")],
        [KeyboardButton("Back 🚪🏃")]
    ], resize_keyboard=True)

redmi_details = ReplyKeyboardMarkup([
    [KeyboardButton("Смартфон Xiaomi Redmi 13C, 4GB+128GB I 8GB+256GB, 6.74' 90Hz, 5000mAh, Dual SIM, 4G LTE")],
    [KeyboardButton("Смартфон Xiaomi Redmi Note 13, 6/128 ГБ, 8/128 ГБ, 8/256 ГБ, 6.67', 120 Гц")],
    [KeyboardButton("Смартфон Xiaomi Redmi 12 8/256 ГБ, 8/128 ГБ 5000 мА/ч и со сканером отпечатка пальца")],
    [KeyboardButton("Back 🚪🏃")]
], resize_keyboard=True)

iphone_details = ReplyKeyboardMarkup([
    [KeyboardButton("Смартфон Apple iPhone 15 5G, eSIM+nano-SIM, Wi-Fi 6, NFC, 120Hz")],
    [KeyboardButton("Смарфон Apple iPhone 15, 128 ГБ, SIM+eSIM")],
    [KeyboardButton("IPhone 15 Pro/ProMax, 128/256 GB SIM+eSIM")],
    [KeyboardButton("Back 🚪🏃")]
], resize_keyboard=True)

samsung_details = ReplyKeyboardMarkup([
    [KeyboardButton("Смартфон Samsung Galaxy A15 8/256GB, 6/128GB, Android 14, FHD+ 90 Hz, 5000 mA/h, 2 Sim")],
    [KeyboardButton("Смартфон Samsung Galaxy S22 Ultra 8 Гб/256 Гб, белый")],
    [KeyboardButton("Смартфон Samsung Galaxy A05 4GB/128GB 6.7' 50mp, 2SIM, 5000mAh")],
    [KeyboardButton("Back 🚪🏃")]
], resize_keyboard=True)

honor_details = ReplyKeyboardMarkup([
    [KeyboardButton("Смартфон Honor X6a, 4/128 GB, 6/128 GB, 5200 мА/ч")],
    [KeyboardButton("Смартфон Honor X6a, 6/128 GB, 5200 мА/ч")],
    [KeyboardButton("Смартфон Honor X8b 8/128/256 GB, NFC, 2 NanoSIM, AMOLED экран с защитой зрения")],
    [KeyboardButton("Back 🚪🏃")]
], resize_keyboard=True)






# noutbuk
noutbook_details = ReplyKeyboardMarkup([
        [KeyboardButton("HP"), KeyboardButton("ACER")],
        [KeyboardButton("LENOVO"), KeyboardButton("THUNDEROBOT")],
        [KeyboardButton("Back 🚪🏃")]
    ], resize_keyboard=True)

hp_details = ReplyKeyboardMarkup([
    [KeyboardButton("Ноутбук HP 15-dy5131wm, 15' FHD, Intel Core i3-1215U, 4,4ГГц, ОЗУ 8ГБ,SSD 256ГБ графика UHD")],
    [KeyboardButton("Ноутбук HP 250 G10 Core i5-1335U, DDR4 8GB SSD 512GB, 15.6' FHD, Windows, + мышка в подарок")],
    [KeyboardButton("Ноутбук-планшет 2 в 1, HP Envy X360 14-ES0013DX i5-1335U ОЗУ 8 ГБ SSD 512 ГБ 14' FHD")],
    [KeyboardButton("Back 🚪🏃")]
], resize_keyboard=True)

acer_details = ReplyKeyboardMarkup([
    [KeyboardButton("Ноутбук Lenovo Intel Celeron N4020, 8 ГБ DDR4, 256 ГБ SSD, 15.6' DOS")],
    [KeyboardButton("Ноутбук Acer Aspire 5 Intel Core I5-1335U DDR5 8/16 ГБ, 256/512 ГБ SSD FHD 15.6")],
    [KeyboardButton("Ноутбук Asus Vivobook E1504GA Intel Core i3 N305 15.6' FHD IPS 8GB 512 GB, серебро")],
    [KeyboardButton("Back 🚪🏃")]
], resize_keyboard=True)

lenovo_details = ReplyKeyboardMarkup([
    [KeyboardButton("Ноутбук Lenovo Intel celeron N4500 Установлено Windows и программы Дисплей 15.6 HD")],
    [KeyboardButton("Ноутбук Lenovo Intel Celeron N4020 DDR4, 4 ГБ, SSD 256 ГБ, 15.6' HD LCD, cерый")],
    [KeyboardButton("Ноутбук Lenovo IdeaPad Gaming 3 , DDR4 8GB, AMD RYZEN 5-5500H, GeForce RTX2050 4gb")],
    [KeyboardButton("Back 🚪🏃")]
], resize_keyboard=True)


thunderobot_details = ReplyKeyboardMarkup([
    [KeyboardButton("Pre-order 60 days RTX4060 i7-13620H Gaming Laptop 911PLUS 17.3'' 165Hz Notebook Computer Laptops Russian Keyboard Best Laptop")],
    [KeyboardButton("ZERO RTX4060 i7-13650HX Gaming Laptop 16'' 240Hz 2.5K DDR5 Notebook Laptops Gamer Russian Keyboard")],
    [KeyboardButton("Ninkear Laptops N16 Pro 16' 2.5K 165Hz Intel Core i7-13620H WiFi 6 32GB RAM + 1TB SSD Office Computer Laptop Windows 11 Notebook")],
    [KeyboardButton("Back 🚪🏃")]
], resize_keyboard=True)