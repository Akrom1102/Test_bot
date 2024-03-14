import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from test import Database
from keyboards import phone_keyword, phone_details, noutbook_details, hp_details, acer_details, lenovo_details, thunderobot_details, redmi_details, samsung_details, iphone_details, honor_details

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = str(message.chat.id)

    check_query = f"""SELECT * FROM users WHERE chat_id = '{chat_id}'"""
    if len(Database.connect(check_query, "select")) >= 1:
        print(f"{username}")
        await message.answer(f"Hello @{username}", reply_markup=phone_keyword)

    else:
        print(f"{first_name} start bot")
        query = f"""INSERT INTO users(first_name, last_name, username, chat_id) VALUES('{first_name}', '{last_name}', '{username}', '{chat_id}')"""
        print(f"{username} {Database.connect(query, "insert")} database")
        print(f"{username}")
        await message.answer(f"Hello @{username}", reply_markup=phone_keyword)



@dp.message_handler(commands=['data'])
async def select(message: types.Message):
    chat_id = message.chat.id
    query_select = f"SELECT * FROM users WHERE chat_id = '{chat_id}'"
    data = Database.connect(query_select, "select")
    print(data)
    await message.answer(f"""
        Hi @{data[0][3]}
        I am bot. Created by Akrom
        First Name: {data[0][1]}
        Last Name: {data[0][2]}""", reply_markup=phone_keyword)


@dp.message_handler(commands=['help'])
async def select(message: types.Message):
    await message.answer(f"""
    1. Sizga yordam kerak bo'lsa telegram bilan aloqaga chiqing  
    2. Yoki +998911348836 nomeriga qo'ng'iroq qiling
    """)

# telefon
@dp.message_handler(lambda message: message.text == "Telefonlar")
async def select(message: types.Message):
    await message.answer(f"""
    Telefonlardan birini tanlang 📱
    """, reply_markup=phone_details)


@dp.message_handler(lambda message: message.text == "Redmi")
async def select(message: types.Message):
    await message.answer(f"""
    Redmi telefonlaridan birini tanlang
    """, reply_markup=redmi_details)

@dp.message_handler(lambda message: message.text == "Смартфон Xiaomi Redmi 13C, 4GB+128GB I 8GB+256GB, 6.74' 90Hz, 5000mAh, Dual SIM, 4G LTE")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 2 897 000
● Дисплей с диагональю: 6,74 дюйма 1600x720, 260 ppi
● Процессор: MediaTek Helio G85
● Частота обновления: до 90 Гц
● Яркость: 450 нит (тип), 600 нит
● Экран: Corning® Gorilla® Glass
● Основная камера 50 Мпс объективом 5P, f/1.8
● 8-мегапиксельная фронтальная камера f /2.0
● Аккумулятор: 5000 мАч (тип)Поддерживает зарядку PD мощностью 18 Вт
● Безопасность: TouchID
● Kино Камера |Режим HDR |Ночной режим |Портретный режим |режим 50 Мп
    """, reply_markup=redmi_details)

@dp.message_handler(lambda message: message.text == "Смартфон Xiaomi Redmi Note 13, 6/128 ГБ, 8/128 ГБ, 8/256 ГБ, 6.67', 120 Гц")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 4 997 000
● Операционная Система: MIUI 14, основанная на Android 13
● Процессор: Snapdragon 685 Mobile (6 нм)
● Оперативная Память: 6 ГБ/8 ГБ LPDDR4X RAM
● Хранилище: 256 ГБ / 512 ГБ встроенной памяти UFS 2.2, расширяемое до 1 ТБ
● Дисплей: 6.67" AMOLED, 2400 x 1080, 120 Hz
● Камеры: 108MP основная + 8MP ультраширокая + 2MP макро + 16MP фронтальная
● Батарея: 5000 мАч, Fast Charge 33 Вт
● Дополнительные функции: Corning Gorilla Glass 3, IP54, защита от влаги и пыли
● Беспроводная Связь: 4G LTE, Bluetooth 5.1, Wi-Fi 2.4GHz/5GHz, ИК-порт
● Разъемы и Слоты: Dual SIM, USB Type-C
    """, reply_markup=redmi_details)

