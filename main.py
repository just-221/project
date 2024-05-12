import os
import telebot
from telebot import types
from datetime import datetime


bot = telebot.TeleBot('6807174202:AAHW82gAbkwPxs59ZJ9XEGLV2GM8lGo_ADc')


user_responses = {}
questions = [
    ("🏢 Ish beruvchi", "⭐️ Ish beruvchi:\nTashkilot nomini kiriting. Tashkilot bo'lmasa ish beruvchining Ism Familiyasini yozing."),
    ("📋 Vakansiya nomi", "📋 Vakansiya nomi:\nVakansiya nomini kiriting, misol uchun:\n\n• Sotuv menejeri\n• Santexnika ustasi\n• Haydovchi"),
    ("💰 Ish haqi", "💰 Ish haqi:\nIsh haqi miqdori, valyutasi va davriyligini kiriting. Misol uchun:\n\n• 3.000.000 so'm - 1 oyga\n• 100 dollar - 1 ishga"),
    ("🌏 Manzil", "🌏 Manzil:\nIsh joyi manzilini kiriting. Misol uchun:\n\n• Toshkent shahar, Chilonzor tumani"),
    ("\n📑 Vakansiya haqida", "📑 Vakansiya haqida:\nVakansiya haqida qisqacha ma'lumot bering. Misol uchun, nima qilinishi kerakligi haqida yozing."),
    ("\n📞 Aloqa", "📞 Aloqa:\nBog'lanish uchun telefon raqam yoki elektron pochta manzilini kiriting. Misol uchun:\n\n• +998912345678\n• example@gmail.com"),
    ("🕰 Murojaat qilish vaqti", "🕰 Murojaat qilish vaqti:\nMurojaat qilish mumkin bo'lgan vaqtlarni kiriting. Misol uchun:\n\n• 9:00 - 18:00"),
    ("\n📌 Qo'shimcha ma'lumotlar", """📌 Qo'shimcha ma'lumotlar:\nQoshimcha ma'lumotlarni kiriting. Agarda ular yo'q bo'lsa "Qo'shimcha ma'lumotlar yo'q" tugmasini bosing.""")
]
num_questions = len(questions)


user_responses2 = {}
questions2 = [
    ("⭐️ Ish qidiruvchi", "⭐️ Ish qidiruvchi:\nIsh qidiruvchining Ism Familiyasini kiriting."),
    ("🗓 Tug'ilgan sana", "🗓 Tug'ilgan sana:\nIsh qidiruvchining tug'ilgan sanasini kiriting. Misol uchun:\n\n• 12.06.2000"),
    ("💠 Mutaxassislik", "💠 Mutaxassislik:\nIsh qidiruvchining mutaxassisligini kiriting. Misol uchun:\n\n• Sotuv menejeri\n• Santexnika ustasi\n• Haydovchi"),
    ("🌏 Manzil", "🌏 Manzil:\nIsh qidiruvchining manzilini kiriting. Misol uchun:\n\n• Toshkent shahar, Chilonzor tumani"),
    ("💰 Ish haqi", "💰 Ish haqi:\nIsh qidiruvchiga maqul ish haqini kiriting. Ish haqi miqdori, valyutasi va davriyligini yozing. Misol uchun:\n\n• 3.000.000 so'm - 1 oyga\n• 100 dollar - 1 ishga"),
    ("🧑‍🎓 Talaba", """🧑‍🎓 Talaba:\nIsh qidiruvchi talaba bo'lsa "Ha" tugmasini, aksincha bo'lsa "Yo'q" tugmasini bosing."""),
    ("📑 Ish qidiruvchi haqida", "📑 Ish qidiruvchi haqida:\nIsh qidiruvchi haqida qisqacha ma'lumot bering. Misol uchun, qanday bilim va qobiliyatlarga ega ekanligi haqida yozing."),
    ("📞 Aloqa", "📞 Aloqa:\nBog'lanish uchun telefon raqam yoki elektron pochta manzilini kiriting. Misol uchun:\n\n• +998912345678\n• example@gmail.com"),
    ("🕰 Murojaat qilish vaqti", "🕰 Murojaat qilish vaqti:\nMurojaat qilish mumkin bo'lgan vaqtlarni kiriting. Misol uchun:\n\n• 9:00 - 18:00"),
    ("📌 Qo'shimcha ma'lumotlar", """📌 Qo'shimcha ma'lumotlar:\nQoshimcha ma'lumotlarni kiriting. Agarda ular yo'q bo'lsa "Qo'shimcha ma'lumotlar yo'q" tugmasini bosing.""")
]
num_questions2 = len(questions2)


user_responses3 = {}
questions3 = [
    ("🧑🏻‍🏫 Ustoz", "🧑🏻‍🏫 Ustoz:\nUstozning Ism Familiyasini yozing."),
    ("📋 Ustozlik yo'nalishi", "📋 Ustozlik yo'nalishi:\nQanday yo'nalish bo'yicha shogirt olinsa, shu yo'nalishni kiriting, misol uchun:\n\n• IT yo'nalishi\n• Sotuv menejeri\n• Santexnika ustasi"),
    ("💰 Ish haqi", """💰 Ish haqi:\nIsh haqi yo'q bo'lsa "Yo'q" deb yozing. Ish haqi bor bo'lsa miqdori, valyutasi va davriyligini kiriting. Misol uchun:\n\n• Yo'q\n\n• 3.000.000 so'm - 1 oyga\n• 100 dollar - 1 ishga"""),
    ("🌏 Manzil", "🌏 Manzil:\nFaoliyat yuritish manzilini kiriting. Misol uchun:\n\n• Toshkent shahar, Chilonzor tumani"),
    ("📑 Ustozlik haqida", "📑 Ustozlik haqida:\nUstozlik haqida qisqacha ma'lumot bering. Misol uchun, nimalar qilinishi haqida yoki ustozlik davri qanday o'tishi haqida yozing."),
    ("📞 Aloqa", """📞 Aloqa:\nBog'lanish uchun telefon raqam yoki elektron pochta manzilini kiriting. Misol uchun:\n\n• +998912345678\n• example@gmail.com"""),
    ("🕰 Murojaat qilish vaqti:", "🕰 Murojaat qilish vaqti:\nMurojaat qilish mumkin bo'lgan vaqtlarni kiriting. Misol uchun:\n\n• 9:00 - 18:00"),
    ("📌 Qo'shimcha ma'lumotlar", """📌 Qo'shimcha ma'lumotlar:\nQoshimcha ma'lumotlarni kiriting. Agarda ular yo'q bo'lsa "Qo'shimcha ma'lumotlar yo'q" tugmasini bosing.""")
]
num_questions3 = len(questions3)


user_responses4 = {}
questions4 = [
    ("🧑🏻 Shogirt", "🧑🏻 Shogirt:\nShogirtning Ism Familiyasini kiriting."),
    ("🗓 Tug'ilgan sana", "🗓 Tug'ilgan sana:\nShogirtning tug'ilgan sanasini kiriting. Misol uchun:\n\n• 12.06.2005"),
    ("💠 Shogirtlik yo'nalishi", """💠 Shogirtlik yo'nalishi:\nQanday yo'nalish bo'yicha ustoz qidirilayotgan bo'lsa, shu yo'nalishni kiriting, misol uchun:\n\n• IT yo'nalishi\n• Sotuv menejeri\n• Santexnika ustasi"""),
    ("🌏 Manzil", "🌏 Manzil:\nQaysi manzil bo'yicha ustoz qidirilayotgan bo'lsa, shu manzilni kiriting, misol uchun:\n\n• Toshkent shahar, Chilonzor tumani"),
    ("💰 Ish haqi", """💰 Ish haqi:\nIsh haqi kerak bo'lmasa "Kerak emas" deb yozing. Ish haqi kerak bo'lsa miqdori, valyutasi va davriyligini kiriting. Misol uchun:\n\n• Yo'q\n\n• 3.000.000 so'm - 1 oyga\n• 100 dollar - 1 ishga"""),
    ("🧑‍🎓 Talaba", """🧑‍🎓 Talaba:\nShogirt talaba bo'lsa "Ha" tugmasini, aksincha bo'lsa "Yo'q" tugmasini bosing."""),
    ("📑 Shogirt haqida", "📑 Shogirt haqida:\nShogirt haqida qisqacha ma'lumot bering. Misol uchun, qanday bilim va qibiliyatlarga ega ekanligi haqida yozing."),
    ("📞 Aloqa", "📞 Aloqa:\nBog'lanish uchun telefon raqam yoki elektron pochta manzilini kiriting. Misol uchun:\n\n• +998912345678\n• example@gmail.com"),
    ("🕰 Murojaat qilish vaqti", "🕰 Murojaat qilish vaqti:\nMurojaat qilish mumkin bo'lgan vaqtlarni kiriting. Misol uchun:\n\n• 9:00 - 18:00"),
    ("📌 Qo'shimcha ma'lumotlar", """📌 Qo'shimcha ma'lumotlar:\nQoshimcha ma'lumotlarni kiriting. Agarda ular yo'q bo'lsa "Qo'shimcha ma'lumotlar yo'q" tugmasini bosing.""")
]
num_questions4 = len(questions4)

user_responses5 = {}
questions5 = [
    ("⭐️ Sherik", "⭐️ Sherik:\nSherikning Ism Familiyasini yozing."),
    ("📋 Sheriklik yo'nalishi", "📋 Sheriklik yo'nalishi:\nQanday yo'nalish bo'yicha sherik qidirilayotgan bo'lsa, shu yo'nalishni kiriting, misol uchun:\n\n• IT yo'nalishi\n• Savdo-sotiq yo'nalishi\n• Ishlab chiqarish yo'nalishi\n• Qimmatbaho toshlar yo'nalishi"),
    ("💰 Hisob-kitob", """💰 Hisob-kitob:\nHisob-kitob alohida muzokara qilinsa "Alohida muzokara qilinadi" deb yozing. Hisob-kitob e'lon qilinsa ma'lumotlarini kiriting. Misol uchun:\n\n• Alohida muzokara qilinadi\n\n• 50/50 ishlanadi\n• Har sotuvdan 20%"""),
    ("🌏 Manzil", "🌏 Manzil:\nQaysi manzil bo'yicha ustoz qidirilayotgan bo'lsa, shu manzilni kiriting, misol uchun:\n\n• Toshkent shahar, Chilonzor tumani"),
    ("📑 Sheriklik haqida", """📑 Sheriklik haqida:\nSheriklik haqida qisqacha ma'lumot bering. Misol uchun, nimalar qilinishi haqida yozing."""),
    ("📞 Aloqa", """📞 Aloqa:\nBog'lanish uchun telefon raqam yoki elektron pochta manzilini kiriting. Misol uchun:\n\n• +998912345678\n• example@gmail.com"""),
    ("🕰 Murojaat qilish vaqti", "🕰 Murojaat qilish vaqti:\nMurojaat qilish mumkin bo'lgan vaqtlarni kiriting. Misol uchun:\n\n• 9:00 - 18:00"),
    ("📌 Qo'shimcha ma'lumotlar", """📌 Qo'shimcha ma'lumotlar:\nQoshimcha ma'lumotlarni kiriting. Agarda ular yo'q bo'lsa "Qo'shimcha ma'lumotlar yo'q" tugmasini bosing.""")
]
num_questions5 = len(questions5)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton("🏢 Ish joylash", callback_data='Ish joylash')
    bt2 = types.InlineKeyboardButton("🧑🏻‍💼 Rezyume joylash", callback_data='Rezyume joylash')
    bt3 = types.InlineKeyboardButton("🧑🏻 Shogirt kerak", callback_data='Shogirt kerak')
    bt4 = types.InlineKeyboardButton("🧑🏻‍🏫 Ustoz kerak", callback_data='Ustoz kerak')
    bt5 = types.InlineKeyboardButton("🎗 Sherik kerak", callback_data='Sherik kerak')
    markup.row(bt1, bt2)
    markup.row(bt3, bt4)
    markup.row(bt5)
    bot.reply_to(message, f"""*Assalomu alaykum {message.from_user.first_name},"EFFECT | Katta mehnat bozori" @palonchi kanali uchun e'lon yaratuvchi botiga xush kelibsiz.*\n\n"EFFECT | Katta mehnat bozori" - ish izlayotgan odamlarga vakansiyalarni, ish beruvchilarga esa ishchilarni topishda yordam beradi. Qolaversa bir qator boshqa yo'nalishlarni ham qollab quvvatlaydi.\n\n*Yo'nalishlar:*\n• "🏢 Ish joylash" - ishchi topish uchun.\n• "🧑🏻‍💼 Rezyume joylash" - ish topish uchun.\n• "🧑🏻 Shogirt kerak" - shogirt topish uchun.\n• "🧑🏻‍🏫 Ustoz kerak" - ustoz topish uchun.\n• "🎗 Sherik kerak" - sherik topish uchun.• "🎗 Sherik kerak" - sherik topish uchun.\n\n*E'lon berish uchun yo'nalishni tanlang 👇*""", reply_markup=markup, parse_mode='Markdown')



