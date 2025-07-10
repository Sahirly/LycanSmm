import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

# Secure token access
TOKEN = os.getenv("BOT_TOKEN")

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📸 Instagram Services", callback_data='instagram')],
        [InlineKeyboardButton("▶️ YouTube Services", callback_data='youtube')],
        [InlineKeyboardButton("📲 Telegram Services", callback_data='telegram')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to LycanSmm! Select a service:", reply_markup=reply_markup)

# Button Handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'instagram':
        keyboard = [
            [InlineKeyboardButton("❤️ Likes - ₹10 per 1K", callback_data='insta_likes')],
            [InlineKeyboardButton("👥 Followers - ₹100 per 1K", callback_data='insta_followers')],
            [InlineKeyboardButton("👀 Views - ₹30 per 100K", callback_data='insta_views')],
            [InlineKeyboardButton("📈 Reach - ₹70 per 1K", callback_data='insta_reach')],
            [InlineKeyboardButton("👁️‍🗨️ Story Views - ₹40 per 1K", callback_data='insta_story')],
            [InlineKeyboardButton("💬 Comments - ₹120 per 1K", callback_data='insta_comments')],
            [InlineKeyboardButton("🔄 Shares - ₹10 per 1K", callback_data='insta_shares')],
            [InlineKeyboardButton("💾 Saves - ₹10 per 1K", callback_data='insta_saves')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("💸 Pay Here", url="upi://pay?pa=afnansidd110-1@okicici&pn=LycanSMM&am=100&cu=INR")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard + payment_keyboard)
        await query.edit_message_text("Choose Instagram Service with Rates:", reply_markup=reply_markup)

    elif query.data == 'youtube':
        keyboard = [
            [InlineKeyboardButton("👥 Subscribers - ₹150 per 1K", callback_data='yt_subs')],
            [InlineKeyboardButton("👁️ Views - ₹80 per 1K", callback_data='yt_views')],
            [InlineKeyboardButton("💰 4k watchtime - ₹1500", callback_data='yt_monetize')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("💸 Pay Here", url="upi://pay?pa=afnansidd110-1@okicici&pn=LycanSMM&am=100&cu=INR")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard + payment_keyboard)
        await query.edit_message_text("Choose YouTube Service with Rates:", reply_markup=reply_markup)

    elif query.data == 'telegram':
        keyboard = [
            [InlineKeyboardButton("👥 Telegram Members - ₹150 per 1K", callback_data='tg_members')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("💸 Pay Here", url="upi://pay?pa=afnansidd110-1@okicici&pn=LycanSMM&am=100&cu=INR")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard + payment_keyboard)
        await query.edit_message_text("Choose Telegram Service with Rates:", reply_markup=reply_markup)

    else:
        await query.edit_message_text(f"You selected: {query.data}.\nPlease send the link related to this service after completing the payment.")

# Message Handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(
        f"✅ Received your link: {user_message}\n\n🛠 Our team will process your request soon."
    )

# Main Function
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()
