from aiogram import Bot, Dispatcher, executor, types
from config import telegram_token
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


bot = Bot(token=telegram_token)
dp = Dispatcher(bot)


HELP_COMMAND = """
<b>/start</b> - <em>начать работу с ботом</em>
<b>/help</b> - <em>список комманд</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>заготовленное фото</em>
"""

async def on_startup(_):
    print('Я запустился')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/rank')
b2 = KeyboardButton('/rank2')
b3 = KeyboardButton('/rank3')
b4 = KeyboardButton('/rank4')
b5 = KeyboardButton('/rank5')
b6 = KeyboardButton('/rank6')
b7 = KeyboardButton('/rank7')
kb.add(b1, b2, b3, b4, b5, b6, b7)


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f'<em><b>Здравствуй, {user_name}!</b> Добро пожаловать в нашего бота! Здесь ты найдешь вводную информацию о званиях.</em>', parse_mode="HTML",
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands='rank')
async def rank_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='Рядовой', callback_data='soldier1')
    ib2 = InlineKeyboardButton(text='Ефрейтор', callback_data='soldier2')
    ikb.add(ib1, ib2)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://forma-odezhda.com/image/data/wp-content/uploads/2017/12/zvaniya-v-armii-rf-03.jpg',
                         caption='Рядовые и матросы на погонах не имеют никаких знаков различия. Ефрейторы и старшие матросы имеют одну горизонтальную лычку.',
                         reply_markup=ikb)

@dp.callback_query_handler(text='soldier1')
async def rank_callback(callback: types.CallbackQuery):
    await callback.answer(text='Рядовой - самое низшее звание в нашей армии. Ниже могут быть только курсанты или рекруты.')

@dp.callback_query_handler(text='soldier2')
async def rank_callback(callback: types.CallbackQuery):
    await callback.answer(text='Ефрейтором назначается самый лучший из рядовых, которые отличились во время службы. Ефрейтор обычно заменят командира в его отсутствие.')


@dp.message_handler(commands='rank2')
async def rank_command(message: types.Message):
    ikb2 = InlineKeyboardMarkup(row_width=4)
    ib2_1 = InlineKeyboardButton(text='Младший сержант', callback_data='option1')
    ib2_2 = InlineKeyboardButton(text='Сержант', callback_data='option2')
    ib2_3 = InlineKeyboardButton(text='Старший сержант', callback_data='option3')
    ib2_4 = InlineKeyboardButton(text='Старшина', callback_data='option4')
    ikb2.add(ib2_1, ib2_2, ib2_3, ib2_4)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='https://forma-odezhda.com/image/data/wp-content/uploads/2017/12/zvaniya-v-armii-rf-04.jpg',
        caption='Имеют знаки различия в виде матерчатых галунов — лычек. Расцветки лычек:\nПолевая форма — защитного цвета;\nПовседневная и парадная форма — жёлтого цвета;',
        reply_markup=ikb2)

@dp.callback_query_handler(text='option1')
async def rank2_callback(callback: types.CallbackQuery):
    await callback.answer(text='Данное воинское звание является выше Ефрейтора и выше рядового. Обычно данное звание присваивается солдату, который уходит в запас. Конечно если он отличился во время службы.')

@dp.callback_query_handler(text='option2')
async def rank2_callback(callback: types.CallbackQuery):
    await callback.answer(text='Во многих странах мира, в том числе и в России, звание сержант даётся солдату младшего командного состава.')

@dp.callback_query_handler(text='option3')
async def rank2_callback(callback: types.CallbackQuery):
    await callback.answer(text='Старший сержант безусловно выше обычного сержанта, но всё ещё подчиняется старшине.')

@dp.callback_query_handler(text='option4')
async def rank2_callback(callback: types.CallbackQuery):
    await callback.answer(text='Старшиной назначается лучший из старших сержантов. Причём старший сержант должен прослужить не меньше 6 месяцев в данном звании.')