@bot.callback_query_handler(func=lambda call: call.data in ['Ish joylash', 'Rezyume joylash', 'Shogirt kerak', 'Ustoz kerak', 'Sherik kerak', 'Ha', 'Ha2',"Yo'q", 'info', 'info2', 'No', 'Yes', 'confirm_manager'])
def callback_query(call):
    message = call.message
    chat_id = message.chat.id

    if call.data == "Ish joylash":
        start_process_job(message, call)
    elif call.data == "Rezyume joylash":
        start_process_resume(message, call)
    elif call.data == "Shogirt kerak":
        start_process_shogirt(message, call)
    elif call.data == "Ustoz kerak":
        start_process_ustoz(message, call)
    elif call.data == "Sherik kerak":
        start_process_sherik(message, call)
    elif call.data == "No":
        bot.send_message(message.chat.id, "❌ E'lon qabul qilinmadi.")
        send_no(message)
    elif call.data == 'Yes':
        send_yes(message)
    elif call.data == 'Ha2':
        handle_confirm(call)






    elif chat_id in user_responses:
        process_job(message, call)
    elif chat_id in user_responses2:
        process_resume(message, call)
    elif chat_id in user_responses3:
        process_shogirt(message, call)
    elif chat_id in user_responses4:
        process_ustoz(message, call)
    elif chat_id in user_responses5:
        process_sherik(message, call)



def send_no(message):
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton("🏢 Ish joylash", callback_data='Ish joylash')
    bt2 = types.InlineKeyboardButton("🧑🏻‍💼 Rezyume joylash", callback_data='Rezyume joylash')
    bt3 = types.InlineKeyboardButton("🧑🏻 Shogirt kerak", callback_data='Shogirt kerak')
    bt4 = types.InlineKeyboardButton("🧑🏻‍🏫 Ustoz kerak", callback_data='Ustoz kerak')
    bt5 = types.InlineKeyboardButton("🎗 Sherik kerak", callback_data='?????????????')
    markup.row(bt1, bt2)
    markup.row(bt3, bt4)
    markup.row(bt5)
    bot.reply_to(message, f"""*Yo'nalishlar:*\n\n• "🏢 Ish joylash" - ishchi topish uchun.\n• "🧑🏻‍💼 Rezyume joylash" - ish topish uchun.\n• "🧑🏻 Shogirt kerak" - shogirt topish uchun.\n• "🧑🏻‍🏫 Ustoz kerak" - ustoz topish uchun.\n• "🎗 Sherik kerak" - sherik topish uchun.\n\n*Yangi e'lon berish uchun yo'nalishni tanlang 👇*""", reply_markup=markup, parse_mode='Markdown')

def send_yes(message):
    markup = types.InlineKeyboardMarkup()
    bt6 = types.InlineKeyboardButton("✅ E'lonni joylash", callback_data='Ha2')
    bt7 = types.InlineKeyboardButton("❌ Bekor qilish", callback_data='No')
    markup.row(bt6, bt7)
    bot.reply_to(message, f"""E'lonni joylash narxi: "BEPUL 🕑"\n\nℹ️ E'lon joylashtirilgandan so'ng, u moderatorlar tomonidan ko'rib chiqiladi. Zaruriyat tug'ilganda, ma'lumotlar to'g'riligini tekshirish maqsadida e'lon muallifi bilan bog'laniladi.\n\nTayyor e'lonni "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylash uchun "E'lonni joylash" tugmasini bosing, bekor qilish uchun "Bekor qilish" tugmasini bosing 👇""", reply_markup=markup, parse_mode='Markdown')

def handle_confirm(call):
    message = call.message
    chat_id = call.message.chat.id
    if chat_id in user_responses and user_responses[chat_id]:
        username = call.from_user.username
        summary_text = format_summary(user_responses.pop(chat_id), username)
        group_chat_id(summary_text)
        bot.answer_callback_query(call.id, "Ma'lumotlar yuborildi!")
        bot.send_message(chat_id, """✅ Sizning e'loningiz "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtirildi.\n\nBizning xizmatimizdan foydalanganingiz uchun hursandmiz, ishlaringizga rivoj tilaymiz ⭐️""")
        send_no(message)

    elif chat_id in user_responses2 and user_responses2[chat_id]:
        username = call.from_user.username
        summary_text = format_summary2(user_responses2.pop(chat_id), username)
        group_chat_id(summary_text)
        bot.answer_callback_query(call.id, "Ma'lumotlar yuborildi!")
        bot.send_message(chat_id, """✅ Sizning e'loningiz "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtirildi.\n\nBizning xizmatimizdan foydalanganingiz uchun hursandmiz, ishlaringizga rivoj tilaymiz ⭐️""")
        send_no(message)

    elif chat_id in user_responses3 and user_responses3[chat_id]:
        username = call.from_user.username
        summary_text = format_summary3(user_responses3.pop(chat_id), username)
        group_chat_id(summary_text)
        bot.answer_callback_query(call.id, "Ma'lumotlar yuborildi!")
        bot.send_message(chat_id, """✅ Sizning e'loningiz "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtirildi.\n\nBizning xizmatimizdan foydalanganingiz uchun hursandmiz, ishlaringizga rivoj tilaymiz ⭐️""")
        send_no(message)

    elif chat_id in user_responses4 and user_responses4[chat_id]:
        username = call.from_user.username
        summary_text = format_summary4(user_responses4.pop(chat_id), username)
        group_chat_id(summary_text)
        bot.answer_callback_query(call.id, "Ma'lumotlar yuborildi!")
        bot.send_message(chat_id, """✅ Sizning e'loningiz "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtirildi.\n\nBizning xizmatimizdan foydalanganingiz uchun hursandmiz, ishlaringizga rivoj tilaymiz ⭐️""")
        send_no(message)

    elif chat_id in user_responses5 and user_responses5[chat_id]:
        username = call.from_user.username
        summary_text = format_summary5(user_responses5.pop(chat_id), username)
        group_chat_id(summary_text)
        bot.answer_callback_query(call.id, "Ma'lumotlar yuborildi!")
        bot.send_message(chat_id, """✅ Sizning e'loningiz "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtirildi.\n\nBizning xizmatimizdan foydalanganingiz uchun hursandmiz, ishlaringizga rivoj tilaymiz ⭐️""")
        send_no(message)

    else:
        bot.answer_callback_query(call.id, "Sizning ma'lumotlaringiz to'pilmadi!")

def group_chat_id(summary_text):
    group_chat_id = '-1002133496353'
    bot.send_message(group_chat_id, summary_text)







def format_summary(user_data, username):
    if not user_data:
        return "No data provided"
    response_text = "🏢 ISH\n\n"
    response_text += f"⭐️ Ish beruvchi: {user_data[0]}\n"
    response_text += f"📋 Vakansiya nomi: {user_data[1]}\n"
    response_text += f"💰 Ish haqi: {user_data[2]}\n"
    response_text += f"🌏 Manzil: {user_data[3]}\n\n"
    response_text += f"📑 Vakansiya haqida: {user_data[4]}\n\n"
    response_text += f"📞 Aloqa: {user_data[5]}\n"
    response_text += f"✉️ Telegram: @{username}\n"
    response_text += f"🕰 Murojaat qilish vaqti: {user_data[6]}\n\n"
    response_text += f"📌 Qo'shimcha ma'lumotlar: {user_data[7]}\n\n"
    response_text += "#Ish\n\n"
    response_text += "🌐  EFFECT | Katta mehnat bozori kanaliga obuna bo'lish (https://t.me/test_bot1567)"
    return response_text

def format_summary2(user_data, username):
    if not user_data:
        return "No data provided"
    response_text = "REZYUME 🧑🏻‍💼\n\n"
    response_text += f"⭐️ Ish qidiruvchi: {user_data[0]}\n"
    response_text += f"🗓 Tug'ilgan sana: {user_data[1]}\n"
    response_text += f"💠 Mutaxassislik: {user_data[2]}\n"
    response_text += f"🌏 Manzil: {user_data[3]}\n"
    response_text += f"💰 Ish haqi: {user_data[4]}\n\n"
    response_text += f"🧑‍🎓 Talaba: {user_data[5]}\n"
    response_text += f"📑 Ish qidiruvchi haqida: {user_data[6]}\n\n"
    response_text += f"📞 Aloqa: {user_data[7]}\n"
    response_text += f"✉️ Telegram: @{username}\n"
    response_text += f"🕰 Murojaat qilish vaqti: {user_data[8]}\n\n"
    response_text += f"📌 Qo'shimcha ma'lumotlar: {user_data[9]}\n\n"
    response_text += "#Rezyume\n\n"
    response_text += "🌐 EFFECT | Katta mehnat bozori kanaliga obuna bo'lish (https://t.me/test_bot1567)"
    return response_text

def format_summary3(user_data, username):
    if not user_data:
        return "No data provided"
    response_text = "SHOGIRT KERAK 🧑🏻\n\n"
    response_text += f"🧑🏻‍🏫 Ustoz: {user_data[0]}\n"
    response_text += f"📋 Ustozlik yo'nalishi: {user_data[1]}\n"
    response_text += f"💰 Ish haqi: {user_data[2]}\n"
    response_text += f"🌏 Manzil: {user_data[3]}\n\n"
    response_text += f"📑 Ustozlik haqida: {user_data[4]}\n\n"
    response_text += f"📞 Aloqa: {user_data[5]}\n"
    response_text += f"✉️ Telegram: @{username}\n"
    response_text += f"🕰 Murojaat qilish vaqti: {user_data[6]}\n\n"
    response_text += f"📌 Qo'shimcha ma'lumotlar: {user_data[7]}\n\n"
    response_text += "#ShogirtKerak\n\n"
    response_text += "🌐 EFFECT | Katta mehnat bozori kanaliga obuna bo'lish (https://t.me/test_bot1567)"
    return response_text

def format_summary4(user_data, username):
    if not user_data:
        return "No data provided"
    response_text = "USTOZ KERAK 🧑🏻‍🏫\n\n"
    response_text += f"🧑🏻 Shogirt: {user_data[0]}\n"
    response_text += f"🗓 Tug'ilgan sana: {user_data[1]}\n"
    response_text += f"💠 Shogirtlik yo'nalishi: {user_data[2]}\n"
    response_text += f"🌏 Manzil: {user_data[3]}\n"
    response_text += f"💰 Ish haqi: {user_data[4]}\n\n"
    response_text += f"🧑‍🎓 Talaba: {user_data[5]}\n"
    response_text += f"📑 Shogirt haqida: {user_data[6]}\n\n"
    response_text += f"📞 Aloqa: {user_data[7]}\n"
    response_text += f"✉️ Telegram: @{username}\n"
    response_text += f"🕰 Murojaat qilish vaqti: {user_data[8]}\n\n"
    response_text += f"📌 Qo'shimcha ma'lumotlar: {user_data[9]}\n\n"
    response_text += "#UstozKerak\n\n"
    response_text += "🌐 EFFECT | Katta mehnat bozori kanaliga obuna bo'lish (https://t.me/test_bot1567)"
    return response_text

def format_summary5(user_data, username):
    if not user_data:
        return "No data provided"
    response_text = "🎗 SHERIK KERAK\n\n"
    response_text += f"⭐️ Sherik: {user_data[0]}\n"
    response_text += f"📋 Sheriklik yo'nalishi: {user_data[1]}\n"
    response_text += f"💰 Hisob-kitob: {user_data[2]}\n"
    response_text += f"🌏 Manzil: {user_data[3]}\n"
    response_text += f"📑 Sheriklik haqida: {user_data[4]}\n\n"
    response_text += f"📞 Aloqa: {user_data[5]}\n"
    response_text += f"✉️ Telegram: @{username}\n"
    response_text += f"🕰 Murojaat qilish vaqti: {user_data[6]}\n\n"
    response_text += f"📌 Qo'shimcha ma'lumotlar: {user_data[7]}\n\n"
    response_text += "#SherikKerak\n\n"
    response_text += "🌐 EFFECT | Katta mehnat bozori kanaliga obuna bo'lish (https://t.me/test_bot1567)"
    return response_text




