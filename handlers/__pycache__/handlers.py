# ==========================================
# handlers/handlers.py
# بخش اول
# ==========================================

import telebot

from keyboards.menus import (
    main_menu,
    link_menu,
    business_menu,
    business_buttons
)

from data.texts import (
    LINK_TEXT,
    WORK_TEXT,
    INCOME_TEXT,
    CONTACT_TEXT,
    SIMIN_TEXT,
    BERS_TEXT
)

from data.businesses import BUSINESSES

TEXTS = {
    "SIMIN_TEXT": SIMIN_TEXT,
    "BERS_TEXT": BERS_TEXT,
}

# -------------------------
# وضعیت آخرین کسب‌وکار
# -------------------------

last_business = {}


# -------------------------
# استارت
# -------------------------

def register_handlers(bot):

    @bot.message_handler(commands=["start"])
    def start(message):

        bot.send_message(
            message.chat.id,
            "👋 به لینک خوش آمدید.\n\nیکی از گزینه‌های زیر را انتخاب کنید.",
            reply_markup=main_menu()
        )


    # ==========================
    # منوی اصلی
    # ==========================

    @bot.message_handler(func=lambda message: True)
    def messages(message):

        text = message.text


        # ----------------------
        # بازگشت
        # ----------------------

        if text == "⬅️ بازگشت":

            bot.send_message(
                message.chat.id,
                "منوی اصلی",
                reply_markup=main_menu()
            )


        elif text == "⬅️ بازگشت به کسب‌وکارها":

            bot.send_message(
                message.chat.id,
                "کسب‌وکارهای لینک",
                reply_markup=business_menu()
            )


        # ----------------------
        # درباره لینک
        # ----------------------

        elif text == "ℹ️ درباره لینک":

            bot.send_message(
                message.chat.id,
                "یکی از گزینه‌های زیر را انتخاب کنید.",
                reply_markup=link_menu()
            )


        elif text == "📖 لینک چیست؟":

            bot.send_message(
                message.chat.id,
                LINK_TEXT,
                reply_markup=link_menu()
            )


        elif text == "⚙️ لینک چگونه کار می‌کند؟":

            bot.send_message(
                message.chat.id,
                WORK_TEXT,
                reply_markup=link_menu()
            )


        elif text == "💰 کسب درآمد با لینک":

            bot.send_message(
                message.chat.id,
                INCOME_TEXT,
                reply_markup=link_menu()
            )
                    # ----------------------
        # کسب‌وکارهای لینک
        # ----------------------

        elif text == "🛍 کسب‌وکارهای لینک":

            bot.send_message(
                message.chat.id,
                "یکی از کسب‌وکارهای زیر را انتخاب کنید.",
                reply_markup=business_menu()
            )

        elif text in BUSINESSES:

            business = BUSINESSES[text]

            last_business[message.chat.id] = text

            caption = business["title"]

            try:
                with open(business["banner"], "rb") as photo:
                    bot.send_photo(
                        message.chat.id,
                        photo,
                        caption=caption
                    )
            except FileNotFoundError:
                bot.send_message(
                    message.chat.id,
                    caption
                )

            business_text = TEXTS[business["text"]]

            bot.send_message(
                message.chat.id,
                business_text,
                reply_markup=business_buttons()
            )
        # ----------------------
        # تماس
        # ----------------------

        elif text == "📞 تماس":

            key = last_business.get(message.chat.id)

            if key:

                bot.send_message(
                    message.chat.id,
                    "☎️ " + BUSINESSES[key]["phone"],
                    reply_markup=business_buttons()
                )


        # ----------------------
        # آدرس
        # ----------------------

        elif text == "📍 آدرس":

            key = last_business.get(message.chat.id)

            if key:

                bot.send_message(
                    message.chat.id,
                    "📍 " + BUSINESSES[key]["address"],
                    reply_markup=business_buttons()
                )


        # ----------------------
        # نمونه‌کارها
        # ----------------------

        elif text == "🖼 نمونه‌کارها":

            key = last_business.get(message.chat.id)

            if key:

                gallery = BUSINESSES[key].get("gallery", [])

                if gallery:

                    for image in gallery:

                        with open(image, "rb") as photo:

                            bot.send_photo(
                                message.chat.id,
                                photo
                            )

                else:

                    bot.send_message(
                        message.chat.id,
                        "هنوز نمونه‌کاری ثبت نشده است.",
                        reply_markup=business_buttons()
                    )


        # ----------------------
        # ارتباط با ما
        # ----------------------

        elif text == "📞 ارتباط با ما":

            bot.send_message(
                message.chat.id,
                CONTACT_TEXT,
                reply_markup=main_menu()
            )


        # ----------------------
        # پیام نامعتبر
        # ----------------------

        else:

            bot.send_message(
                message.chat.id,
                "لطفاً از دکمه‌های منو استفاده کنید.",
                reply_markup=main_menu()
            )