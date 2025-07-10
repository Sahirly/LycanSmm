import os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

# Secure token from Render Environment Variable
TOKEN = os.getenv("BOT_TOKEN")

# Generate a unique order ID
def generate_order_id():
    return f"LYC{datetime.now().strftime('%y%m%d%H%M%S')}"

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📸 Instagram Services", callback_data='instagram')],
        [InlineKeyboardButton("▶️ YouTube Services", callback_data='youtube')],
        [InlineKeyboardButton("📲 Telegram Services", callback_data='telegram')],
        [InlineKeyboardButton("📖 FAQs", callback_data='faq')],
        [InlineKeyboardButton("📦 Track My Order", callback_data='track')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to LycanSmm! Select a service:", reply_markup=reply_markup)

# Button Handler with Debug Logs
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("👉 CallbackQueryHandler triggered")
    query = update.callback_query
    await query.answer()

    order_id = generate_order_id()

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
        await query.message.reply_text(
            f"Choose Instagram Service with Rates:\n\n🆔 Order ID: #{order_id}\nProcessing starts instantly.\nTotal delivery time: 5–10 minutes.\n\n💼 Once our team is online, your request will be accepted and delivered shortly. Thank you for your business mindset and trust!",
            reply_markup=InlineKeyboardMarkup(keyboard + payment_keyboard)
        )

    elif query.data == 'youtube':
        keyboard = [
            [InlineKeyboardButton("👥 Subscribers - ₹150 per 1K", callback_data='yt_subs')],
            [InlineKeyboardButton("👁️ Views - ₹80 per 1K", callback_data='yt_views')],
            [InlineKeyboardButton("💰 4k watchtime - ₹1500", callback_data='yt_monetize')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("💳 Payment Instructions", callback_data='payment_info')]
        ]
        await query.message.reply_text(
            f"Choose YouTube Service with Rates:\n\n🆔 Order ID: #{order_id}\nProcessing starts instantly.\nTotal delivery time: 30–60 minutes.\n\n💼 Once our team is online, your request will be accepted and executed as per queue. Stay assured!",
            reply_markup=InlineKeyboardMarkup(keyboard + payment_keyboard)
        )

    elif query.data == 'telegram':
        keyboard = [
            [InlineKeyboardButton("👥 Telegram Members - ₹150 per 1K", callback_data='tg_members')],
        ]
        payment_keyboard = [
            [InlineKeyboardButton("💳 Payment Instructions", callback_data='payment_info')]
        ]
        await query.message.reply_text(
            f"Choose Telegram Service with Rates:\n\n🆔 Order ID: #{order_id}\nProcessing starts instantly.\nTotal delivery time: 5–10 minutes.\n\n💼 Once our team is online, your request will be accepted and pushed for delivery soon. Appreciate your patience!",
            reply_markup=InlineKeyboardMarkup(keyboard + payment_keyboard)
        )

    elif query.data == 'payment_info':
        await query.message.reply_photo(
            photo=open("paytm_qr.png", "rb"),
            caption=(
                "💸 *How to Pay:*\n\n"
                "Scan the QR code above or use any UPI app (PhonePe, GPay, Paytm) and send payment to:\n"
                "`afnansidd110-1@okicici`\n"
                "Amount: As per your service selection\n"
                "After payment, send the screenshot and your post link here.\n\n"
                "✅ Our team will verify and process your request."
            ),
            parse_mode="Markdown"
        )

    elif query.data == 'faq':
        await query.message.reply_text(
            "📖 *Frequently Asked Questions:*\n"
            "1. *How long does delivery take?*\nUsually within 5–60 minutes depending on the service.\n"
            "2. *Are these services safe?*\nYes, we deliver via non-drop & organic promotion techniques.\n"
            "3. *Will followers/views drop?*\nWe ensure stable growth but a <5% drop can naturally occur.\n"
            "4. *Is there support?*\nAbsolutely! We're here 10AM–11PM daily to assist you.",
            parse_mode="Markdown"
        )

    elif query.data == 'track':
        await query.message.reply_text(
            "📦 *Track My Order:*\n"
            "Please reply with your Order ID (e.g., `LYC240710153045`) so we can update you on your status.",
            parse_mode="Markdown"
        )

    else:
        await query.message.reply_text(f"You selected: {query.data}. Please send the link related to this service after completing the payment.")

# Message Handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    if user_message.upper().startswith("LYC"):
        await update.message.reply_text(
            f"🔎 Tracking Order ID: {user_message}\n\n⏳ Status: In queue / Processing.\n✅ You'll receive confirmation as soon as it's live."
        )
    else:
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
