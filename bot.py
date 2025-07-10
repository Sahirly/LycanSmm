import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

# Secure token from Render Environment Variable
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

# Button Handler with Debug Logs
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("👉 CallbackQueryHandler triggered")  # Debug line
    query = update.callback_query
    await query.answer()

    if query.data == 'instagram':
        keyboard = [
            [InlineKeyboardButton("❤️ Likes - ₹10 per 1K", callback_data='insta_likes')],
            [InlineKeyboardButton("👥 Followers - ₹100 per 1K", callback_data='insta_followers')],
            [InlineKeyboardButton("👀 Views - ₹30 per 100K", callback_data='insta_views')],
            [InlineKeyboardButton("📈 Reach - ₹70 per 1K", callback_data='insta_reach')],
            [InlineKeyboardButton("👁‍🗨 Story Views - ₹40 per 1K", callback_data='insta_story')],
            [InlineKeyboardButton("💬 Comments - ₹120 per 1K", callback_data='insta_comments')],
            [InlineKeyboardButton("🔄 Shares - ₹10 per 1K", callback_data='insta_shares')],
            [InlineKeyboardButton("💾 Saves - ₹10 per 1K", callback_data='insta_saves')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("💳 Payment Instructions", callback_data='payment_info')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard + payment_keyboard)
        await query.message.reply_text("Choose Instagram Service with Rates:", reply_markup=reply_markup)

    elif query.data == 'youtube':
        keyboard = [
            [InlineKeyboardButton("👥 Subscribers - ₹150 per 1K", callback_data='yt_subs')],
            [InlineKeyboardButton("👁️ Views - ₹80 per 1K", callback_data='yt_views')],
            [InlineKeyboardButton("💰 4k watchtime - ₹1500", callback_data='yt_monetize')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("💳 Payment Instructions", callback_data='payment_info')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard + payment_keyboard)
        await query.message.reply_text("Choose YouTube Service with Rates:", reply_markup=reply_markup)

    elif query.data == 'telegram':
        keyboard = [
            [InlineKeyboardButton("👥 Telegram Members - ₹150 per 1K", callback_data='tg_members')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("💳 Payment Instructions", callback_data='payment_info')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard + payment_keyboard)
        await query.message.reply_text("Choose Telegram Service with Rates:", reply_markup=reply_markup)

    elif query.data == 'payment_info':
        await query.message.reply_text(
            "💸 *How to Pay:*\n\nUse any UPI app (PhonePe, GPay, Paytm) and send payment to:\n`afnansidd110-1@okicici`\nAmount: As per your service selection\nAfter payment, send the screenshot and your post link here.\n\n✅ Our team will verify and process your request.",
            parse_mode="Markdown"
        )

    else:
        await query.message.reply_text(f"You selected: {query.data}. Please send the link related to this service after completing the payment.")

# Message Handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(
        f"✅ Received your link: {user_message}\n\n🛠️ Our team will process your request soon."
    )

# Main
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button, pattern=".*"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