def start_process_job(message, call):
    chat_id = message.chat.id
    user_responses[chat_id] = []
    text = """*🏢 ISH\n\nIsh joylashtirish uchun bir nechta savollarga javob bering. Har bir javobingiz to'g'ri va ishonchli ma'lumotlardan iborat bo'lishi kerak ekanligiga e'tiborli bo'ling.\n\nSo'rovnoma yakunida, agarda kiritilgan barcha ma'lumotlar to'g'ri bo'lsa "✅ To'g'ri" tugmasini bosing, aksincha bo'lsa "❌ Noto'g'ri" tugmasini bosing va so'rovnomani qaytadan to'ldiring.\n\nE'lon tayor bo'lgandan kegin "E'lonni joylash" tugmasi bosilsa e'lon o'sha zaxotiyoq "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtiriladi.*"""
    bot.reply_to(message, text, parse_mode='Markdown')
    ask_question(message, 0)

def start_process_resume(message, call):
    chat_id = message.chat.id
    text = """*🧑🏻‍💼 REZYUME*\n\nRezyume joylashtirish uchun bir nechta savollarga javob bering. Har bir javobingiz to'g'ri va ishonchli ma'lumotlardan iborat bo'lishi kerak ekanligiga e'tiborli bo'ling.\n\nSo'rovnoma yakunida, agarda kiritilgan barcha ma'lumotlar to'g'ri bo'lsa "✅ To'g'ri" tugmasini bosing, aksincha bo'lsa "❌ Noto'g'ri" tugmasini bosing va so'rovnomani qaytadan to'ldiring.\n\nE'lon tayor bo'lgandan kegin "E'lonni joylash" tugmasi bosilsa e'lon o'sha zaxotiyoq "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtiriladi."""
    bot.reply_to(message, text, parse_mode='Markdown')
    user_responses2[chat_id] = []
    ask_question1(message, 0)

def start_process_shogirt(message, call):
    chat_id = message.chat.id
    text = """*🧑🏻 SHOGIRT KERAK\n\nShogirt kerakligi haqida e'lon joylashtirish uchun bir nechta savollarga javob bering. Har bir javobingiz to'g'ri va ishonchli ma'lumotlardan iborat bo'lishi kerak ekanligiga e'tiborli bo'ling.\n\nSo'rovnoma yakunida, agarda kiritilgan barcha ma'lumotlar to'g'ri bo'lsa "✅ To'g'ri" tugmasini bosing, aksincha bo'lsa "❌ Noto'g'ri" tugmasini bosing va so'rovnomani qaytadan to'ldiring.\n\nE'lon tayor bo'lgandan kegin "E'lonni joylash" tugmasi bosilsa e'lon o'sha zaxotiyoq "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtiriladi.*"""
    bot.reply_to(message, text, parse_mode='Markdown')
    user_responses3[chat_id] = []
    ask_question2(message, 0)

def start_process_ustoz(message, call):
    chat_id = message.chat.id
    text = """*🧑🏻‍🏫 USTOZ KERAK*\n\nUstoz kerakligi haqida e'lon joylashtirish uchun bir nechta savollarga javob bering. Har bir javobingiz to'g'ri va ishonchli ma'lumotlardan iborat bo'lishi kerak ekanligiga e'tiborli bo'ling.\n\nSo'rovnoma yakunida, agarda kiritilgan barcha ma'lumotlar to'g'ri bo'lsa "✅ To'g'ri" tugmasini bosing, aksincha bo'lsa "❌ Noto'g'ri" tugmasini bosing va so'rovnomani qaytadan to'ldiring.\n\nE'lon tayor bo'lgandan kegin "E'lonni joylash" tugmasi bosilsa e'lon o'sha zaxotiyoq "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtiriladi."""
    bot.reply_to(message, text, parse_mode='Markdown')
    user_responses4[chat_id] = []
    ask_question3(message, 0)

def start_process_sherik(message, call):
    chat_id = message.chat.id
    text = """*🎗 SHERIK KERAK*\n\nSherik kerakligi haqida e'lon joylashtirish uchun bir nechta savollarga javob bering. Har bir javobingiz to'g'ri va ishonchli ma'lumotlardan iborat bo'lishi kerak ekanligiga e'tiborli bo'ling.\n\nSo'rovnoma yakunida, agarda kiritilgan barcha ma'lumotlar to'g'ri bo'lsa "✅ To'g'ri" tugmasini bosing, aksincha bo'lsa "❌ Noto'g'ri" tugmasini bosing va so'rovnomani qaytadan to'ldiring.\n\nE'lon tayor bo'lgandan kegin "E'lonni joylash" tugmasi bosilsa e'lon o'sha zaxotiyoq "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtiriladi."""
    bot.reply_to(message, text, parse_mode='Markdown')
    user_responses5[chat_id] = []
    ask_question4(message, 0)




def process_job(message, call):
    chat_id = message.chat.id
    user_data = user_responses.get(chat_id, [])
    question_index = len(user_data)

    if call.data in ['info']:
        user_data.append(call.data if call.data != 'info' else "Yo'q")
        question_index += 1

    if question_index >= num_questions:
        send_summary0(message, user_data, call.from_user.username)
    else:
        ask_question(message, question_index)

def process_resume(message, call):
    chat_id = message.chat.id
    user_data = user_responses2.get(chat_id, [])
    question_index = len(user_data)

    if call.data in ['Ha', "Yo'q", 'info2']:
        user_responses2[message.chat.id].append(call.data if call.data != 'info2' else "Yo'q")
        question_index += 1

    if question_index >= num_questions2:
        send_summary(message, user_data, call.from_user.username)
    else:
        ask_question1(message, question_index)

def process_shogirt(message, call):
    chat_id = message.chat.id
    user_data = user_responses3.get(chat_id, [])
    question_index = len(user_data)

    if call.data in ['info']:
        user_responses3[message.chat.id].append(call.data if call.data != 'info' else "Yo'q")
        question_index += 1

    if question_index >= num_questions3:
        send_summary1(message, user_data, call.from_user.username)
    else:
        ask_question2(message, question_index)

def process_ustoz(message, call):
    chat_id = message.chat.id
    user_data = user_responses4.get(chat_id, [])
    question_index = len(user_data)

    if call.data in ['Ha', "Yo'q", 'info']:
        user_responses4[message.chat.id].append(call.data if call.data != 'info' else "Yo'q")
        question_index += 1

    if question_index >= num_questions4:
        send_summary2(message, user_data, call.from_user.username)
    else:
        ask_question3(message, question_index)

def process_sherik(message, call):
    chat_id = message.chat.id
    user_data = user_responses5.get(chat_id, [])
    question_index = len(user_data)

    if call.data in ['info']:
        user_responses5[message.chat.id].append(call.data if call.data != 'info' else "Yo'q")
        question_index += 1

    if question_index >= num_questions5:
        send_summary3(message, user_data, call.from_user.username)
    else:
        ask_question4(message, question_index)






def ask_question(message, question_index):
    if question_index < num_questions:
        question_text = questions[question_index][1]
        question_text = apply_formatting(question_text)
        markup = types.InlineKeyboardMarkup()
        if question_index == 7:
            markup.add(types.InlineKeyboardButton("Qo'shimcha ma'lumotlar yo'q", callback_data='info'))
        else:
            markup = None

        msg = bot.send_message(message.chat.id, question_text, reply_markup=markup, parse_mode='Markdown')
        bot.register_next_step_handler(msg, handle_answer1, question_index)
    else:
        all_answers = user_responses[message.chat.id]
        send_summary0(message, all_answers, message.from_user.username)

def handle_answer1(message, question_index):
    user_responses[message.chat.id].append(message.text)
    ask_question(message, question_index + 1)

def send_summary0(message, answers, username):
    chat_id = message.chat.id
    response_text = format_summary(answers, username)
    bot.send_message(chat_id, response_text)


    mess = "*Barcha ma'lumotlar to'g'rimi?*"
    markup = types.InlineKeyboardMarkup()
    btn_confirm = types.InlineKeyboardButton("✅ To'g'ri", callback_data='Yes')
    btn_edit = types.InlineKeyboardButton("❌ Noto'g'ri", callback_data='No')
    markup.add(btn_confirm, btn_edit)

    bot.send_message(chat_id, mess, reply_markup=markup, parse_mode='Markdown')

def apply_formatting(text):
    formatted_text = text.replace('⭐️ Ish beruvchi:', '*⭐️ Ish beruvchi:*')
    formatted_text = formatted_text.replace("📋 Vakansiya nomi:", "*📋 Vakansiya nomi:*")
    formatted_text = formatted_text.replace('• Sotuv menejeri', '_• Sotuv menejeri_')
    formatted_text = formatted_text.replace('• Santexnika ustasi', '_• Santexnika ustasi_')
    formatted_text = formatted_text.replace('• Haydovchi', '_• Haydovchi_')
    formatted_text = formatted_text.replace('💰 Ish haqi:', '*💰 Ish haqi:*')
    formatted_text = formatted_text.replace("• 3.000.000 so'm - 1 oyga", "_• 3.000.000 so'm - 1 oyga_")
    formatted_text = formatted_text.replace('• 100 dollar - 1 ishga', '_• 100 dollar - 1 ishga_')
    formatted_text = formatted_text.replace('🌏 Manzil:', '*🌏 Manzil:*')
    formatted_text = formatted_text.replace('• Toshkent shahar, Chilonzor tumani', '_• Toshkent shahar, Chilonzor tumani_')
    formatted_text = formatted_text.replace('📑 Vakansiya haqida:', '*📑 Vakansiya haqida:*')
    formatted_text = formatted_text.replace('📞 Aloqa:', '*📞 Aloqa:*')
    formatted_text = formatted_text.replace('• +998912345678', '_• +998912345678_')
    formatted_text = formatted_text.replace('• example@gmail.com', '_• example@gmail.com_')
    formatted_text = formatted_text.replace('🕰 Murojaat qilish vaqti:', '*🕰 Murojaat qilish vaqti:*')
    formatted_text = formatted_text.replace('• 9:00 - 18:00', '_• 9:00 - 18:00_')
    formatted_text = formatted_text.replace("📌 Qo'shimcha ma'lumotlar:", "*📌 Qo'shimcha ma'lumotlar:*")
    return formatted_text




def ask_question1(message, question_index):
    if question_index < num_questions2:
        question_text = questions2[question_index][1]
        question_text = apply_formatting1(question_text)
        markup = types.InlineKeyboardMarkup()
        if question_index == 5:
            markup.add(types.InlineKeyboardButton("Ha", callback_data='Ha'),
                       types.InlineKeyboardButton("Yo'q", callback_data="Yo'q"))
        elif question_index == 9:
            markup.add(types.InlineKeyboardButton("Qo'shimcha ma'lumotlar yo'q", callback_data='info2'))
        else:
            markup = None

        msg = bot.send_message(message.chat.id, question_text, reply_markup=markup, parse_mode='Markdown')
        if markup is None or question_index == 9:
            bot.register_next_step_handler(msg, handle_answer2, question_index)
    else:
        all_answers = user_responses2[message.chat.id]
        send_summary(message, all_answers, message.from_user.username)

def handle_answer2(message, question_index):
    chat_id = message.chat.id
    if chat_id not in user_responses2:
        user_responses2[chat_id] = []
    user_responses2[chat_id].append(message.text)
    ask_question1(message, question_index + 1)

def send_summary(message, answers, username):
    chat_id = message.chat.id
    response_text = format_summary2(answers, username)
    bot.send_message(chat_id, response_text)

    mess = "*Barcha ma'lumotlar to'g'rimi?*"
    markup = types.InlineKeyboardMarkup()
    btn_confirm = types.InlineKeyboardButton("✅ To'g'ri", callback_data='Yes')
    btn_edit = types.InlineKeyboardButton("❌ Noto'g'ri", callback_data='No')
    markup.add(btn_confirm, btn_edit)

    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='Markdown')