@dp.message_handler(lambda message: message.text == "Смартфон Xiaomi Redmi 12 8/256 ГБ, 8/128 ГБ 5000 мА/ч и со сканером отпечатка пальца")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 2 009 000
● FM-радио, FaceID, TouchID
● Количество объективов (MP) 3*(50 + 8 + 2)
● Селфи камера: 8 MP
● Количество SIM: 2 (DUAL SIM)
● Тип Дисплея: QDLED
● Разрешение: 1080 х 2460
● Частота обновления: 90
● Чипсет: MediaTek Helio G88
● 3,5 мм разъем для наушников
● Емкость аккумулятора: 5000 мА/ч
    """, reply_markup=redmi_details)









@dp.message_handler(lambda message: message.text == "Iphone")
async def select(message: types.Message):
    await message.answer(f"""
    Iphone telefonlaridan birini tanlang
    """, reply_markup=iphone_details)

@dp.message_handler(lambda message: message.text == "Смартфон Apple iPhone 15 5G, eSIM+nano-SIM, Wi-Fi 6, NFC, 120Hz")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 25 000 000
● Мощный Процессор: Сверхбыстрый чип обеспечивает плавную работу и энергоэффективность.
● Яркий Дисплей: Super Retina XDR экран с высоким разрешением для яркого и детального отображения.
● Закажите iPhone 15 сейчас и переживите будущее в своих руках!
● Улучшенная Камера: Великолепные снимки и видео с продвинутой системой камер и режимом ночной съемки.
● Быстрая Зарядка: Технологии быстрой беспроводной и проводной зарядки для комфортного использования.
● Интеграция Apple: Совместимость с экосистемой Apple для гармоничного взаимодействия с другими устройствами.
● Комбинация стиля и производительности.
● Современный дизайн и высококачественные материалы.
● Поддержка последних версий операционной системы iOS.
    """, reply_markup=iphone_details)

@dp.message_handler(lambda message: message.text == "Смарфон Apple iPhone 15, 128 ГБ, SIM+eSIM")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 19 000 000
● Гарантия 12 месяцев. IMEI-1 официально зарегистрированы (активация регистрации происходит в течение 30 дней)
● Операционная система: iOS 17
● Диагональ экрана: 6,1"
● Встроенная память: 128 ГБ
● Оперативная память: 6 ГБ
● Камера: 48 МП
● Количество SIM-карт: 1 nano-SIM / eSim
● Материал корпуса: Metall natural
● Тип разблокировки: FaceID
● Процессор: Apple Bionic A16    
    """, reply_markup=iphone_details)


@dp.message_handler(lambda message: message.text == "IPhone 15 Pro/ProMax, 128/256 GB SIM+eSIM")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 23 800 000
● Гарантия 12 месяцев. IMEI-1 официально зарегистрированы (активация регистрации происходит в течение 30 дней)
● Встроенная память - 128/256 ГБ / Версия ОС - iOS 17
● Количество SIM-карт: nano SIM + eSIM
● Дисплей - 6.7" (2796x1290), 2K QHD, OLED
● Камера - 48 МП/ 12 МП / 12 МП
● Видеосъемка (основная камера) - 4K с частотой до 60 кадров/с (3840x2160)
● Процессор - Apple A17 Pro; Материал корпуса – Титан
● Тип разъема для зарядки - USB-C
● Функции зарядки - беспроводная зарядка, быстрая зарядка
● Емкость аккумулятора - Pro: 3274 мА•ч/Promax : 4422 мА•ч
    """, reply_markup=iphone_details)






@dp.message_handler(lambda message: message.text == "Samsung")
async def select(message: types.Message):
    await message.answer(f"""
    Samsung telefonlaridan birini tanlang
    """, reply_markup=samsung_details)

@dp.message_handler(lambda message: message.text == "Смартфон Samsung Galaxy A15 8/256GB, 6/128GB, Android 14, FHD+ 90 Hz, 5000 mA/h, 2 Sim")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 3 099 000
● Заводская комплектация: документация, кабель USB Type-C, скрепка для извлечения слота SIM-карты / карты памяти
● Все IMEI официально зарегистрированы, активация регистрации осуществляется в течение 30 дней. Производитель предоставляет гарантию на свою продукцию в течение 12 месяцев.
● Оперативная память: 6ГБ / 8ГБ
● Размер экрана: 6,5 дюйма
● Емкость аккумулятора: 5000 мА/ч
● Память: 128ГБ / 256ГБ
● Частота обновления экрана: 90 Гц
    """, reply_markup=samsung_details)

@dp.message_handler(lambda message: message.text == "Смартфон Samsung Galaxy S22 Ultra 8 Гб/256 Гб, белый")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 18 961 000
● Тип моноблок (классический)
● Стандарт GSM 900/1800/1900, 3G, 4G LTE, 5G
● Операционная система Android 12
● SIM-карта поддержка 2-х nano SIM-карт, попеременный режим работы
● Материал металл и стекло
● Поддержка 5G Да
● Технология NFC Да
    """, reply_markup=samsung_details)


