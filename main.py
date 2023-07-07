import os

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')
bot = AsyncTeleBot(TOKEN, parse_mode='HTML')


bot = AsyncTeleBot("6329139729:AAEgTQ7raiKCHY8aeOGi-xJEhzmPZJBmi68")

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    qwex = '/help'
    one_button = '16к'
    two_button = '19к'
    three_button = '22к'
    w_button = '23к'
    q_button = '20к'
    e_button = '27к'
    r_button = '26к'
    t_button = '28к'
    y_button = '36к'
    u_button = '24к'
    i_button = '42к'
    o_button = '43к'
    p_button = '45к'
    a_button = '46к'
    s_button = '49к'
    d_button = '52к'
    f_button = '52к'
    g_button = '56к'
    h_button = '59к'
    j_button = '60к'
    k_button = '62к'
    l_button = '74к'
    z_button = '76к'
    x_button = '81к'
    c_button = '83к'
    v_button = '84к'
    b_button = '93к'
    n_button = '98к'
    m_button = '100к'
    qw_button = '103к'
    er_button = '115к'
    rt_button = '125к'
    ty_button = '149к'
    markup.add(qwex, one_button, two_button, three_button, w_button, q_button, e_button, r_button, t_button, y_button, u_button, i_button, o_button, p_button, a_button, s_button, d_button, f_button, g_button, h_button, j_button, k_button, l_button, z_button, x_button, c_button, v_button, b_button, n_button, m_button, qw_button, er_button, rt_button, ty_button, row_width=2)
    await bot.reply_to(message, 'Введите свой бюджет, на который вы хотите купить ноутбук', reply_markup= markup)
    print(message)


@bot.message_handler(commands=['Hi'])
async def send_w(send_message):
    chat_id = send_message.from_user.id
    await bot.send_message(chat_id, 'Привет рад тебя видеть!', disable_notification=True)


