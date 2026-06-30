from telebot import types
from data.businesses import BUSINESSES


# =========================
# منوی اصلی
# =========================

def main_menu():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("ℹ️ درباره لینک")

    markup.row("🛍 کسب‌وکارهای لینک")

    markup.row("📞 ارتباط با ما")

    return markup


# =========================
# منوی درباره لینک
# =========================

def link_menu():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("📖 لینک چیست؟")

    markup.row("⚙️ لینک چگونه کار می‌کند؟")

    markup.row("💰 کسب درآمد با لینک")

    markup.row("⬅️ بازگشت")

    return markup


# =========================
# منوی کسب‌وکارها
# =========================

def business_menu():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for business in BUSINESSES.keys():

        markup.row(business)

    markup.row("⬅️ بازگشت")

    return markup


# =========================
# دکمه‌های صفحه کسب‌وکار
# =========================

def business_buttons():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("🖼 نمونه‌کارها")

    markup.row("📞 تماس", "📍 آدرس")

    markup.row("⬅️ بازگشت به کسب‌وکارها")

    return markup