@dp.message_handler(lambda message: message.text == "Смартфон Samsung Galaxy A05 4GB/128GB 6.7' 50mp, 2SIM, 5000mAh")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 2 000 000 
● Камера 50 МП
● 8-ядерный процессор
● Аккумулятор ёмкостью 5000 мА∙ч
● Разрешение - 720 x 1600
● Объем ОЗУ - 4 ГБ
● Память - 128 ГБ
● Операционная система - Android 13
● Экран 6,7-дюймов HD+
    """, reply_markup=samsung_details)









@dp.message_handler(lambda message: message.text == "Honor")
async def select(message: types.Message):
    await message.answer(f"""
    Honor telefonlaridan birini tanlang
    """, reply_markup=honor_details)

@dp.message_handler(lambda message: message.text == "Смартфон Honor X6a, 4/128 GB, 6/128 GB, 5200 мА/ч")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 2 099 000
● Официальная гарантия от производителя: 1 год. Все IMEI официально зарегистрированы (активация регистрации происходит в течение 30 дней).
● Большой экран 6,7 дюймов позволит с удовольствием смотреть ленту социальных сетей и любимые видео
● Батарея емкостью 5000 мАч порадует своей мощностью, чтобы Вы могли активно использовать смартфон в течении всего дня без страха, что он быстро разрядится
● Несмотря на бюджетность, Honor X6a оснащен четкой камерой 50 Мп, которая порадует тех, кто любит делать качественный контент для своих социальных сетей
    """, reply_markup=honor_details)

@dp.message_handler(lambda message: message.text == "Смартфон Honor X6a, 6/128 GB, 5200 мА/ч")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 2 249 000
● Официальная гарантия от производителя: 1 год. Все IMEI официально зарегистрированы (активация регистрации происходит в течение 30 дней).
● Большой экран 6,7 дюймов позволит с удовольствием смотреть ленту социальных сетей и любимые видео
● Батарея емкостью 5000 мАч порадует своей мощностью, чтобы Вы могли активно использовать смартфон в течении всего дня без страха, что он быстро разрядится
● Несмотря на бюджетность, Honor X6a оснащен четкой камерой 50 Мп, которая порадует тех, кто любит делать качественный контент для своих социальных сетей
● Справа в кнопку включения интегрирован датчик отпечатка пальца, чтобы Вы быстро и легко разблокировали свой смартфон
    """, reply_markup=honor_details)


@dp.message_handler(lambda message: message.text == "Смартфон Honor X8b 8/128/256 GB, NFC, 2 NanoSIM, AMOLED экран с защитой зрения")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 4 782 000
● Официальная гарантия от производителя: 1 год. Все IMEI официально зарегистрированы (активация регистрации происходит в течение 30 дней).
● Приобретая стильный смартфон Honor X8b в магазине In Touch вы бонусом получаете портативный блендер или Honor Gift Box. Важно! Один из двух указанных подарков выбирается случайным образом и выбрать конкретный тип подарка не получится.
● Откройте для себя Honor X8b – смартфон нового поколения, созданный для тех, кто ценит мощность, скорость и качество изображения.
● С емкостью аккумулятора 4500 мА/ч и 35-ваттной технологией HONOR SuperCharge, ваш смартфон будет работать весь день без дополнительной зарядки.
● С размерами 161.05 мм * 74.55 мм * 6.78 мм и весом всего 166 грамм, Honor X8b удобно лежит в руке и легко помещается в карман.
    """, reply_markup=honor_details)












@dp.message_handler(lambda message: message.text == "Back 🚪🏃")
async def select(message: types.Message):
    await message.answer(f"""
    Telefon📱 yoki Noutbukni💻   tanlang
    """, reply_markup=phone_keyword)


# noutbuk
@dp.message_handler(lambda message: message.text == "Noutbuklar")
async def select(message: types.Message):
    await message.answer(f"""
    Noutbuklardan birini tanlang 💻
    """, reply_markup=noutbook_details)

@dp.message_handler(lambda message: message.text == "HP")
async def select(message: types.Message):
    await message.answer(f"""
    HP noutbuklaridan birini tanlang
    """, reply_markup=hp_details)

