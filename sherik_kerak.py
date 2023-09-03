from aiogram import types, Bot, executor, Dispatcher
from aiogram.dispatcher.filters import Text
from configg import TOKEN
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import re
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#TOKEN = "5829827642:AAFEDvw4abmyqabTHKHVX-m-ae3O9qRZz_k"
PHONE_PATTERN = re.compile("^\+998[0-9]{9}$")

class ProfileState(StatesGroup):
    
    Ism = State()
    Texnologiya = State()
    Nomer = State()
    Hudud = State()
    Narx = State()
    Kasb = State()
    Vaqt = State()
    Maqsad = State()


storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


async def on_startup(_):
    print("Bot muvaffaqiyatli ishga tushurildi")


reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
knop1 = KeyboardButton(text="Sherik kerak")
knop2 = KeyboardButton(text="Ish joyi kerak")
knop3 = KeyboardButton(text="Hodim kerak")
knop4 = KeyboardButton(text="Ustoz kerak")
knop5 = KeyboardButton(text="Shogird kerak")
reply_buttons.add(knop1, knop2)
reply_buttons.add(knop3, knop4)
reply_buttons.add(knop5)


reply_button = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text="ha")
btn2 = KeyboardButton(text="yo'q")
reply_button.add(btn1,btn2)



@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    user = types.User.get_current()
    await message.answer(text=f"<b>Assalom aleykum {user['first_name']}\nUstozShogird kanaliga xush kelibsiz<b>,\n\n/help yordam buyrug'i orqali nimalarga qodirligimni bilib oling!", reply_markup=reply_buttons,)# parse_mode="HTML")
   


@dp.message_handler(Text(equals="Sherik kerak"))
async def Sherik_kerak(message: types.Message):
    await message.answer(text=f"<b>Sherik topish uchun ariza berish<b> \n\nHozir sizga bir nechta savollar beriladi.\nHar biriga javob bering\nOxirida hammasi to'g'ri bo'lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.\n\n<b>Ism, familiyangizni kiriting?<b>",) 
                         #parse_mode="HTML")
    await ProfileState.Ism.set()
    



@dp.message_handler(state=ProfileState.Ism)
async def set_Ism(message: types.Message, state: FSMContext):
    await state.update_data(Ism=message.text)
    await message.answer(text=f"<b>📚 Texnologiya:<b>\n\nTalab qilinadigan texnologiyalarni kiriting?\nHar biriga javob bering\nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\n<u>Java, C++, C#<u>",) 
                         #parse_mode="HTML")
    await ProfileState.next()
    

@dp.message_handler(state=ProfileState.Texnologiya)
async def set_texnologiya(message:types.Message, state: FSMContext):
    await state.update_data(Texnologiya=message.text)
    await message.answer(text=f"<b>📞 Aloqa:<b> \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67",) 
                            #parse_mode="HTML")") 
    await ProfileState.next()



@dp.message_handler(lambda message: not PHONE_PATTERN.match(message.text), state=ProfileState.Nomer)
async def error_nomer(message: types.Message, state: FSMContext):
    await message.answer(text="Siz notog'ri raqam kiritdingiz!!!")
    


@dp.message_handler(state=ProfileState.Nomer)
async def set_nomer(message: types.Message, state: FSMContext):
    await state.update_data(Nomer=message.text)
    await message.answer(text=f"<b>🌐 Hudud:<b>\n\Qaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.",)# parse_mode="HTNL")
    await ProfileState.next()


@dp.message_handler(state=ProfileState.Hudud)
async def set_texnologiya(message:types.Message, state: FSMContext):
    await state.update_data(Hudud=message.text)
    await message.answer(text=f"<b>💰 Narxi:<b>\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?",) 
                            #parse_mode="HTML")") 
    await ProfileState.next()



@dp.message_handler(lambda message: not message.text.isdigit(), state=ProfileState.Narx)
async def not_allow_age(message: types.Message, state: FSMContext):
    await message.answer(text="Siz jo'natgan xabar faqat sonlardan iborat bo'lishi kerak")



@dp.message_handler(state=ProfileState.Narx)
async def set_texnologiya(message:types.Message, state: FSMContext):
    await state.update_data(Narx=message.text)
    await message.answer(text=f"<b>👨🏻‍💻 Kasbi:<b>\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba",) 
                            #parse_mode="HTML")") 
    await ProfileState.next()



@dp.message_handler(state=ProfileState.Kasb)
async def set_texnologiya(message:types.Message, state: FSMContext):
    await state.update_data(Kasb=message.text)
    await message.answer(text=f"<b>🕰 Murojaat qilish vaqti:<b>\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00",) 
                            #parse_mode="HTML")") 
    await ProfileState.next()



@dp.message_handler(state=ProfileState.Vaqt)
async def set_texnologiya(message:types.Message, state: FSMContext):
    await state.update_data(Vaqt=message.text)
    await message.answer(text=f"<b>🔎 Maqsad:<b>\n\nMaqsadingizni qisqacha yozib bering.",) 
                            #parse_mode="HTML")") 
    await ProfileState.next()




@dp.message_handler(state=ProfileState.Maqsad)
async def set_texnologiya(message:types.Message, state: FSMContext):
    await state.update_data(Maqsad=message.text)
    data = await state.get_data()
    user = message.get_current()
    text = f"<b>Sherik kerak:<b>\n\n🏅 Sherik: {data['Ism']}\n📚 Texnologiya: {data['Texnologiya']}\n🇺🇿 Telegram: {user['from']['username']} \n📞 Aloqa: {data['Nomer']}\n🌐 Hudud: {data['Hudud']}\n💰 Narxi: {data['Narx']}\n 👨🏻‍💻 Kasbi: {data['Kasb']}\n🕰 Murojaat qilish vaqti: {data['Vaqt']}\n🔎 Maqsad: {data['Maqsad']}\n\n#sherik\n\nBarcha ma'lumotlar to'g'rimi?"
    await message.answer(text, reply_markup=reply_button)
    await state.reset_state(with_data=False)




@dp.callback_query_handler()
async def send_info(callback: types.CallbackQuery, state: FSMContext, message: types.message):
    data = await state.get_data()
    if callback.data == "ha":
        await bot.send_message(chat_id="")

    


def start_keyboard() -> types.ReplyKeyboardMarkup:
    """Create reply keyboard with main menu."""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        types.KeyboardButton("First Button "),
    )
    return keyboard




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True,on_startup=on_startup)