@dp.message_handler(commands='rank3')
async def rank3_command(message: types.Message):
    ikb3 = InlineKeyboardMarkup(row_width=2)
    ib3_1 = InlineKeyboardButton(text='Прапорщик', callback_data='options1')
    ib3_2 = InlineKeyboardButton(text='Старший прапорщик', callback_data='options2')
    ikb3.add(ib3_1, ib3_2)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://avatars.dzeninfra.ru/get-zen_doc/1574327/pub_5dd69827992239515030f9f8_5dd6996b18187b7aa623100d/scale_1200',
                         caption='Имеют знаки различия в виде маленьких звёздочек, расположенных вертикально. Погоны схожи с офицерскими, но без просветов и могут иметь канты.',
                         reply_markup=ikb3)

@dp.callback_query_handler(text='options1')
async def rank3_callback(callback: types.CallbackQuery):
    await callback.answer(text='Воинское звание Российской армии, которое следует после старшины, но всё ещё ниже офицеров.')

@dp.callback_query_handler(text='options2')
async def rank3_callback(callback: types.CallbackQuery):
    await callback.answer(text='Старший прапорщик присваивается отличившимся прапорщикам, следующая ступень офицерский состав армии России.')


@dp.message_handler(commands='rank4')
async def rank_command(message: types.Message):
    ikb4 = InlineKeyboardMarkup(row_width=4)
    ib4_1 = InlineKeyboardButton(text='Младший лейтенант', callback_data='ensign1')
    ib4_2 = InlineKeyboardButton(text='Лейтенант', callback_data='ensign2')
    ib4_3 = InlineKeyboardButton(text='Старший лейтенант', callback_data='ensign3')
    ib4_4 = InlineKeyboardButton(text='Капитан', callback_data='ensign4')
    ikb4.add(ib4_1, ib4_2, ib4_3, ib4_4)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='https://avatars.dzeninfra.ru/get-zen_doc/1781308/pub_5dd69827992239515030f9f8_5dd6996b576a853bcc85b4a0/scale_1200',
        caption='Одна вертикально расположенная полоска — просвет. Звёздочки металлические, маленькие (13 мм). На полевых погонах просвета нет.',
        reply_markup=ikb4)

@dp.callback_query_handler(text='ensign1')
async def rank4_callback(callback: types.CallbackQuery):
    await callback.answer(text='Начинающим офицерам присваивается звание младшего лейтенанта. именно с этого звания становятся офицерами.')

@dp.callback_query_handler(text='ensign2')
async def rank4_callback(callback: types.CallbackQuery):
    await callback.answer(text='Лейтенант, также переводится, как заместитель. Воинское звание следующее за младшим лейтенантом.')

@dp.callback_query_handler(text='ensign3')
async def rank4_callback(callback: types.CallbackQuery):
    await callback.answer(text='Старший лейтенант - очередное воинское звание всё ещё младшего офицерского состава.')

@dp.callback_query_handler(text='ensign4')
async def rank4_callback(callback: types.CallbackQuery):
    await callback.answer(text='Данное звание существует достаточно давно. Капитан обычно командует целой ротой, далее идёт старший офицерский состав.')


@dp.message_handler(commands='rank5')
async def rank_command(message: types.Message):
    ikb5 = InlineKeyboardMarkup(row_width=3)
    ib5_1 = InlineKeyboardButton(text='Майор', callback_data='major1')
    ib5_2 = InlineKeyboardButton(text='Подполковник', callback_data='major2')
    ib5_3 = InlineKeyboardButton(text='Полковник', callback_data='major3')
    ikb5.add(ib5_1, ib5_2, ib5_3)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='https://avatars.dzeninfra.ru/get-zen_doc/1779726/pub_5dd69827992239515030f9f8_5dd6996bf45e3c5279deb189/scale_1200',
        caption='Два просвета и бо́льшие по размеру металлические звёздочки (20 мм). На полевых погонах просвета нет.',
        reply_markup=ikb5)