@dp.message_handler(lambda message: message.text == "ACER")
async def select(message: types.Message):
    await message.answer(f"""
    ACER noutbuklaridan birini tanlang
    """, reply_markup=acer_details)

@dp.message_handler(lambda message: message.text == "LENOVO")
async def select(message: types.Message):
    await message.answer(f"""
    LENOVO noutbuklaridan birini tanlang
    """, reply_markup=lenovo_details)

@dp.message_handler(lambda message: message.text == "THUNDEROBOT")
async def select(message: types.Message):
    await message.answer(f"""
    THUNDEROBOT noutbuklaridan birini tanlang
    """, reply_markup=thunderobot_details)
# hp ----------------------------------------------------------------------------

# 1-hp noutbuk
@dp.message_handler(lambda message: message.text == "Ноутбук HP 15-dy5131wm, 15' FHD, Intel Core i3-1215U, 4,4ГГц, ОЗУ 8ГБ,SSD 256ГБ графика UHD")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 4 900 000
● Память - 8 ГБ оперативной памяти DDR4-3200 МГц (2 x 4 ГБ)
● Графика - Интегрированный ® Графика Intel UHD
● Тип батареи - 3-элементный, литий-ионный аккумулятор емкостью 41 Вт·ч
● Аудио - Два динамика
    """, reply_markup=hp_details)

# 2-hp noutbuk
@dp.message_handler(lambda message: message.text == "Ноутбук HP 250 G10 Core i5-1335U, DDR4 8GB SSD 512GB, 15.6' FHD, Windows, + мышка в подарок")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 7 200 000
● Процессор 10 ядер 12 потоков тактовая частота до 4,6 ГГц с технологией Intel Turbo Boost Кэш 12 МБ
● ОЗУ 8 Гбайт (1 x 8 Гбайт) ОЗУ, DDR4, 3200 МГц
● Windows установлена
● 1 год гарантии
""", reply_markup=hp_details)

# 3-hp noutbuk
@dp.message_handler(lambda message: message.text == "Ноутбук-планшет 2 в 1, HP Envy X360 14-ES0013DX i5-1335U ОЗУ 8 ГБ SSD 512 ГБ 14' FHD")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 9 900 000
● Процессор: Intel Core i5-1335U 13 поколения
● Объём SSD 512 ГБ
● Видеоадаптер: Intel Iris Xe Graphics
● Аудио: Двойные динамики HP, специально настроенные экспертами Bang & Olufsen
● Датчик отпечатка пальца и подсветка клавиатуры Версия операционной системы: Windows 11 Home
● Веб-Камера HP True Vision 5MP с затвором камеры . Премиум дизайн из прочного и легкого аллюминия.
""", reply_markup=hp_details)
# ----------------------------------------------------------------------------------------------

# acer ---------------
# 1-acer noutbuk
@dp.message_handler(lambda message: message.text == "Ноутбук Lenovo Intel Celeron N4020, 8 ГБ DDR4, 256 ГБ SSD, 15.6' DOS")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 3 242 000
● Процессор: Intel Celeron N4020
● Объем оперативной памяти: 8 ГБ
● Видеокарта: Intel UHD Graphics
● Диагональ экрана: 15.6"
● Количество ядер: 2
● Количество потоков: 2
    """, reply_markup=lenovo_details)

# 2-acer noutbuk
@dp.message_handler(lambda message: message.text == "Ноутбук Acer Aspire 5 Intel Core I5-1335U DDR5 8/16 ГБ, 256/512 ГБ SSD FHD 15.6")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 6 899 000
● Процессор: Intel Core i5-1335U
● Быстрый доступ к файлам и операционной системе благодаря SSD-накопителю на 256/512 ГБ
● Качественный 15,6-дюймовый FHD-дисплей с IPS-технологией для яркого и четкого изображения
● Качественный 15,6-дюймовый FHD-дисплей с IPS-технологией для яркого и четкого изображения
● Без операционной системы
● Количество ядер: 10
""", reply_markup=acer_details)

# 3-acer noutbuk
@dp.message_handler(lambda message: message.text == "Ноутбук Asus Vivobook E1504GA Intel Core i3 N305 15.6' FHD IPS 8GB 512 GB, серебро")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 5 400 000
● Процессор Intel Core i3-N305 13 - поколениео 8ядер 8 поток
● Диагональ экрана 15.6″ FHD IPS
● Тип матрицы дисплея IPS
● Видеокарта Intel UHD Graphics
● Твердотельный накопитель 512GB SSD
● Разъемы, порты HDMI, 3.5 мм jack (микрофон/аудио), USB Type-A USB 2.0, USB 3.2 Gen1, USB Type-C USB 3.2 Gen
""", reply_markup=acer_details)

