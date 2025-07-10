import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

# Secure token from Render Environment Variable
TOKEN = os.getenv("BOT_TOKEN")

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("\ud83d\udcf8 Instagram Services", callback_data='instagram')],
        [InlineKeyboardButton("\u25b6\ufe0f YouTube Services", callback_data='youtube')],
        [InlineKeyboardButton("\ud83d\udcf2 Telegram Services", callback_data='telegram')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to LycanSmm! Select a service:", reply_markup=reply_markup)

# Button Handler with Debug Logs
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("\ud83d\udc49 CallbackQueryHandler triggered")  # Debug line
    query = update.callback_query
    await query.answer()

    if query.data == 'instagram':
        keyboard = [
            [InlineKeyboardButton("\u2764\ufe0f Likes - \u20b910 per 1K", callback_data='insta_likes')],
            [InlineKeyboardButton("\ud83d\udc65 Followers - \u20b9100 per 1K", callback_data='insta_followers')],
            [InlineKeyboardButton("\ud83d\udc40 Views - \u20b930 per 100K", callback_data='insta_views')],
            [InlineKeyboardButton("\ud83d\udcc8 Reach - \u20b970 per 1K", callback_data='insta_reach')],
            [InlineKeyboardButton("\ud83d\udc41\ufe0f\u200d\u25b8\ufe0f Story Views - \u20b940 per 1K", callback_data='insta_story')],
            [InlineKeyboardButton("\ud83d\udcac Comments - \u20b9120 per 1K", callback_data='insta_comments')],
            [InlineKeyboardButton("\ud83d\udd04 Shares - \u20b910 per 1K", callback_data='insta_shares')],
            [InlineKeyboardButton("\ud83d\udcbe Saves - \u20b910 per 1K", callback_data='insta_saves')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("\ud83d\udcb8 Pay Here", url="upi://pay?pa=afnansidd110-1@okicici&pn=LycanSMM&am=100&cu=INR")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard + payment_keyboard)
        await query.message.reply_text("Choose Instagram Service with Rates:", reply_markup=reply_markup)

    elif query.data == 'youtube':
        keyboard = [
            [InlineKeyboardButton("\ud83d\udc65 Subscribers - \u20b9150 per 1K", callback_data='yt_subs')],
            [InlineKeyboardButton("\ud83d\udc41\ufe0f Views - \u20b980 per 1K", callback_data='yt_views')],
            [InlineKeyboardButton("\ud83d\udcb0 4k watchtime - \u20b91500", callback_data='yt_monetize')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("\ud83d\udcb8 Pay Here", url="upi://pay?pa=afnansidd110-1@okicici&pn=LycanSMM&am=100&cu=INR")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard + payment_keyboard)
        await query.message.reply_text("Choose YouTube Service with Rates:", reply_markup=reply_markup)

    elif query.data == 'telegram':
        keyboard = [
            [InlineKeyboardButton("\ud83d\udc65 Telegram Members - \u20b9150 per 1K", callback_data='tg_members')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("\ud83d\udcb8 Pay Here", url="upi://pay?pa=afnansidd110-1@okicici&pn=LycanSMM&am=100&cu=INR")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard + payment_keyboard)
        await query.message.reply_text("Choose Telegram Service with Rates:", reply_markup=reply_markup)

    else:
        await query.message.reply_text(f"You selected: {query.data}. Please send the link related to this service after completing the payment.")

# Message Handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(
        f"\u2705 Received your link: {user_message}\n\n\ud83d\udee0 Our team will process your request soon."
    )

# Main
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("\ud83e\udd16 Bot is running...")
    app.run_polling()