def apply_formatting1(text):
    formatted_text = text.replace('⭐️ Ish qidiruvchi:', '*⭐️ Ish qidiruvchi:*')
    formatted_text = formatted_text.replace("🗓 Tug'ilgan sana:", "*🗓 Tug'ilgan sana:*")
    formatted_text = formatted_text.replace('• 12.06.2000', '_• 12.06.2000_')
    formatted_text = formatted_text.replace('• Sotuv menejeri', '_• Sotuv menejeri_')
    formatted_text = formatted_text.replace('• Santexnika ustasi', '_• Santexnika ustasi_')
    formatted_text = formatted_text.replace('• Haydovchi', '_• Haydovchi_')
    formatted_text = formatted_text.replace('💠 Mutaxassislik:', '*💠 Mutaxassislik:*')
    formatted_text = formatted_text.replace('💰 Ish haqi:', '*💰 Ish haqi:*')
    formatted_text = formatted_text.replace("• 3.000.000 so'm - 1 oyga", "_• 3.000.000 so'm - 1 oyga_")
    formatted_text = formatted_text.replace('• 100 dollar - 1 ishga', '_• 100 dollar - 1 ishga_')
    formatted_text = formatted_text.replace('🌏 Manzil:', '*🌏 Manzil:*')
    formatted_text = formatted_text.replace('• Toshkent shahar, Chilonzor tumani', '_• Toshkent shahar, Chilonzor tumani_')
    formatted_text = formatted_text.replace('🧑‍🎓 Talaba:', '*🧑‍🎓 Talaba:*')
    formatted_text = formatted_text.replace('📑 Ish qidiruvchi haqida:', '*📑 Ish qidiruvchi haqida:*')
    formatted_text = formatted_text.replace('📞 Aloqa:', '*📞 Aloqa:*')
    formatted_text = formatted_text.replace('• +998912345678', '_• +998912345678_')
    formatted_text = formatted_text.replace('• example@gmail.com', '_• example@gmail.com_')
    formatted_text = formatted_text.replace('🕰 Murojaat qilish vaqti:', '*🕰 Murojaat qilish vaqti:*')
    formatted_text = formatted_text.replace('• 9:00 - 18:00', '_• 9:00 - 18:00_')
    formatted_text = formatted_text.replace("📌 Qo'shimcha ma'lumotlar:", "*📌 Qo'shimcha ma'lumotlar:*")
    return formatted_text



def ask_question2(message, question_index):
    if question_index < num_questions3:
        question_text = questions3[question_index][1]
        question_text = apply_formatting2(question_text)
        markup = types.InlineKeyboardMarkup()
        if question_index == 7:
            markup.add(types.InlineKeyboardButton("Qo'shimcha ma'lumotlar yo'q", callback_data='info'))
        else:
            markup = None

        msg = bot.send_message(message.chat.id, question_text, reply_markup=markup, parse_mode='Markdown')
        bot.register_next_step_handler(msg, handle_answer3, question_index)
    else:
        all_answers = user_responses3[message.chat.id]
        send_summary1(message, all_answers, message.from_user.username)

def handle_answer3(message, question_index):
    chat_id = message.chat.id
    if chat_id not in user_responses3:
        user_responses3[chat_id] = []
    user_responses3[chat_id].append(message.text)
    ask_question2(message, question_index + 1)

def send_summary1(message, answers, username):
    chat_id = message.chat.id
    response_text = format_summary3(answers, username)
    bot.send_message(chat_id, response_text)

    mess = "*Barcha ma'lumotlar to'g'rimi?*"
    markup = types.InlineKeyboardMarkup()
    btn_confirm = types.InlineKeyboardButton("✅ To'g'ri", callback_data='Yes')
    btn_edit = types.InlineKeyboardButton("❌ Noto'g'ri", callback_data='No')
    markup.add(btn_confirm, btn_edit)

    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='Markdown')

def apply_formatting2(text):
    formatted_text = text.replace('🧑🏻‍🏫 Ustoz:', '*🧑🏻‍🏫 Ustoz:*')
    formatted_text = formatted_text.replace("📋 Ustozlik yo'nalishi:", "*📋 Ustozlik yo'nalishi:*")
    formatted_text = formatted_text.replace("• IT yo'nalishi", "_• IT yo'nalishi_")
    formatted_text = formatted_text.replace('• Sotuv menejeri', '_• Sotuv menejeri_')
    formatted_text = formatted_text.replace('• Santexnika ustasi', '_• Santexnika ustasi_')
    formatted_text = formatted_text.replace('💰 Ish haqi:', '*💰 Ish haqi:*')
    formatted_text = formatted_text.replace("• Yo'q", "_• Yo'q_")
    formatted_text = formatted_text.replace("• 3.000.000 so'm - 1 oyga", "_• 3.000.000 so'm - 1 oyga_")
    formatted_text = formatted_text.replace('• 100 dollar - 1 ishga', '_• 100 dollar - 1 ishga_')
    formatted_text = formatted_text.replace('🌏 Manzil:', '*🌏 Manzil:*')
    formatted_text = formatted_text.replace('• Toshkent shahar, Chilonzor tumani', '_• Toshkent shahar, Chilonzor tumani_')
    formatted_text = formatted_text.replace('📑 Ustozlik haqida:', '*📑 Ustozlik haqida:*')
    formatted_text = formatted_text.replace('📞 Aloqa:', '*📞 Aloqa:*')
    formatted_text = formatted_text.replace('• +998912345678', '_• +998912345678_')
    formatted_text = formatted_text.replace('• example@gmail.com', '_• example@gmail.com_')
    formatted_text = formatted_text.replace('🕰 Murojaat qilish vaqti:', '*🕰 Murojaat qilish vaqti:*')
    formatted_text = formatted_text.replace('• 9:00 - 18:00', '_• 9:00 - 18:00_')
    formatted_text = formatted_text.replace("📌 Qo'shimcha ma'lumotlar:", "*📌 Qo'shimcha ma'lumotlar:*")
    return formatted_text



def ask_question3(message, question_index):
    if question_index < num_questions4:
        question_text = questions4[question_index][1]
        question_text = apply_formatting3(question_text)
        markup = types.InlineKeyboardMarkup()
        if question_index == 5:
            markup.add(types.InlineKeyboardButton("Ha", callback_data='Ha'),
                       types.InlineKeyboardButton("Yo'q", callback_data="Yo'q"))
        elif question_index == 9:
            markup.add(types.InlineKeyboardButton("Qo'shimcha ma'lumotlar yo'q", callback_data='info'))
        else:
            markup = None

        msg = bot.send_message(message.chat.id, question_text, reply_markup=markup, parse_mode='Markdown')
        if markup is None or question_index == 9:
            bot.register_next_step_handler(msg, handle_answer4, question_index)
    else:
        all_answers = user_responses4[message.chat.id]
        send_summary2(message, all_answers, message.from_user.username)

def handle_answer4(message, question_index):
    chat_id = message.chat.id
    if chat_id not in user_responses4:
        user_responses4[chat_id] = []
    user_responses4[chat_id].append(message.text)
    ask_question3(message, question_index + 1)

def send_summary2(message, answers, username):
    chat_id = message.chat.id
    response_text = format_summary4(answers, username)
    bot.send_message(chat_id, response_text)

    mess = "*Barcha ma'lumotlar to'g'rimi?*"
    markup = types.InlineKeyboardMarkup()
    btn_confirm = types.InlineKeyboardButton("✅ To'g'ri", callback_data='Yes')
    btn_edit = types.InlineKeyboardButton("❌ Noto'g'ri", callback_data='No')
    markup.add(btn_confirm, btn_edit)

    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='Markdown')

def apply_formatting3(text):
    formatted_text = text.replace('🧑🏻 Shogirt:', '*🧑🏻 Shogirt:*')
    formatted_text = formatted_text.replace("🗓 Tug'ilgan sana:", "*🗓 Tug'ilgan sana:*")
    formatted_text = formatted_text.replace("• 12.06.2005", "_• 12.06.2005_")
    formatted_text = formatted_text.replace("💠 Shogirtlik yo'nalishi:", "*💠 Shogirtlik yo'nalishi:*")
    formatted_text = formatted_text.replace("• IT yo'nalishi", "_• IT yo'nalishi_")
    formatted_text = formatted_text.replace('• Sotuv menejeri', '_• Sotuv menejeri_')
    formatted_text = formatted_text.replace('• Santexnika ustasi', '_• Santexnika ustasi_')
    formatted_text = formatted_text.replace('💰 Ish haqi:', '*💰 Ish haqi:*')
    formatted_text = formatted_text.replace("• Yo'q", "_• Yo'q_")
    formatted_text = formatted_text.replace("• 3.000.000 so'm - 1 oyga", "_• 3.000.000 so'm - 1 oyga_")
    formatted_text = formatted_text.replace('• 100 dollar - 1 ishga', '_• 100 dollar - 1 ishga_')
    formatted_text = formatted_text.replace('🌏 Manzil:', '*🌏 Manzil:*')
    formatted_text = formatted_text.replace('Toshkent shahar, Chilonzor tumani', '_Toshkent shahar, Chilonzor tumani_')
    formatted_text = formatted_text.replace('🧑‍🎓 Talaba:', '*🧑‍🎓 Talaba:*')
    formatted_text = formatted_text.replace('📑 Shogirt haqida: ', '*📑 Shogirt haqida:*')
    formatted_text = formatted_text.replace('📞 Aloqa:', '*📞 Aloqa:*')
    formatted_text = formatted_text.replace('• +998912345678', '_• +998912345678_')
    formatted_text = formatted_text.replace('• example@gmail.com', '_• example@gmail.com_')
    formatted_text = formatted_text.replace('🕰 Murojaat qilish vaqti:', '*🕰 Murojaat qilish vaqti:*')
    formatted_text = formatted_text.replace('• 9:00 - 18:00', '_• 9:00 - 18:00_')
    formatted_text = formatted_text.replace("📌 Qo'shimcha ma'lumotlar:", "*📌 Qo'shimcha ma'lumotlar:*")
    return formatted_text



def ask_question4(message, question_index):
    if question_index < num_questions5:
        question_text = questions5[question_index][1]
        question_text = apply_formatting4(question_text)
        markup = types.InlineKeyboardMarkup()
        if question_index == 7:
            markup.add(types.InlineKeyboardButton("Qo'shimcha ma'lumotlar yo'q", callback_data='info'))
        else:
            markup = None

        msg = bot.send_message(message.chat.id, question_text, reply_markup=markup, parse_mode='Markdown')
        bot.register_next_step_handler(msg, handle_answer5, question_index)
    else:
        all_answers = user_responses5[message.chat.id]
        send_summary3(message, all_answers, message.from_user.username)

def handle_answer5(message, question_index):
    chat_id = message.chat.id
    if chat_id not in user_responses5:
        user_responses5[chat_id] = []
    user_responses5[chat_id].append(message.text)
    ask_question4(message, question_index + 1)

def send_summary3(message, answers, username):
    chat_id = message.chat.id
    response_text = format_summary5(answers, username)
    bot.send_message(chat_id, response_text)

    mess = "*Barcha ma'lumotlar to'g'rimi?*"
    markup = types.InlineKeyboardMarkup()
    btn_confirm = types.InlineKeyboardButton("✅ To'g'ri", callback_data='Yes')
    btn_edit = types.InlineKeyboardButton("❌ Noto'g'ri", callback_data='No')
    markup.add(btn_confirm, btn_edit)

    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='Markdown')

def apply_formatting4(text):
    formatted_text = text.replace('⭐️ Sherik:', '*⭐️ Sherik:*')
    formatted_text = formatted_text.replace("📋 Sheriklik yo'nalishi:", "*📋 Sheriklik yo'nalishi:*")
    formatted_text = formatted_text.replace("• IT yo'nalishi", "_• IT yo'nalishi_")
    formatted_text = formatted_text.replace("• Savdo-sotiq yo'nalishi", "_• Savdo-sotiq yo'nalishi_")
    formatted_text = formatted_text.replace("• Ishlab chiqarish yo'nalishi", "_• Ishlab chiqarish yo'nalishi_")
    formatted_text = formatted_text.replace("• Qimmatbaho toshlar yo'nalishi", "_• Qimmatbaho toshlar yo'nalishi_")
    formatted_text = formatted_text.replace('💰 Hisob-kitob:', '*💰 Hisob-kitob:*')
    formatted_text = formatted_text.replace('• Alohida muzokara qilinadi', '_• Alohida muzokara qilinadi_')
    formatted_text = formatted_text.replace('• 50/50 ishlanadi', '_• 50/50 ishlanadi_')
    formatted_text = formatted_text.replace('• Har', '_• Har_')
    formatted_text = formatted_text.replace('20%', '_20%_')
    formatted_text = formatted_text.replace('🌏 Manzil:', '*🌏 Manzil:*')
    formatted_text = formatted_text.replace('• Toshkent shahar, Chilonzor tumani', '_• Toshkent shahar, Chilonzor tumani_')
    formatted_text = formatted_text.replace('📑 Sheriklik haqida:', '*📑 Sheriklik haqida:*')
    formatted_text = formatted_text.replace('📞 Aloqa:', '*📞 Aloqa:*')
    formatted_text = formatted_text.replace('• +998912345678', '_• +998912345678_')
    formatted_text = formatted_text.replace('• example@gmail.com', '_• example@gmail.com_')
    formatted_text = formatted_text.replace('🕰 Murojaat qilish vaqti:', '*🕰 Murojaat qilish vaqti:*')
    formatted_text = formatted_text.replace('• 9:00 - 18:00', '_• 9:00 - 18:00_')
    formatted_text = formatted_text.replace("📌 Qo'shimcha ma'lumotlar:", "*📌 Qo'shimcha ma'lumotlar:*")
    return formatted_text