# ______________________________________________________________-

# lenovo
@dp.message_handler(lambda message: message.text == "Ноутбук Lenovo Intel celeron N4500 Установлено Windows и программы Дисплей 15.6 HD")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 3 089 000
● Процессор: Intel® Celeron® Processor N4500
● Тактовая частота CPU: 1.10 GHz
● Максимальная частота процессора: 2.80 GHz
● Количество ядер процессора: 2 ядра
● Дисплей: 15.6" FullHD
● Оперативная память: 4 ГБ DDR4
● Хранилище: 256 ГБ SSD m2
● Установлено Windows и программы
""", reply_markup=lenovo_details)


@dp.message_handler(lambda message: message.text == "Ноутбук Lenovo Intel Celeron N4020 DDR4, 4 ГБ, SSD 256 ГБ, 15.6' HD LCD, cерый")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 2 998 000
● Разрешение: 1366 x 768, HD
● Интерфейсы: USB 2.0, USB 3.0, HDMI, RJ45 (LAN)
● Частота обновления экрана: 60 Гц
● Количество ядер: 2
● Количество потоков: 2
● Видеокарта: Intel UHD Graphics
● Стереодинамики: есть
● Микрофон: есть
● OC: без windows
● Максимальная частота процессора: 2.8 ГГц
""", reply_markup=lenovo_details)

@dp.message_handler(lambda message: message.text == "Ноутбук Lenovo IdeaPad Gaming 3 , DDR4 8GB, AMD RYZEN 5-5500H, GeForce RTX2050 4gb")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 7 734 000
● Видеокарта: NVIDIA GeForce RTX 2050 (4 ГБ видеопамяти GDDR6)
● Оперативная память: 8 ГБ DDR4 (модульный, с возможностью расширения до 16 ГБ)
● Накопитель: 512 ГБ SSD NVMe PCIe
● Операционная система: Windows 11
● Гарантия: 12 месяцов
● Процессор: AMD Ryzen 5-5500H (6 ядер, 12 потоков, тактовая частота до 4.0 ГГц)
● Дисплей: 15.6-дюймовый Full HD IPS LCD
""", reply_markup=lenovo_details)

# __________________________________________

# THUNDEROBOT
@dp.message_handler(lambda message: message.text == "Pre-order 60 days RTX4060 i7-13620H Gaming Laptop 911PLUS 17.3'' 165Hz Notebook Computer Laptops Russian Keyboard Best Laptop")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 204 530 ₽ (-20%)
● Processor Model: i7-13650HX RTX4060
● Brand Name - THUNDEROBOT
● Origin - Mainland China
● Display Size - 16"
● Hard Drive Capacity - 512GB
● Operating System - Windows 11
● Hard Drive Type - SSD
● RAM - 16GB
● Type - Gaming Laptop
● Graphics Brand - nVIDIA
""", reply_markup=thunderobot_details)



@dp.message_handler(lambda message: message.text == "ZERO RTX4060 i7-13650HX Gaming Laptop 16'' 240Hz 2.5K DDR5 Notebook Laptops Gamer Russian Keyboard")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 90 000 ₽ 
● Processor Model: i7-13650HX RTX4060
● Brand Name - THUNDEROBOT
● Origin - Mainland China
● Display Size - 16"
● Hard Drive Capacity - 512GB
● Operating System - Windows 11
● Hard Drive Type - SSD
● RAM - 16GB
● Type - Gaming Laptop
""", reply_markup=thunderobot_details)



@dp.message_handler(lambda message: message.text == "Ninkear Laptops N16 Pro 16' 2.5K 165Hz Intel Core i7-13620H WiFi 6 32GB RAM + 1TB SSD Office Computer Laptop Windows 11 Notebook")
async def select(message: types.Message):
    await message.answer(f"""
● Цена: 111 182 ₽ (-20%)
● Processor Model: Intel core i7-13620H
● Brand Name - DERE
● Origin - Mainland China
● Display Size 16"
● Hard Drive Capacity 1TB
● Memory Type - DDR4
""", reply_markup=thunderobot_details)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