@bot.message_handler(commands=['qwe'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_photo(chat_id, 'https://kartinkof.club/uploads/posts/2022-03/1648288320_1-kartinkof-club-p-mem-ladno-s-zhak-fresko-1.jpg', caption='Заголовок')


@bot.message_handler(commands=['s'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAIiDWSkCw94sjKtOGX7xi92w_eBbMpEAAJjAAPz7BshTAKIMFXJIN8vBA')

@bot.message_handler(commands=['del'])
async def send_bold(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<b>жирный</b>', parse_mode="HTML")


@bot.message_handler(commands=['inline'])
async def send_bold(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<i>курсив</i>', parse_mode="HTML")

@bot.message_handler(comands=['taim'])
async def send_welcome(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_message(chat_id, 'Начался таймер 5 сек')
    for i in range(1, 6):
        await asyncio.sleep(1)
        await bot.edit_message_text(f'{5-i} Секунд прошло', chat_id, bot_message.id)
    await bot.delete_message(chat_id, bot_message.id)


@bot.message_handler(commands=['qwer'])
async def send_welcome(message):
    chat_id = message.chat.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    one_button = '1'
    two_button = '2'
    three_button = '3'
    markup.add(one_button, two_button, three_button, row_width=2)
    await bot.send_message(chat_id, '4', reply_markup=markup)

def generate_reply_keyboard(list_buttons, row):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*list_buttons, row_width=row)
    return markup

@bot.message_handler(commands=['qwert'])
async def send_welcome(message):
    chat_id = message.from_user.id
    list_buttons = '5', '6', '7'
    await bot.send_message(chat_id, '8', reply_markup=generate_reply_keyboard(list_buttons, 2))


@bot.message_handler(commands=['fg'])
async def send_welcome(message, button1=None, button2=None, button3=None):
    chat_id = message.from_user.id
    from telebot.types import InlineKeyboardButton
    markup = InlineKeyboardButton()
    button = InlineKeyboardButton('11', callback_data='first')
    button = InlineKeyboardButton('12', callback_data='second')
    button = InlineKeyboardButton('13', callback_data='first')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    await bot.send_message(chat_id, '14', reply_markup=markup)


@bot.message_handler(commands=['w'])
async def send_welcome(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, '🎲')
    print(bot_message.dice.value)

@bot.message_handler(commands=['q'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_document(chat_id, open('text.txt', 'rb'))

@bot.message_handler(commands=['rer'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id, 58.002592, 56.250967)



@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    chat_id = message.from_user.id
    text_message = message.text
    text_message = text_message.lower()
    if 'дела' in text_message or 'настроение' in text_message:
        await bot.reply_to(message, 'Хорошо, а у тебя?')
    elif 'шутка' in text_message or 'анекдот' in text_message:
        await bot.reply_to(message, 'Колобок повесился')
    elif 'чд' in text_message or 'Чд' in text_message:
        await bot.reply_to(message, 'Ничего')
    elif 'кд' in text_message or 'Кд' in text_message:
        await bot.reply_to(message, 'Норм')
    elif 'пон' in text_message or 'Пон' in text_message:
        await bot.reply_to(message, 'Ага')
    elif '16к' in text_message or '16 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/d4t-uAys8EjZPLujvkgYQZw6OumbjpxK4AOTVr5eQ1Q/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1499216_v01_b.jpg', caption='Ноутбук IRBIS NB NB69, 13.3", IPS, Intel Atom Z3735F, 4-ядерный, 2ГБ DDR3, 32ГБ eMMC, Intel HD Graphics , серебристый')
    elif '19к' in text_message or '19 тысяч' in text_message:
        await bot.send_photo(chat_id,'https://technosuccess.ru/images/thumbnails/680/680/detailed/6063/8594314_1_1682335517.jpg', caption='Ноутбук Digma EVE 15 P418, 15.6", IPS, Intel Celeron N4020C, 2-ядерный, 4ГБ 128ГБ eMMC, Intel UHD Graphics 600, серый космос')
    elif '22к' in text_message or '22 тысячи' in text_message:
        await bot.send_photo(chat_id,'https://items.s1.citilink.ru/1470838_v14_b.jpg', caption='Ноутбук Digma EVE 15 P417, 15.6", IPS, Intel Pentium J3710, 4-ядерный, 4ГБ 128ГБ eMMC, Intel HD Graphics 405, темно-серый')
    elif '23к' in text_message or '23 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1932412_v04_b.jpg', caption='Ноутбук CHUWI GemiBook Xpro 14.1", IPS, Intel Celeron N100, 4-ядерный, 8ГБ LPDDR5, 256ГБ SSD, Intel UHD Graphics , серый')
    elif '20к' in text_message or '20 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1497619_v01_b.jpg', caption='Ноутбук Digma EVE 11 C421Y, 11.6", трансформер, TN, Intel Celeron N4020C, 2-ядерный, 4ГБ 128ГБ eMMC, Intel UHD Graphics 600, черный')
    elif '27к' in text_message or '27 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1840570_v01_b.jpg', caption='Ноутбук HP 250 G8, 15.6", SVA, Intel Celeron N4020, 2-ядерный, 4ГБ DDR4, 1000ГБ, Intel UHD Graphics 600, темно-серебристый')
    elif '26к' in text_message or '26 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1882183_v01_b.jpg', caption='Ноутбук iRU Калибр 15GLG, 15.6", IPS, Intel Celeron N4020, 2-ядерный, 4ГБ 1ТБ, Intel HD Graphics 600, черный')
    elif '28к' in text_message or '28 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1490205_v01_b.jpg', caption='Ноутбук HP 255 G8, 15.6", SVA, AMD Athlon Silver 3050U, 2-ядерный, 4ГБ DDR4, 1000ГБ, AMD Radeon , темно-серебристый')
    elif '69к' in text_message or '69 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1892716_v01_b.jpg', caption='Ноутбук Huawei MateBook D 16 16", IPS, Intel Core i5 12450H, 8-ядерный, 16ГБ LPDDR4x, 512ГБ SSD, Intel UHD Graphics , серый космос')
    elif '46к' in text_message or '46 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1895065_v03_b.jpg', caption='Ноутбук Lenovo V15 G2 ALC, 15.6", TN, AMD Ryzen 5 5500U, 6-ядерный, 8ГБ DDR4, 256ГБ SSD, AMD Radeon , черный')
    elif '43к' in text_message or '43 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://static.price.ru/images/models/-/noutbuk/huawei-matebook-d-14-nbd-wdi9/2e90e4ea7df6f3fba1594814194a80e9.JPEG', caption='Ноутбук Huawei MateBook D 15 BOD-WDI9, 15.6", IPS, Intel Core i3 1115G4, 2-ядерный, 8ГБ DDR4, 256ГБ SSD, Intel UHD Graphics , серый космос')
    elif '42к' in text_message or '42 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1797219_v01_b.jpg', caption='Ноутбук HIPER Expertbook MTL1577, 15.6", IPS, AMD Ryzen 5 5600U, 6-ядерный, 8ГБ DDR4, 256ГБ SSD, AMD Radeon , серый')
    elif '45к' in text_message or '45 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://img.2bit.ru/images/items/597/596301-1828625_v03_b.jpg', caption='Ноутбук Digma Pro Fortis M, 15.6", IPS, Intel Core i5 10210U, 4-ядерный, 8ГБ 512ГБ SSD, Intel UHD Graphics , серый')
    elif '52к' in text_message or '52 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://img.2bit.ru/images/items/597/596301-1828625_v03_b.jpg', caption='Ноутбук ASUS A516JP-EJ461, 15.6", TN, Intel Core i7 1065G7, 4-ядерный, 16ГБ DDR4, 512ГБ SSD, NVIDIA GeForce MX330 - 2 ГБ, серебристый')
    elif '59к' in text_message or '59 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/s4pQpEDIqDCMt29-GGqyx0YWx05HXIGFx6u_2KiztkI/resizing_type:fit/gravity:sm/width:400/height:400/plain/items/1936338_v01_b.jpg', caption='Ноутбук Huawei MateBook D 15 BoM-WFP9, 15.6", IPS, AMD Ryzen 7 5700U, 8-ядерный, 16ГБ DDR4, 512ГБ SSD, AMD Radeon , серебристый')
    elif '49к' in text_message or '49 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1797151_v01_b.jpg', caption='Ноутбук HIPER DZEN MTL1569, 15.6", IPS, Intel Core i5 1135G7, 4-ядерный, 8ГБ DDR4, 256ГБ SSD, Intel Iris Xe graphics , серый')
    elif '69к' in text_message or '69 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/6LpSw0whJS_FaJV6roXe1IG-QohwR6LVGzhrvmxrisA/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1681278_v03_b.jpg', caption='Ноутбук игровой MSI GF63 Thin 11UC-207XRU, 15.6", IPS, Intel Core i5 11400H, 6-ядерный, 16ГБ DDR4, 512ГБ SSD, NVIDIA GeForce RTX 3050 для ноутбуков - 4 ГБ, черный')
    elif '62к' in text_message or '62 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/04GDGnTGr7dfK1d402-jnGm95R1upGEpIoHOrEZNmlQ/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1892720_v04_b.jpg', caption='Ноутбук Huawei MateBook D 15 BoD-WFH9, 15.6", IPS, Intel Core i5 1135G7, 4-ядерный, 16ГБ DDR4, 512ГБ SSD, Intel Iris Xe graphics , серебристый')
    elif '103к' in text_message or '103 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/dv1UF3DGhHzTrWPv37mMHyTDWnnI9qAsavznsWHiQFk/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1660309_v01_b.jpg', caption='Ноутбук игровой MSI Sword 15 A12UE-487XRU, 15.6", IPS, Intel Core i7 12700H, 14-ядерный, 16ГБ DDR4, 512ГБ SSD, NVIDIA GeForce RTX 3060 для ноутбуков - 6 ГБ, белый')
    elif '60к' in text_message or '60 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://avatars.mds.yandex.net/get-mpic/1884605/img_id1555291989976301972.jpeg/orig', caption='Ноутбук MSI Modern 14 C5M-010XRU, 14", IPS, AMD Ryzen 5 5625U, 6-ядерный, 16ГБ DDR4, 512ГБ SSD, AMD Radeon , черный')
    elif '44к' in text_message or '44 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://avatars.mds.yandex.net/get-mpic/4303516/img_id4872597255853481157.jpeg/orig', caption='Ноутбук Huawei MateBook D 15 BOD-WDI9, 15.6", IPS, Intel Core i3 1115G4, 2-ядерный, 8ГБ DDR4, 256ГБ SSD, Intel UHD Graphics , серебристый')
    elif '84к' in text_message or '84 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1800489_v01_b.jpg', caption='Ноутбук игровой MSI GF63 Thin 11UD-206XRU, 15.6", IPS, Intel Core i5 11400H, 6-ядерный, 16ГБ DDR4, 512ГБ SSD, NVIDIA GeForce RTX 3050 Ti для ноутбуков - 4 ГБ, черный')
    elif '83к' in text_message or '83 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/INkgIfgCTCzH8Xn8c75DsjwS69NkI94Lyap8bu7aPk8/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1681285_v03_b.jpg', caption='Ноутбук игровой MSI Sword 17 A11UD-809XRU, 17.3", IPS, Intel Core i5 11400H, 6-ядерный, 16ГБ DDR4, 512ГБ SSD, NVIDIA GeForce RTX 3050 Ti для ноутбуков - 4 ГБ, белый')
    elif '36к' in text_message or '36 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/FNhD5346ZYkjgCAXv_a7w5QpLiQvzhzOSJObh1rJPIw/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1775351_v05_b.jpg', caption='Ноутбук CHUWI Corebook X 14, 14", IPS, Intel Core i3 10110U, 2-ядерный, 8ГБ DDR4, 512ГБ SSD, Intel UHD Graphics , серый')
    elif '100к' in text_message or '100 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://avatars.mds.yandex.net/get-mpic/7516119/img_id5635268548098807890.jpeg/orig', caption='Ноутбук игровой MSI Pulse GL66 12UEK-289XRU, 15.6", IPS, Intel Core i5 12500H, 12-ядерный, 8ГБ DDR4, 512ГБ SSD, NVIDIA GeForce RTX 3060 для ноутбуков - 6 ГБ, серый')
    elif '149к' in text_message or '149 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/CTcb26p-zhQpVAAwO7nFZYOIjxCCpS5Pur047OjdptU/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1834983_v01_b.jpg', caption='Ноутбук игровой MSI Vector GP66 12UGSO-671RU, 15.6", IPS, Intel Core i7 12700H, 14-ядерный, 16ГБ DDR5, 1ТБ SSD, NVIDIA GeForce RTX 3070 Ti для ноутбуков - 8 ГБ, черный')
    elif '76к' in text_message or '76 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1892716_v01_b.jpg', caption='Ноутбук Huawei MateBook D 16 RLEF-X, 16", IPS, Intel Core i5 12450H, 8-ядерный, 16ГБ LPDDR4x, 512ГБ SSD, Intel UHD Graphics , серый')
    elif '54к' in text_message or '54 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/QD5keCe9NFP5LllTYrXkl0JFz6eRDpwmpaeyp16bVf4/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1892727_v01_b.jpg', caption='Ноутбук Huawei MateBook D 14 NbDE-WDH9, 14", IPS, Intel Core i5 1155G7, 4-ядерный, 8ГБ DDR4, 512ГБ SSD, Intel Iris Xe graphics , серебристый')
    elif '93к' in text_message or '93 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1800399_v01_b.jpg', caption='Ноутбук игровой MSI Sword 17 A11UD-808XRU, 17.3", IPS, Intel Core i7 11800H, 8-ядерный, 16ГБ DDR4, 512ГБ SSD, NVIDIA GeForce RTX 3050 Ti для ноутбуков - 4 ГБ, белый')
    elif '119к' in text_message or '119 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1840693_v01_b.jpg', caption='Ноутбук игровой ADATA XPG Xenia 15KC, 15.6", IPS, Intel Core i7 11800H, 8-ядерный, 32ГБ DDR4, 1ТБ SSD, NVIDIA GeForce RTX 3070 для ноутбуков - 8 ГБ, черный')
    elif '98к' in text_message or '98 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/UoHA08gMf7xzlqVUsfmC9Pt4RPUpfZOwDcu-t8_LtAU/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1808579_v01_b.jpg', caption='Ноутбук Xiaomi Redmibook Pro, 15.6", IPS, Intel Core i5 12450H, 8-ядерный, 16ГБ LPDDR5, 512ГБ SSD, Intel UHD Graphics , серебристый')
    elif '56к' in text_message or '56 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/OOL3I9fz59voes8T2YWqzH6plmyC6o-dalBV5Krxx1Q/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1783769_v15_b.jpg', caption='Ноутбук Digma Pro Fortis M, 15.6", IPS, Intel Core i7 10710U, 6-ядерный, 16ГБ 512ГБ SSD, Intel UHD Graphics , серый')
    elif '81к' in text_message or '81 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1861103_v01_b.jpg', caption='Ноутбук Xiaomi Redmibook Pro, 14", IPS, AMD Ryzen 5 5625U, 6-ядерный, 16ГБ DDR4, 512ГБ SSD, AMD Radeon , серый')
    elif '74к' in text_message or '74 тысячи' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1924840_v03_b.jpg', caption='Ноутбук игровой Lenovo IP Gaming 3 16ARH7, 16", IPS, AMD Ryzen 5 6600H, 6-ядерный, 8ГБ DDR5, 512ГБ SSD, NVIDIA GeForce RTX 3050 для ноутбуков - 4 ГБ, серый')
    elif '125к' in text_message or '125 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://items.s1.citilink.ru/1840807_v01_b.jpg', caption='Ноутбук игровой ADATA XPG Xenia 16RX, 16.1", IPS, AMD Ryzen 7 6800H, 8-ядерный, 16ГБ DDR5, 1ТБ SSD, AMD Radeon RX6650XT - 8 ГБ, черный')
    elif '115к' in text_message or '115 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/AUihBwaYXT-EAhGILql6XGol47VAp5l7gDaojt4EamI/resizing_type:fit/gravity:sm/width:400/height:400/plain/items/1835015_v01_b.jpg', caption='Ноутбук игровой MSI Pulse GL66 12UEK-220RU, 15.6", IPS, Intel Core i7 12700H, 14-ядерный, 16ГБ DDR4, 512ГБ SSD, NVIDIA GeForce RTX 3060 для ноутбуков - 6 ГБ, серый')
    elif '59к' in text_message or '59 тысяч' in text_message:
        await bot.send_photo(chat_id, 'https://cdn.citilink.ru/tVrLWNiUx6HEAjlO8Ww6BycLP0d2lqv4sN-GHnXzvog/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1848474_v03_b.jpg', caption='Ноутбук MSI Modern 15 B12HW-002XRU, 15.6", IPS, Intel Core i5 1235U, 10-ядерный, 8ГБ DDR4, 512ГБ SSD, Intel Arc A370M - 4 ГБ, черный')
    elif 'к' in text_message or 'тысяч' in text_message:
        await bot.reply_to(message, '')
    elif 'к' in text_message or 'тысяч' in text_message:
        await bot.reply_to(message, '')
    elif 'к' in text_message or 'тысяч' in text_message:
        await bot.reply_to(message, '')






import asyncio

asyncio.run(bot.polling())