bot.polling(none_stop=True)





'''
Full code:
import os
import telebot
from telebot import types
from datetime import datetime


bot = telebot.TeleBot('6807174202:AAHW82gAbkwPxs59ZJ9XEGLV2GM8lGo_ADc')


user_responses = {}
questions = [
    ("🏢 Ish beruvchi", "⭐️ Ish beruvchi:\nTashkilot nomini kiriting. Tashkilot bo'lmasa ish beruvchining Ism Familiyasini yozing."),
    ("📋 Vakansiya nomi", "📋 Vakansiya nomi:\nVakansiya nomini kiriting, misol uchun:\n\n• Sotuv menejeri\n• Santexnika ustasi\n• Haydovchi"),
    ("💰 Ish haqi", "💰 Ish haqi:\nIsh haqi miqdori, valyutasi va davriyligini kiriting. Misol uchun:\n\n• 3.000.000 so'm - 1 oyga\n• 100 dollar - 1 ishga"),
    ("🌏 Manzil", "🌏 Manzil:\nIsh joyi manzilini kiriting. Misol uchun:\n\n• Toshkent shahar, Chilonzor tumani"),
    ("\n📑 Vakansiya haqida", "📑 Vakansiya haqida:\nVakansiya haqida qisqacha ma'lumot bering. Misol uchun, nima qilinishi kerakligi haqida yozing."),
    ("\n📞 Aloqa", "📞 Aloqa:\nBog'lanish uchun telefon raqam yoki elektron pochta manzilini kiriting. Misol uchun:\n\n• +998912345678\n• example@gmail.com"),
    ("🕰 Murojaat qilish vaqti", "🕰 Murojaat qilish vaqti:\nMurojaat qilish mumkin bo'lgan vaqtlarni kiriting. Misol uchun:\n\n• 9:00 - 18:00"),
    ("\n📌 Qo'shimcha ma'lumotlar", """📌 Qo'shimcha ma'lumotlar:\nQoshimcha ma'lumotlarni kiriting. Agarda ular yo'q bo'lsa "Qo'shimcha ma'lumotlar yo'q" tugmasini bosing.""")
]
num_questions = len(questions)


user_responses2 = {}
questions2 = [
    ("⭐️ Ish qidiruvchi", "⭐️ Ish qidiruvchi:\nIsh qidiruvchining Ism Familiyasini kiriting."),
    ("🗓 Tug'ilgan sana", "🗓 Tug'ilgan sana:\nIsh qidiruvchining tug'ilgan sanasini kiriting. Misol uchun:\n\n• 12.06.2000"),
    ("💠 Mutaxassislik", "💠 Mutaxassislik:\nIsh qidiruvchining mutaxassisligini kiriting. Misol uchun:\n\n• Sotuv menejeri\n• Santexnika ustasi\n• Haydovchi"),
    ("🌏 Manzil", "🌏 Manzil:\nIsh qidiruvchining manzilini kiriting. Misol uchun:\n\n• Toshkent shahar, Chilonzor tumani"),
    ("💰 Ish haqi", "💰 Ish haqi:\nIsh qidiruvchiga maqul ish haqini kiriting. Ish haqi miqdori, valyutasi va davriyligini yozing. Misol uchun:\n\n• 3.000.000 so'm - 1 oyga\n• 100 dollar - 1 ishga"),
    ("🧑‍🎓 Talaba", """🧑‍🎓 Talaba:\nIsh qidiruvchi talaba bo'lsa "Ha" tugmasini, aksincha bo'lsa "Yo'q" tugmasini bosing."""),
    ("📑 Ish qidiruvchi haqida", "📑 Ish qidiruvchi haqida:\nIsh qidiruvchi haqida qisqacha ma'lumot bering. Misol uchun, qanday bilim va qobiliyatlarga ega ekanligi haqida yozing."),
    ("📞 Aloqa", "📞 Aloqa:\nBog'lanish uchun telefon raqam yoki elektron pochta manzilini kiriting. Misol uchun:\n\n• +998912345678\n• example@gmail.com"),
    ("🕰 Murojaat qilish vaqti", "🕰 Murojaat qilish vaqti:\nMurojaat qilish mumkin bo'lgan vaqtlarni kiriting. Misol uchun:\n\n• 9:00 - 18:00"),
    ("📌 Qo'shimcha ma'lumotlar", """📌 Qo'shimcha ma'lumotlar:\nQoshimcha ma'lumotlarni kiriting. Agarda ular yo'q bo'lsa "Qo'shimcha ma'lumotlar yo'q" tugmasini bosing.""")
]
num_questions2 = len(questions2)


user_responses3 = {}
questions3 = [
    ("🧑🏻‍🏫 Ustoz", "🧑🏻‍🏫 Ustoz:\nUstozning Ism Familiyasini yozing."),
    ("📋 Ustozlik yo'nalishi", "📋 Ustozlik yo'nalishi:\nQanday yo'nalish bo'yicha shogirt olinsa, shu yo'nalishni kiriting, misol uchun:\n\n• IT yo'nalishi\n• Sotuv menejeri\n• Santexnika ustasi"),
    ("💰 Ish haqi", """💰 Ish haqi:\nIsh haqi yo'q bo'lsa "Yo'q" deb yozing. Ish haqi bor bo'lsa miqdori, valyutasi va davriyligini kiriting. Misol uchun:\n\n• Yo'q\n\n• 3.000.000 so'm - 1 oyga\n• 100 dollar - 1 ishga"""),
    ("🌏 Manzil", "🌏 Manzil:\nFaoliyat yuritish manzilini kiriting. Misol uchun:\n\n• Toshkent shahar, Chilonzor tumani"),
    ("📑 Ustozlik haqida", "📑 Ustozlik haqida:\nUstozlik haqida qisqacha ma'lumot bering. Misol uchun, nimalar qilinishi haqida yoki ustozlik davri qanday o'tishi haqida yozing."),
    ("📞 Aloqa", """📞 Aloqa:\nBog'lanish uchun telefon raqam yoki elektron pochta manzilini kiriting. Misol uchun:\n\n• +998912345678\n• example@gmail.com"""),
    ("🕰 Murojaat qilish vaqti:", "🕰 Murojaat qilish vaqti:\nMurojaat qilish mumkin bo'lgan vaqtlarni kiriting. Misol uchun:\n\n• 9:00 - 18:00"),
    ("📌 Qo'shimcha ma'lumotlar", """📌 Qo'shimcha ma'lumotlar:\nQoshimcha ma'lumotlarni kiriting. Agarda ular yo'q bo'lsa "Qo'shimcha ma'lumotlar yo'q" tugmasini bosing.""")
]
num_questions3 = len(questions3)


user_responses4 = {}
questions4 = [
    ("🧑🏻 Shogirt", "🧑🏻 Shogirt:\nShogirtning Ism Familiyasini kiriting."),
    ("🗓 Tug'ilgan sana", "🗓 Tug'ilgan sana:\nShogirtning tug'ilgan sanasini kiriting. Misol uchun:\n\n• 12.06.2005"),
    ("💠 Shogirtlik yo'nalishi", """💠 Shogirtlik yo'nalishi:\nQanday yo'nalish bo'yicha ustoz qidirilayotgan bo'lsa, shu yo'nalishni kiriting, misol uchun:\n\n• IT yo'nalishi\n• Sotuv menejeri\n• Santexnika ustasi"""),
    ("🌏 Manzil", "🌏 Manzil:\nQaysi manzil bo'yicha ustoz qidirilayotgan bo'lsa, shu manzilni kiriting, misol uchun:\n\n• Toshkent shahar, Chilonzor tumani"),
    ("💰 Ish haqi", """💰 Ish haqi:\nIsh haqi kerak bo'lmasa "Kerak emas" deb yozing. Ish haqi kerak bo'lsa miqdori, valyutasi va davriyligini kiriting. Misol uchun:\n\n• Yo'q\n\n• 3.000.000 so'm - 1 oyga\n• 100 dollar - 1 ishga"""),
    ("🧑‍🎓 Talaba", """🧑‍🎓 Talaba:\nShogirt talaba bo'lsa "Ha" tugmasini, aksincha bo'lsa "Yo'q" tugmasini bosing."""),
    ("📑 Shogirt haqida", "📑 Shogirt haqida:\nShogirt haqida qisqacha ma'lumot bering. Misol uchun, qanday bilim va qibiliyatlarga ega ekanligi haqida yozing."),
    ("📞 Aloqa", "📞 Aloqa:\nBog'lanish uchun telefon raqam yoki elektron pochta manzilini kiriting. Misol uchun:\n\n• +998912345678\n• example@gmail.com"),
    ("🕰 Murojaat qilish vaqti", "🕰 Murojaat qilish vaqti:\nMurojaat qilish mumkin bo'lgan vaqtlarni kiriting. Misol uchun:\n\n• 9:00 - 18:00"),
    ("📌 Qo'shimcha ma'lumotlar", """📌 Qo'shimcha ma'lumotlar:\nQoshimcha ma'lumotlarni kiriting. Agarda ular yo'q bo'lsa "Qo'shimcha ma'lumotlar yo'q" tugmasini bosing.""")
]
num_questions4 = len(questions4)

user_responses5 = {}
questions5 = [
    ("⭐️ Sherik", "⭐️ Sherik:\nSherikning Ism Familiyasini yozing."),
    ("📋 Sheriklik yo'nalishi", "📋 Sheriklik yo'nalishi:\nQanday yo'nalish bo'yicha sherik qidirilayotgan bo'lsa, shu yo'nalishni kiriting, misol uchun:\n\n• IT yo'nalishi\n• Savdo-sotiq yo'nalishi\n• Ishlab chiqarish yo'nalishi\n• Qimmatbaho toshlar yo'nalishi"),
    ("💰 Hisob-kitob", """💰 Hisob-kitob:\nHisob-kitob alohida muzokara qilinsa "Alohida muzokara qilinadi" deb yozing. Hisob-kitob e'lon qilinsa ma'lumotlarini kiriting. Misol uchun:\n\n• Alohida muzokara qilinadi\n\n• 50/50 ishlanadi\n• Har sotuvdan 20%"""),
    ("🌏 Manzil", "🌏 Manzil:\nQaysi manzil bo'yicha ustoz qidirilayotgan bo'lsa, shu manzilni kiriting, misol uchun:\n\n• Toshkent shahar, Chilonzor tumani"),
    ("📑 Sheriklik haqida", """📑 Sheriklik haqida:\nSheriklik haqida qisqacha ma'lumot bering. Misol uchun, nimalar qilinishi haqida yozing."""),
    ("📞 Aloqa", """📞 Aloqa:\nBog'lanish uchun telefon raqam yoki elektron pochta manzilini kiriting. Misol uchun:\n\n• +998912345678\n• example@gmail.com"""),
    ("🕰 Murojaat qilish vaqti", "🕰 Murojaat qilish vaqti:\nMurojaat qilish mumkin bo'lgan vaqtlarni kiriting. Misol uchun:\n\n• 9:00 - 18:00"),
    ("📌 Qo'shimcha ma'lumotlar", """📌 Qo'shimcha ma'lumotlar:\nQoshimcha ma'lumotlarni kiriting. Agarda ular yo'q bo'lsa "Qo'shimcha ma'lumotlar yo'q" tugmasini bosing.""")
]
num_questions5 = len(questions5)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton("🏢 Ish joylash", callback_data='Ish joylash')
    bt2 = types.InlineKeyboardButton("🧑🏻‍💼 Rezyume joylash", callback_data='Rezyume joylash')
    bt3 = types.InlineKeyboardButton("🧑🏻 Shogirt kerak", callback_data='Shogirt kerak')
    bt4 = types.InlineKeyboardButton("🧑🏻‍🏫 Ustoz kerak", callback_data='Ustoz kerak')
    bt5 = types.InlineKeyboardButton("🎗 Sherik kerak", callback_data='Sherik kerak')
    markup.row(bt1, bt2)
    markup.row(bt3, bt4)
    markup.row(bt5)
    bot.reply_to(message, f"""*Assalomu alaykum {message.from_user.first_name},"EFFECT | Katta mehnat bozori" @palonchi kanali uchun e'lon yaratuvchi botiga xush kelibsiz.*\n\n"EFFECT | Katta mehnat bozori" - ish izlayotgan odamlarga vakansiyalarni, ish beruvchilarga esa ishchilarni topishda yordam beradi. Qolaversa bir qator boshqa yo'nalishlarni ham qollab quvvatlaydi.\n\n*Yo'nalishlar:*\n• "🏢 Ish joylash" - ishchi topish uchun.\n• "🧑🏻‍💼 Rezyume joylash" - ish topish uchun.\n• "🧑🏻 Shogirt kerak" - shogirt topish uchun.\n• "🧑🏻‍🏫 Ustoz kerak" - ustoz topish uchun.\n• "🎗 Sherik kerak" - sherik topish uchun.• "🎗 Sherik kerak" - sherik topish uchun.\n\n*E'lon berish uchun yo'nalishni tanlang 👇*""", reply_markup=markup, parse_mode='Markdown')



@bot.callback_query_handler(func=lambda call: call.data in ['Ish joylash', 'Rezyume joylash', 'Shogirt kerak', 'Ustoz kerak', 'Sherik kerak', 'Ha', "Yo'q", 'info', 'info2', 'No', 'Yes', 'confirm_manager'])
def callback_query(call):
    message = call.message
    chat_id = message.chat.id

    if call.data == "Ish joylash":
        start_process_job(message, call)
    elif call.data == "Rezyume joylash":
        start_process_resume(message, call)
    elif call.data == "Shogirt kerak":
        start_process_shogirt(message, call)
    elif call.data == "Ustoz kerak":
        start_process_ustoz(message, call)
    elif call.data == "Sherik kerak":
        start_process_sherik(message, call)
    elif call.data == "No":
        bot.send_message(message.chat.id, "❌ E'lon qabul qilinmadi.")
        send_no(message)
    elif call.data == 'Yes':
        handle_confirm(call)
    elif call.data == 'confirm_manager':
        handle_confirm_manager(call)






    elif chat_id in user_responses:
        process_job(message, call)
    elif chat_id in user_responses2:
        process_resume(message, call)
    elif chat_id in user_responses3:
        process_shogirt(message, call)
    elif chat_id in user_responses4:
        process_ustoz(message, call)
    elif chat_id in user_responses5:
        process_sherik(message, call)



def send_no(message):
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton("🏢 Ish joylash", callback_data='Ish joylash')
    bt2 = types.InlineKeyboardButton("🧑🏻‍💼 Rezyume joylash", callback_data='Rezyume joylash')
    bt3 = types.InlineKeyboardButton("🧑🏻 Shogirt kerak", callback_data='Shogirt kerak')
    bt4 = types.InlineKeyboardButton("🧑🏻‍🏫 Ustoz kerak", callback_data='Ustoz kerak')
    bt5 = types.InlineKeyboardButton("🎗 Sherik kerak", callback_data='?????????????')
    markup.row(bt1, bt2)
    markup.row(bt3, bt4)
    markup.row(bt5)
    bot.reply_to(message, f"""*Yo'nalishlar:*\n\n• "🏢 Ish joylash" - ishchi topish uchun.\n• "🧑🏻‍💼 Rezyume joylash" - ish topish uchun.\n• "🧑🏻 Shogirt kerak" - shogirt topish uchun.\n• "🧑🏻‍🏫 Ustoz kerak" - ustoz topish uchun.\n• "🎗 Sherik kerak" - sherik topish uchun.\n\n*Yangi e'lon berish uchun yo'nalishni tanlang 👇*""", reply_markup=markup, parse_mode='Markdown')




def handle_confirm_manager(call):
    message = call.message
    chat_id = message.chat.id
    group_chat_id = '-1002133496353'

    summary_text = message.text
    bot.send_message(group_chat_id, summary_text)
    bot.answer_callback_query(call.id, "Данные отправились в группу!")
    bot.send_message(chat_id, "Сообщение отправлено в группу ")

def handle_confirm(call):
    message = call.message
    chat_id = call.message.chat.id
    if chat_id in user_responses and user_responses[chat_id]:
        username = call.from_user.username
        summary_text = format_summary(user_responses.pop(chat_id), username)
        send_to_manager(summary_text)
        bot.answer_callback_query(call.id, "Маълумотлар юборилди!")
        bot.send_message(chat_id, "Сизнинг маълумотларингиз менеджерга юборилди. Сиз билан боғланишади!")
        bot.send_message(chat_id, "E'lon berish uchun yo'nalishni tanlang 👇")
        send_welcome(message)

    elif chat_id in user_responses2 and user_responses2[chat_id]:
        username = call.from_user.username
        summary_text = format_summary2(user_responses2.pop(chat_id), username)
        send_to_manager(summary_text)
        bot.answer_callback_query(call.id, "Маълумотлар юборилди!")
        bot.send_message(chat_id, "Сизнинг маълумотларингиз менеджерга юборилди. Сиз билан боғланишади!")
        bot.send_message(chat_id, "E'lon berish uchun yo'nalishni tanlang 👇")
        send_welcome(message)

    elif chat_id in user_responses3 and user_responses3[chat_id]:
        username = call.from_user.username
        summary_text = format_summary3(user_responses3.pop(chat_id), username)
        send_to_manager(summary_text)
        bot.answer_callback_query(call.id, "Маълумотлар юборилди!")
        bot.send_message(chat_id, "Сизнинг маълумотларингиз менеджерга юборилди. Сиз билан боғланишади!")
        bot.send_message(chat_id, "E'lon berish uchun yo'nalishni tanlang 👇")
        send_welcome(message)

    elif chat_id in user_responses4 and user_responses4[chat_id]:
        username = call.from_user.username
        summary_text = format_summary4(user_responses4.pop(chat_id), username)
        send_to_manager(summary_text)
        bot.answer_callback_query(call.id, "Маълумотлар юборилди!")
        bot.send_message(chat_id, "Сизнинг маълумотларингиз менеджерга юборилди. Сиз билан боғланишади!")
        bot.send_message(chat_id, "E'lon berish uchun yo'nalishni tanlang 👇")
        send_welcome(message)

    else:
        bot.answer_callback_query(call.id, "Сизнинг маълумотларингиз топилмади!")

def send_to_manager(summary_text):
    manager_chat_id = '168724495'
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("HA", callback_data=f'confirm_manager'))
    bot.send_message(manager_chat_id, summary_text, reply_markup=markup)





def format_summary(user_data, username):
    if not user_data:
        return "No data provided"
    response_text = "🏢 ISH\n\n"
    response_text += f"⭐️ Ish beruvchi: {user_data[0]}\n"
    response_text += f"📋 Vakansiya nomi: {user_data[1]}\n"
    response_text += f"💰 Ish haqi: {user_data[2]}\n"
    response_text += f"🌏 Manzil: {user_data[3]}\n\n"
    response_text += f"📑 Vakansiya haqida: {user_data[4]}\n\n"
    response_text += f"📞 Aloqa: {user_data[5]}\n"
    response_text += f"✉️ Telegram: @{username}\n"
    response_text += f"🕰 Murojaat qilish vaqti: {user_data[6]}\n\n"
    response_text += f"📌 Qo'shimcha ma'lumotlar: {user_data[7]}\n\n"
    response_text += "#Ish\n\n"
    response_text += "🌐  EFFECT | Katta mehnat bozori kanaliga obuna bo'lish (https://t.me/test_bot1567)"
    return response_text

def format_summary2(user_data, username):
    if not user_data:
        return "No data provided"
    response_text = "REZYUME 🧑🏻‍💼\n\n"
    response_text += f"⭐️ Ish qidiruvchi: {user_data[0]}\n"
    response_text += f"🗓 Tug'ilgan sana: {user_data[1]}\n"
    response_text += f"💠 Mutaxassislik: {user_data[2]}\n"
    response_text += f"🌏 Manzil: {user_data[3]}\n"
    response_text += f"💰 Ish haqi: {user_data[4]}\n\n"
    response_text += f"🧑‍🎓 Talaba: {user_data[5]}\n"
    response_text += f"📑 Ish qidiruvchi haqida: {user_data[6]}\n\n"
    response_text += f"📞 Aloqa: {user_data[7]}\n"
    response_text += f"✉️ Telegram: @{username}\n"
    response_text += f"🕰 Murojaat qilish vaqti: {user_data[8]}\n\n"
    response_text += f"📌 Qo'shimcha ma'lumotlar: {user_data[9]}\n\n"
    response_text += "#Rezyume\n\n"
    response_text += "🌐 EFFECT | Katta mehnat bozori kanaliga obuna bo'lish (https://t.me/test_bot1567)"
    return response_text

def format_summary3(user_data, username):
    if not user_data:
        return "No data provided"
    response_text = "SHOGIRT KERAK 🧑🏻\n\n"
    response_text += f"🧑🏻‍🏫 Ustoz: {user_data[0]}\n"
    response_text += f"📋 Ustozlik yo'nalishi: {user_data[1]}\n"
    response_text += f"💰 Ish haqi: {user_data[2]}\n"
    response_text += f"🌏 Manzil: {user_data[3]}\n\n"
    response_text += f"📑 Ustozlik haqida: {user_data[4]}\n\n"
    response_text += f"📞 Aloqa: {user_data[5]}\n"
    response_text += f"✉️ Telegram: @{username}\n"
    response_text += f"🕰 Murojaat qilish vaqti: {user_data[6]}\n\n"
    response_text += f"📌 Qo'shimcha ma'lumotlar: {user_data[7]}\n\n"
    response_text += "#ShogirtKerak\n\n"
    response_text += "🌐 EFFECT | Katta mehnat bozori kanaliga obuna bo'lish (https://t.me/test_bot1567)"
    return response_text

def format_summary4(user_data, username):
    if not user_data:
        return "No data provided"
    response_text = "USTOZ KERAK 🧑🏻‍🏫\n\n"
    response_text += f"🧑🏻 Shogirt: {user_data[0]}\n"
    response_text += f"🗓 Tug'ilgan sana: {user_data[1]}\n"
    response_text += f"💠 Shogirtlik yo'nalishi: {user_data[2]}\n"
    response_text += f"🌏 Manzil: {user_data[3]}\n"
    response_text += f"💰 Ish haqi: {user_data[4]}\n\n"
    response_text += f"🧑‍🎓 Talaba: {user_data[5]}\n"
    response_text += f"📑 Shogirt haqida: {user_data[6]}\n\n"
    response_text += f"📞 Aloqa: {user_data[7]}\n"
    response_text += f"✉️ Telegram: @{username}\n"
    response_text += f"🕰 Murojaat qilish vaqti: {user_data[8]}\n\n"
    response_text += f"📌 Qo'shimcha ma'lumotlar: {user_data[9]}\n\n"
    response_text += "#UstozKerak\n\n"
    response_text += "🌐 EFFECT | Katta mehnat bozori kanaliga obuna bo'lish (https://t.me/test_bot1567)"
    return response_text

def format_summary5(user_data, username):
    if not user_data:
        return "No data provided"
    response_text = "🎗 SHERIK KERAK\n\n"
    response_text += f"⭐️ Sherik: {user_data[0]}\n"
    response_text += f"📋 Sheriklik yo'nalishi: {user_data[1]}\n"
    response_text += f"💰 Hisob-kitob: {user_data[2]}\n"
    response_text += f"🌏 Manzil: {user_data[3]}\n"
    response_text += f"📑 Sheriklik haqida: {user_data[4]}\n\n"
    response_text += f"📞 Aloqa: {user_data[5]}\n"
    response_text += f"✉️ Telegram: @{username}\n"
    response_text += f"🕰 Murojaat qilish vaqti: {user_data[6]}\n\n"
    response_text += f"📌 Qo'shimcha ma'lumotlar: {user_data[7]}\n\n"
    response_text += "#SherikKerak\n\n"
    response_text += "🌐 EFFECT | Katta mehnat bozori kanaliga obuna bo'lish (https://t.me/test_bot1567)"
    return response_text




def start_process_job(message, call):
    chat_id = message.chat.id
    user_responses[chat_id] = []
    text = """*🏢 ISH\n\nIsh joylashtirish uchun bir nechta savollarga javob bering. Har bir javobingiz to'g'ri va ishonchli ma'lumotlardan iborat bo'lishi kerak ekanligiga e'tiborli bo'ling.\n\nSo'rovnoma yakunida, agarda kiritilgan barcha ma'lumotlar to'g'ri bo'lsa "✅ To'g'ri" tugmasini bosing, aksincha bo'lsa "❌ Noto'g'ri" tugmasini bosing va so'rovnomani qaytadan to'ldiring.\n\nE'lon tayor bo'lgandan kegin "E'lonni joylash" tugmasi bosilsa e'lon o'sha zaxotiyoq "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtiriladi.*"""
    bot.reply_to(message, text, parse_mode='Markdown')
    ask_question(message, 0)

def start_process_resume(message, call):
    chat_id = message.chat.id
    text = """*🧑🏻‍💼 REZYUME*\n\nRezyume joylashtirish uchun bir nechta savollarga javob bering. Har bir javobingiz to'g'ri va ishonchli ma'lumotlardan iborat bo'lishi kerak ekanligiga e'tiborli bo'ling.\n\nSo'rovnoma yakunida, agarda kiritilgan barcha ma'lumotlar to'g'ri bo'lsa "✅ To'g'ri" tugmasini bosing, aksincha bo'lsa "❌ Noto'g'ri" tugmasini bosing va so'rovnomani qaytadan to'ldiring.\n\nE'lon tayor bo'lgandan kegin "E'lonni joylash" tugmasi bosilsa e'lon o'sha zaxotiyoq "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtiriladi."""
    bot.reply_to(message, text, parse_mode='Markdown')
    user_responses2[chat_id] = []
    ask_question1(message, 0)

def start_process_shogirt(message, call):
    chat_id = message.chat.id
    text = """*🧑🏻 SHOGIRT KERAK\n\nShogirt kerakligi haqida e'lon joylashtirish uchun bir nechta savollarga javob bering. Har bir javobingiz to'g'ri va ishonchli ma'lumotlardan iborat bo'lishi kerak ekanligiga e'tiborli bo'ling.\n\nSo'rovnoma yakunida, agarda kiritilgan barcha ma'lumotlar to'g'ri bo'lsa "✅ To'g'ri" tugmasini bosing, aksincha bo'lsa "❌ Noto'g'ri" tugmasini bosing va so'rovnomani qaytadan to'ldiring.\n\nE'lon tayor bo'lgandan kegin "E'lonni joylash" tugmasi bosilsa e'lon o'sha zaxotiyoq "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtiriladi.*"""
    bot.reply_to(message, text, parse_mode='Markdown')
    user_responses3[chat_id] = []
    ask_question2(message, 0)

def start_process_ustoz(message, call):
    chat_id = message.chat.id
    text = """*🧑🏻‍🏫 USTOZ KERAK*\n\nUstoz kerakligi haqida e'lon joylashtirish uchun bir nechta savollarga javob bering. Har bir javobingiz to'g'ri va ishonchli ma'lumotlardan iborat bo'lishi kerak ekanligiga e'tiborli bo'ling.\n\nSo'rovnoma yakunida, agarda kiritilgan barcha ma'lumotlar to'g'ri bo'lsa "✅ To'g'ri" tugmasini bosing, aksincha bo'lsa "❌ Noto'g'ri" tugmasini bosing va so'rovnomani qaytadan to'ldiring.\n\nE'lon tayor bo'lgandan kegin "E'lonni joylash" tugmasi bosilsa e'lon o'sha zaxotiyoq "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtiriladi."""
    bot.reply_to(message, text, parse_mode='Markdown')
    user_responses4[chat_id] = []
    ask_question3(message, 0)

def start_process_sherik(message, call):
    chat_id = message.chat.id
    text = """*🎗 SHERIK KERAK*\n\nSherik kerakligi haqida e'lon joylashtirish uchun bir nechta savollarga javob bering. Har bir javobingiz to'g'ri va ishonchli ma'lumotlardan iborat bo'lishi kerak ekanligiga e'tiborli bo'ling.\n\nSo'rovnoma yakunida, agarda kiritilgan barcha ma'lumotlar to'g'ri bo'lsa "✅ To'g'ri" tugmasini bosing, aksincha bo'lsa "❌ Noto'g'ri" tugmasini bosing va so'rovnomani qaytadan to'ldiring.\n\nE'lon tayor bo'lgandan kegin "E'lonni joylash" tugmasi bosilsa e'lon o'sha zaxotiyoq "EFFECT | Katta mehnat bozori" @palonchi kanaliga joylashtiriladi."""
    bot.reply_to(message, text, parse_mode='Markdown')
    user_responses5[chat_id] = []
    ask_question4(message, 0)




def process_job(message, call):
    chat_id = message.chat.id
    user_data = user_responses.get(chat_id, [])
    question_index = len(user_data)

    if call.data in ['info']:
        user_data.append(call.data if call.data != 'info' else "Yo'q")
        question_index += 1

    if question_index >= num_questions:
        send_summary0(message, user_data, call.from_user.username)
    else:
        ask_question(message, question_index)

def process_resume(message, call):
    chat_id = message.chat.id
    user_data = user_responses2.get(chat_id, [])
    question_index = len(user_data)

    if call.data in ['Ha', "Yo'q", 'info2']:
        user_responses2[message.chat.id].append(call.data if call.data != 'info2' else "Yo'q")
        question_index += 1

    if question_index >= num_questions2:
        send_summary(message, user_data, call.from_user.username)
    else:
        ask_question1(message, question_index)

def process_shogirt(message, call):
    chat_id = message.chat.id
    user_data = user_responses3.get(chat_id, [])
    question_index = len(user_data)

    if call.data in ['info']:
        user_responses3[message.chat.id].append(call.data if call.data != 'info' else "Yo'q")
        question_index += 1

    if question_index >= num_questions3:
        send_summary1(message, user_data, call.from_user.username)
    else:
        ask_question2(message, question_index)

def process_ustoz(message, call):
    chat_id = message.chat.id
    user_data = user_responses4.get(chat_id, [])
    question_index = len(user_data)

    if call.data in ['Ha', "Yo'q", 'info']:
        user_responses4[message.chat.id].append(call.data if call.data != 'info' else "Yo'q")
        question_index += 1

    if question_index >= num_questions4:
        send_summary2(message, user_data, call.from_user.username)
    else:
        ask_question3(message, question_index)

def process_sherik(message, call):
    chat_id = message.chat.id
    user_data = user_responses5.get(chat_id, [])
    question_index = len(user_data)

    if call.data in ['info']:
        user_responses5[message.chat.id].append(call.data if call.data != 'info' else "Yo'q")
        question_index += 1

    if question_index >= num_questions5:
        send_summary3(message, user_data, call.from_user.username)
    else:
        ask_question4(message, question_index)






def ask_question(message, question_index):
    if question_index < num_questions:
        question_text = questions[question_index][1]
        question_text = apply_formatting(question_text)
        markup = types.InlineKeyboardMarkup()
        if question_index == 7:
            markup.add(types.InlineKeyboardButton("Qo'shimcha ma'lumotlar yo'q", callback_data='info'))
        else:
            markup = None

        msg = bot.send_message(message.chat.id, question_text, reply_markup=markup, parse_mode='Markdown')
        bot.register_next_step_handler(msg, handle_answer1, question_index)
    else:
        all_answers = user_responses[message.chat.id]
        send_summary0(message, all_answers, message.from_user.username)

def handle_answer1(message, question_index):
    user_responses[message.chat.id].append(message.text)
    ask_question(message, question_index + 1)

def send_summary0(message, answers, username):
    chat_id = message.chat.id
    response_text = format_summary(answers, username)
    bot.send_message(chat_id, response_text)


    mess = "*Barcha ma'lumotlar to'g'rimi?*"
    markup = types.InlineKeyboardMarkup()
    btn_confirm = types.InlineKeyboardButton("✅ To'g'ri", callback_data='Yes')
    btn_edit = types.InlineKeyboardButton("❌ Noto'g'ri", callback_data='No')
    markup.add(btn_confirm, btn_edit)

    bot.send_message(chat_id, mess, reply_markup=markup, parse_mode='Markdown')

def apply_formatting(text):
    formatted_text = text.replace('⭐️ Ish beruvchi:', '*⭐️ Ish beruvchi:*')
    formatted_text = formatted_text.replace("📋 Vakansiya nomi:", "*📋 Vakansiya nomi:*")
    formatted_text = formatted_text.replace('• Sotuv menejeri', '_• Sotuv menejeri_')
    formatted_text = formatted_text.replace('• Santexnika ustasi', '_• Santexnika ustasi_')
    formatted_text = formatted_text.replace('• Haydovchi', '_• Haydovchi_')
    formatted_text = formatted_text.replace('💰 Ish haqi:', '*💰 Ish haqi:*')
    formatted_text = formatted_text.replace("• 3.000.000 so'm - 1 oyga", "_• 3.000.000 so'm - 1 oyga_")
    formatted_text = formatted_text.replace('• 100 dollar - 1 ishga', '_• 100 dollar - 1 ishga_')
    formatted_text = formatted_text.replace('🌏 Manzil:', '*🌏 Manzil:*')
    formatted_text = formatted_text.replace('• Toshkent shahar, Chilonzor tumani', '_• Toshkent shahar, Chilonzor tumani_')
    formatted_text = formatted_text.replace('📑 Vakansiya haqida:', '*📑 Vakansiya haqida:*')
    formatted_text = formatted_text.replace('📞 Aloqa:', '*📞 Aloqa:*')
    formatted_text = formatted_text.replace('• +998912345678', '_• +998912345678_')
    formatted_text = formatted_text.replace('• example@gmail.com', '_• example@gmail.com_')
    formatted_text = formatted_text.replace('🕰 Murojaat qilish vaqti:', '*🕰 Murojaat qilish vaqti:*')
    formatted_text = formatted_text.replace('• 9:00 - 18:00', '_• 9:00 - 18:00_')
    formatted_text = formatted_text.replace("📌 Qo'shimcha ma'lumotlar:", "*📌 Qo'shimcha ma'lumotlar:*")
    return formatted_text




def ask_question1(message, question_index):
    if question_index < num_questions2:
        question_text = questions2[question_index][1]
        question_text = apply_formatting1(question_text)
        markup = types.InlineKeyboardMarkup()
        if question_index == 5:
            markup.add(types.InlineKeyboardButton("Ha", callback_data='Ha'),
                       types.InlineKeyboardButton("Yo'q", callback_data="Yo'q"))
        elif question_index == 9:
            markup.add(types.InlineKeyboardButton("Qo'shimcha ma'lumotlar yo'q", callback_data='info2'))
        else:
            markup = None

        msg = bot.send_message(message.chat.id, question_text, reply_markup=markup, parse_mode='Markdown')
        if markup is None or question_index == 9:
            bot.register_next_step_handler(msg, handle_answer2, question_index)
    else:
        all_answers = user_responses2[message.chat.id]
        send_summary(message, all_answers, message.from_user.username)

def handle_answer2(message, question_index):
    chat_id = message.chat.id
    if chat_id not in user_responses2:
        user_responses2[chat_id] = []
    user_responses2[chat_id].append(message.text)
    ask_question1(message, question_index + 1)

def send_summary(message, answers, username):
    chat_id = message.chat.id
    response_text = format_summary2(answers, username)
    bot.send_message(chat_id, response_text)

    mess = "*Barcha ma'lumotlar to'g'rimi?*"
    markup = types.InlineKeyboardMarkup()
    btn_confirm = types.InlineKeyboardButton("✅ To'g'ri", callback_data='Yes')
    btn_edit = types.InlineKeyboardButton("❌ Noto'g'ri", callback_data='No')
    markup.add(btn_confirm, btn_edit)

    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='Markdown')

def apply_formatting1(text):
    formatted_text = text.replace('⭐️ Ish qidiruvchi:', '*⭐️ Ish qidiruvchi:*')
    formatted_text = formatted_text.replace("🗓 Tug'ilgan sana:", "*🗓 Tug'ilgan sana:*")
    formatted_text = formatted_text.replace('• 12.06.2000', '_• 12.06.2000_')
    formatted_text = formatted_text.replace('• Sotuv menejeri', '_• Sotuv menejeri_')
    formatted_text = formatted_text.replace('• Santexnika ustasi', '_• Santexnika ustasi_')
    formatted_text = formatted_text.replace('• Haydovchi', '_• Haydovchi_')
    formatted_text = formatted_text.replace('💠 Mutaxassislik:', '*💠 Mutaxassislik:*')
    formatted_text = formatted_text.replace('💰 Ish haqi:', '*💰 Ish haqi:*')
    formatted_text = formatted_text.replace("• 3.000.000 so'm - 1 oyga", "_• 3.000.000 so'm - 1 oyga_")
    formatted_text = formatted_text.replace('• 100 dollar - 1 ishga', '_• 100 dollar - 1 ishga_')
    formatted_text = formatted_text.replace('🌏 Manzil:', '*🌏 Manzil:*')
    formatted_text = formatted_text.replace('• Toshkent shahar, Chilonzor tumani', '_• Toshkent shahar, Chilonzor tumani_')
    formatted_text = formatted_text.replace('🧑‍🎓 Talaba:', '*🧑‍🎓 Talaba:*')
    formatted_text = formatted_text.replace('📑 Ish qidiruvchi haqida:', '*📑 Ish qidiruvchi haqida:*')
    formatted_text = formatted_text.replace('📞 Aloqa:', '*📞 Aloqa:*')
    formatted_text = formatted_text.replace('• +998912345678', '_• +998912345678_')
    formatted_text = formatted_text.replace('• example@gmail.com', '_• example@gmail.com_')
    formatted_text = formatted_text.replace('🕰 Murojaat qilish vaqti:', '*🕰 Murojaat qilish vaqti:*')
    formatted_text = formatted_text.replace('• 9:00 - 18:00', '_• 9:00 - 18:00_')
    formatted_text = formatted_text.replace("📌 Qo'shimcha ma'lumotlar:", "*📌 Qo'shimcha ma'lumotlar:*")
    return formatted_text



def ask_question2(message, question_index):
    if question_index < num_questions3:
        question_text = questions3[question_index][1]
        question_text = apply_formatting2(question_text)
        markup = types.InlineKeyboardMarkup()
        if question_index == 7:
            markup.add(types.InlineKeyboardButton("Qo'shimcha ma'lumotlar yo'q", callback_data='info'))
        else:
            markup = None

        msg = bot.send_message(message.chat.id, question_text, reply_markup=markup, parse_mode='Markdown')
        bot.register_next_step_handler(msg, handle_answer3, question_index)
    else:
        all_answers = user_responses3[message.chat.id]
        send_summary1(message, all_answers, message.from_user.username)

def handle_answer3(message, question_index):
    chat_id = message.chat.id
    if chat_id not in user_responses3:
        user_responses3[chat_id] = []
    user_responses3[chat_id].append(message.text)
    ask_question2(message, question_index + 1)

def send_summary1(message, answers, username):
    chat_id = message.chat.id
    response_text = format_summary3(answers, username)
    bot.send_message(chat_id, response_text)

    mess = "*Barcha ma'lumotlar to'g'rimi?*"
    markup = types.InlineKeyboardMarkup()
    btn_confirm = types.InlineKeyboardButton("✅ To'g'ri", callback_data='Yes')
    btn_edit = types.InlineKeyboardButton("❌ Noto'g'ri", callback_data='No')
    markup.add(btn_confirm, btn_edit)

    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='Markdown')

def apply_formatting2(text):
    formatted_text = text.replace('🧑🏻‍🏫 Ustoz:', '*🧑🏻‍🏫 Ustoz:*')
    formatted_text = formatted_text.replace("📋 Ustozlik yo'nalishi:", "*📋 Ustozlik yo'nalishi:*")
    formatted_text = formatted_text.replace("• IT yo'nalishi", "_• IT yo'nalishi_")
    formatted_text = formatted_text.replace('• Sotuv menejeri', '_• Sotuv menejeri_')
    formatted_text = formatted_text.replace('• Santexnika ustasi', '_• Santexnika ustasi_')
    formatted_text = formatted_text.replace('💰 Ish haqi:', '*💰 Ish haqi:*')
    formatted_text = formatted_text.replace("• Yo'q", "_• Yo'q_")
    formatted_text = formatted_text.replace("• 3.000.000 so'm - 1 oyga", "_• 3.000.000 so'm - 1 oyga_")
    formatted_text = formatted_text.replace('• 100 dollar - 1 ishga', '_• 100 dollar - 1 ishga_')
    formatted_text = formatted_text.replace('🌏 Manzil:', '*🌏 Manzil:*')
    formatted_text = formatted_text.replace('• Toshkent shahar, Chilonzor tumani', '_• Toshkent shahar, Chilonzor tumani_')
    formatted_text = formatted_text.replace('📑 Ustozlik haqida:', '*📑 Ustozlik haqida:*')
    formatted_text = formatted_text.replace('📞 Aloqa:', '*📞 Aloqa:*')
    formatted_text = formatted_text.replace('• +998912345678', '_• +998912345678_')
    formatted_text = formatted_text.replace('• example@gmail.com', '_• example@gmail.com_')
    formatted_text = formatted_text.replace('🕰 Murojaat qilish vaqti:', '*🕰 Murojaat qilish vaqti:*')
    formatted_text = formatted_text.replace('• 9:00 - 18:00', '_• 9:00 - 18:00_')
    formatted_text = formatted_text.replace("📌 Qo'shimcha ma'lumotlar:", "*📌 Qo'shimcha ma'lumotlar:*")
    return formatted_text



def ask_question3(message, question_index):
    if question_index < num_questions4:
        question_text = questions4[question_index][1]
        question_text = apply_formatting3(question_text)
        markup = types.InlineKeyboardMarkup()
        if question_index == 5:
            markup.add(types.InlineKeyboardButton("Ha", callback_data='Ha'),
                       types.InlineKeyboardButton("Yo'q", callback_data="Yo'q"))
        elif question_index == 9:
            markup.add(types.InlineKeyboardButton("Qo'shimcha ma'lumotlar yo'q", callback_data='info'))
        else:
            markup = None

        msg = bot.send_message(message.chat.id, question_text, reply_markup=markup, parse_mode='Markdown')
        if markup is None or question_index == 9:
            bot.register_next_step_handler(msg, handle_answer4, question_index)
    else:
        all_answers = user_responses4[message.chat.id]
        send_summary2(message, all_answers, message.from_user.username)

def handle_answer4(message, question_index):
    chat_id = message.chat.id
    if chat_id not in user_responses4:
        user_responses4[chat_id] = []
    user_responses4[chat_id].append(message.text)
    ask_question3(message, question_index + 1)

def send_summary2(message, answers, username):
    chat_id = message.chat.id
    response_text = format_summary4(answers, username)
    bot.send_message(chat_id, response_text)

    mess = "*Barcha ma'lumotlar to'g'rimi?*"
    markup = types.InlineKeyboardMarkup()
    btn_confirm = types.InlineKeyboardButton("✅ To'g'ri", callback_data='Yes')
    btn_edit = types.InlineKeyboardButton("❌ Noto'g'ri", callback_data='No')
    markup.add(btn_confirm, btn_edit)

    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='Markdown')

def apply_formatting3(text):
    formatted_text = text.replace('🧑🏻 Shogirt:', '*🧑🏻 Shogirt:*')
    formatted_text = formatted_text.replace("🗓 Tug'ilgan sana:", "*🗓 Tug'ilgan sana:*")
    formatted_text = formatted_text.replace("• 12.06.2005", "_• 12.06.2005_")
    formatted_text = formatted_text.replace("💠 Shogirtlik yo'nalishi:", "*💠 Shogirtlik yo'nalishi:*")
    formatted_text = formatted_text.replace("• IT yo'nalishi", "_• IT yo'nalishi_")
    formatted_text = formatted_text.replace('• Sotuv menejeri', '_• Sotuv menejeri_')
    formatted_text = formatted_text.replace('• Santexnika ustasi', '_• Santexnika ustasi_')
    formatted_text = formatted_text.replace('💰 Ish haqi:', '*💰 Ish haqi:*')
    formatted_text = formatted_text.replace("• Yo'q", "_• Yo'q_")
    formatted_text = formatted_text.replace("• 3.000.000 so'm - 1 oyga", "_• 3.000.000 so'm - 1 oyga_")
    formatted_text = formatted_text.replace('• 100 dollar - 1 ishga', '_• 100 dollar - 1 ishga_')
    formatted_text = formatted_text.replace('🌏 Manzil:', '*🌏 Manzil:*')
    formatted_text = formatted_text.replace('Toshkent shahar, Chilonzor tumani', '_Toshkent shahar, Chilonzor tumani_')
    formatted_text = formatted_text.replace('🧑‍🎓 Talaba:', '*🧑‍🎓 Talaba:*')
    formatted_text = formatted_text.replace('📑 Shogirt haqida: ', '*📑 Shogirt haqida:*')
    formatted_text = formatted_text.replace('📞 Aloqa:', '*📞 Aloqa:*')
    formatted_text = formatted_text.replace('• +998912345678', '_• +998912345678_')
    formatted_text = formatted_text.replace('• example@gmail.com', '_• example@gmail.com_')
    formatted_text = formatted_text.replace('🕰 Murojaat qilish vaqti:', '*🕰 Murojaat qilish vaqti:*')
    formatted_text = formatted_text.replace('• 9:00 - 18:00', '_• 9:00 - 18:00_')
    formatted_text = formatted_text.replace("📌 Qo'shimcha ma'lumotlar:", "*📌 Qo'shimcha ma'lumotlar:*")
    return formatted_text



def ask_question4(message, question_index):
    if question_index < num_questions5:
        question_text = questions5[question_index][1]
        question_text = apply_formatting4(question_text)
        markup = types.InlineKeyboardMarkup()
        if question_index == 7:
            markup.add(types.InlineKeyboardButton("Qo'shimcha ma'lumotlar yo'q", callback_data='info'))
        else:
            markup = None

        msg = bot.send_message(message.chat.id, question_text, reply_markup=markup, parse_mode='Markdown')
        bot.register_next_step_handler(msg, handle_answer5, question_index)
    else:
        all_answers = user_responses5[message.chat.id]
        send_summary3(message, all_answers, message.from_user.username)

def handle_answer5(message, question_index):
    chat_id = message.chat.id
    if chat_id not in user_responses5:
        user_responses5[chat_id] = []
    user_responses5[chat_id].append(message.text)
    ask_question4(message, question_index + 1)

def send_summary3(message, answers, username):
    chat_id = message.chat.id
    response_text = format_summary5(answers, username)
    bot.send_message(chat_id, response_text)

    mess = "*Barcha ma'lumotlar to'g'rimi?*"
    markup = types.InlineKeyboardMarkup()
    btn_confirm = types.InlineKeyboardButton("✅ To'g'ri", callback_data='Yes')
    btn_edit = types.InlineKeyboardButton("❌ Noto'g'ri", callback_data='No')
    markup.add(btn_confirm, btn_edit)

    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='Markdown')

def apply_formatting4(text):
    formatted_text = text.replace('⭐️ Sherik:', '*⭐️ Sherik:*')
    formatted_text = formatted_text.replace("📋 Sheriklik yo'nalishi:", "*📋 Sheriklik yo'nalishi:*")
    formatted_text = formatted_text.replace("• IT yo'nalishi", "_• IT yo'nalishi_")
    formatted_text = formatted_text.replace("• Savdo-sotiq yo'nalishi", "_• Savdo-sotiq yo'nalishi_")
    formatted_text = formatted_text.replace("• Ishlab chiqarish yo'nalishi", "_• Ishlab chiqarish yo'nalishi_")
    formatted_text = formatted_text.replace("• Qimmatbaho toshlar yo'nalishi", "_• Qimmatbaho toshlar yo'nalishi_")
    formatted_text = formatted_text.replace('💰 Hisob-kitob:', '*💰 Hisob-kitob:*')
    formatted_text = formatted_text.replace('• Alohida muzokara qilinadi', '_• Alohida muzokara qilinadi_')
    formatted_text = formatted_text.replace('• 50/50 ishlanadi', '_• 50/50 ishlanadi_')
    formatted_text = formatted_text.replace('• Har', '_• Har_')
    formatted_text = formatted_text.replace('20%', '_20%_')
    formatted_text = formatted_text.replace('🌏 Manzil:', '*🌏 Manzil:*')
    formatted_text = formatted_text.replace('• Toshkent shahar, Chilonzor tumani', '_• Toshkent shahar, Chilonzor tumani_')
    formatted_text = formatted_text.replace('📑 Sheriklik haqida:', '*📑 Sheriklik haqida:*')
    formatted_text = formatted_text.replace('📞 Aloqa:', '*📞 Aloqa:*')
    formatted_text = formatted_text.replace('• +998912345678', '_• +998912345678_')
    formatted_text = formatted_text.replace('• example@gmail.com', '_• example@gmail.com_')
    formatted_text = formatted_text.replace('🕰 Murojaat qilish vaqti:', '*🕰 Murojaat qilish vaqti:*')
    formatted_text = formatted_text.replace('• 9:00 - 18:00', '_• 9:00 - 18:00_')
    formatted_text = formatted_text.replace("📌 Qo'shimcha ma'lumotlar:", "*📌 Qo'shimcha ma'lumotlar:*")
    return formatted_text


bot.polling(none_stop=True)
'''