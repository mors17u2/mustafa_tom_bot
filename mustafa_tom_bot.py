from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
import asyncio

# استبدل "YOUR_TOKEN" برمز الوصول (Token) الخاص بالبوت
TOKEN = '7745977689:AAGjl6jAYesQcSTOkw6BjJRnyllJjJuFaLM'

# دالة الرد على الرسائل
async def reply_to_greetings(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text.lower().strip()  # تحويل النص إلى أحرف صغيرة وإزالة المسافات الزائدة

    # الرموز التعبيرية المناسبة لكل رد
    responses = {
        "السلام عليكم": "وعليكم السلام، شلونك؟ 👋",
        "مرحبا": "هلا بيك، شلونك؟ 👋",
        "هلو": "هلا بيك، شلونك؟ 👋",
        "شلونك": "تمام، انت شلونك؟ 👍",
        "شلونچ": "تمام، انتي شلونچ؟ 👍",
        "شلونكم": "تمام، انتو شلونكم؟ 👍",
        "صباح الخير": "صباح النور، يومك سعيد! ☀️",
        "مساء الخير": "مساء النور، شلونك بالليل؟ 🌙",
        "الله بالخير": "الله بالخير، شلونك؟ 🌟",
        "هلا": "هلا بيك، شخبارك؟ 👋",
        "ها": "هلا بيك، شخبارك؟ 👋",
        "وينك": "موجود، انت وينك؟ 🕵️",
        "شخبارك": "كلشي تمام، انت شخبارك؟ 😊",
        "تصبح على خير": "وأنت من أهله، تصبح على خير. 🌜",
        "تنام": "وأنت من أهله، تصبح على خير. 🌜",
        "الحمد لله": "الله يديم العافية. 🙌",
        "يعني": "يعني الحمد لله، الأمور بخير. 🤔",
        "شكو ماكو": "ماكو شي، كله هدوء!🤷🏻‍♂️",
        "كيف حالك": "الحمد لله، وأنت؟ 😊",
        "عاش من شافك": "انت العايش، شلون صحتك؟ 😍",
        "تعال": "وين، شنو تريد؟ 👉",
        "اني جاي": "حياك الله، وينك من زمان؟ 🎉",
        "تروح وتجي": "إن شاء الله دوم بخير. 🙌",
        "جيد": "تمام، المهم صحتك! 👌",
        "وين كنت": "كنت مشغول شوية. 🤔",
        "حبيبي": "حبيبي الغالي، شخبارك؟ ❤️",
        "شكرا": "عفوا، لا شكر على واجب.❤",
        "مشتاق لك": "وأني هم مشتاق لك، تفضل! 😍"
    }

    # تحقق مما إذا كانت الرسالة تحتوي على كلمة "بوت"
    if "بوت" in message_text and len(message_text.split()) > 1:
        await update.message.reply_text("خير شرايد. 🤔\n\nDev.Mustafa   ||   @mu_rs")
        return  # الخروج من الدالة هنا

    # البحث عن الرد المناسب
    response = None
    for key in responses.keys():
        if key in message_text:
            response = responses[key]
            break

    # إذا لم يتم العثور على أي رد مناسب، فلا يرد البوت على الرسالة
    if response is None:
        return  # لا يقوم البوت بالرد على الرسالة

    # إرسال الرد
    await update.message.reply_text(response + "\n\nDev.Mustafa   ||   @mu_rs")

async def main():
    # إعداد البوت باستخدام Token
    application = Application.builder().token(TOKEN).build()
    
    # تهيئة التطبيق
    await application.initialize()

    # إضافة معالج للرسائل النصية
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_greetings))

    # بدء تشغيل البوت بدون إغلاق الحلقة
    await application.start()
    print("Bot started...")

    # تشغيل البوت بشكل متواصل
    await application.updater.start_polling()
    
    # نستخدم هذه الطريقة للتأكد من استمرار البرنامج بالعمل بشكل لا نهائي
    await asyncio.Event().wait()  # This will keep the bot running indefinitely

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    if not loop.is_running():
        loop.run_until_complete(main())
    else:
        asyncio.ensure_future(main())