@dp.callback_query_handler(text='major1')
async def rank5_callback(callback: types.CallbackQuery):
    await callback.answer(text='Майор - даётся в качестве начального звания в старшем офицерском составе армии.')

@dp.callback_query_handler(text='major2')
async def rank5_callback(callback: types.CallbackQuery):
    await callback.answer(text='Промежуточное звание старшего офицерского состава, между майором и полковником.')

@dp.callback_query_handler(text='major3')
async def rank5_callback(callback: types.CallbackQuery):
    await callback.answer(text='Крайнее звание старшего офицерского звания армии России.')


@dp.message_handler(commands='rank6')
async def rank_command(message: types.Message):
    ikb6 = InlineKeyboardMarkup(row_width=2)
    ib6_1 = InlineKeyboardButton(text='Генерал-майор', callback_data='m_general1')
    ib6_2 = InlineKeyboardButton(text='Генерал-лейтенант', callback_data='m_general2')
    ib6_3 = InlineKeyboardButton(text='Генерал-полковник', callback_data='m_general3')
    ikb6.add(ib6_1, ib6_2, ib6_3)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='https://avatars.dzeninfra.ru/get-zen_doc/1922981/pub_5dd69827992239515030f9f8_5dd6996ba9876a758f94e317/scale_1200',
        caption='Вертикально расположенные вышитые звёздочки большего размера (22 мм), просветов нет.',
        reply_markup=ikb6)

@dp.callback_query_handler(text='m_general1')
async def rank6_callback(callback: types.CallbackQuery):
    await callback.answer(text='Первое звание высшего офицерского состава. Обычно генерал майору даётся в распоряжение целая дивизия.')

@dp.callback_query_handler(text='m_general2')
async def rank6_callback(callback: types.CallbackQuery):
    await callback.answer(text='Данное звание следует за генерал-лейтенантом. Также известно в некоторых странах, как заместитель.')

@dp.callback_query_handler(text='m_general3')
async def rank6_callback(callback: types.CallbackQuery):
    await callback.answer(text='Одно из высших званий в армии Российской федерации.')


@dp.message_handler(commands='rank7')
async def rank_command(message: types.Message):
    ikb7 = InlineKeyboardMarkup(row_width=2)
    ib7_1 = InlineKeyboardButton(text='Генерал-армии', callback_data='s_general1')
    ib7_2 = InlineKeyboardButton(text='Маршал', callback_data='s_general2')
    ikb7.add(ib7_1, ib7_2)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='https://avatars.dzeninfra.ru/get-zen_doc/1716636/pub_5dd69827992239515030f9f8_5dd6996b849b846d505a89e5/scale_2400',
        caption='Генерал армии, адмирал флота — одна большая вышитая звезда диаметром 40 мм (с 22 февраля 2013 года)[11]; над ней расположена вышитая звезда, обрамлённая венком (цвет звезды соответствует роду службы, диаметр венка 35 мм)[10]. \nМаршал Российской Федерации — одна большая вышитая звезда диаметром 40 мм, на фоне радиально расходящихся серебряных лучей, образующих пятиугольник; над звездой — вышитый герб России (без геральдического щита) диаметром 40 мм.',
        reply_markup=ikb7)

@dp.callback_query_handler(text='s_general1')
async def rank7_callback(callback: types.CallbackQuery):
    await callback.answer(text='В некоторых странах мира, данное звание является высшим званием армии.')

@dp.callback_query_handler(text='s_general2')
async def rank7_callback(callback: types.CallbackQuery):
    await callback.answer(text='Маршал - высшее воинское звание в российской армии.')


@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands='give')
async def give_command(message: types.Message):
    await message.answer('Поздравляю! Ты нашел секретный команду. В подарок я тебе отправляю крутой стикер.')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEMPOhmXZk01msvrs5upnB_IxJBDHxI0gACASYAAsqriUshdPqhh3WEnTUE')



@dp.message_handler()
async def emoji(message: types.Message):
    await message.answer(message.text + '❤️ ')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)