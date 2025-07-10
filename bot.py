import os
from datetime import datetime
from functools import wraps
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

# Secure token from Render Environment Variable
TOKEN = os.getenv("BOT_TOKEN")

# Admin list
ADMINS = [123456789, 7432801922]  # Replace with your Telegram user IDs

# In-memory order tracking
orders_log = []

# Admin-only access decorator
def restricted_to_admins(func):
    @wraps(func)
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in ADMINS:
            return await update.message.reply_text("🚫 This command is only for admins.")
        return await func(update, context, *args, **kwargs)
    return wrapped

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

# Admin Panel Command
@restricted_to_admins
async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 View Recent Orders", callback_data='admin_view_orders')],
        [InlineKeyboardButton("✅ Confirm Order", switch_inline_query_current_chat="Confirm Order: LYC")],
        [InlineKeyboardButton("❌ Reject Order", switch_inline_query_current_chat="Reject Order: LYC")],
        [InlineKeyboardButton("💰 Check Payments", callback_data='admin_check_payments')],
    ]
    await update.message.reply_text("🛠️ *Admin Control Panel*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# Button Handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    order_id = generate_order_id()
    user_id = query.from_user.id
    username = query.from_user.username or query.from_user.first_name

    if query.data == 'instagram':
        orders_log.append((order_id, user_id, 'Instagram'))
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
        payment_keyboard = [[InlineKeyboardButton("💳 Payment Instructions", callback_data='payment_info')]]
        await query.message.reply_text(
            f"Choose Instagram Service with Rates:\n\n🆔 Order ID: #{order_id}\nProcessing starts instantly.\nTotal delivery time: 5–10 minutes.\n\n💼 Once our team is online, your request will be accepted and delivered shortly.",
            reply_markup=InlineKeyboardMarkup(keyboard + payment_keyboard)
        )

    elif query.data == 'youtube':
        orders_log.append((order_id, user_id, 'YouTube'))
        keyboard = [
            [InlineKeyboardButton("👥 Subscribers - ₹150 per 1K", callback_data='yt_subs')],
            [InlineKeyboardButton("👁️ Views - ₹80 per 1K", callback_data='yt_views')],
            [InlineKeyboardButton("💰 4k watchtime - ₹1500", callback_data='yt_monetize')],
        ]
        payment_keyboard = [[InlineKeyboardButton("💳 Payment Instructions", callback_data='payment_info')]]
        await query.message.reply_text(
            f"Choose YouTube Service with Rates:\n\n🆔 Order ID: #{order_id}\nProcessing starts instantly.\nTotal delivery time: 30–60 minutes.\n\n💼 Once our team is online, your request will be accepted and executed as per queue.",
            reply_markup=InlineKeyboardMarkup(keyboard + payment_keyboard)
        )

    elif query.data == 'telegram':
        orders_log.append((order_id, user_id, 'Telegram'))
        keyboard = [[InlineKeyboardButton("👥 Telegram Members - ₹150 per 1K", callback_data='tg_members')]]
        payment_keyboard = [[InlineKeyboardButton("💳 Payment Instructions", callback_data='payment_info')]]
        await query.message.reply_text(
            f"Choose Telegram Service with Rates:\n\n🆔 Order ID: #{order_id}\nProcessing starts instantly.\nTotal delivery time: 5–10 minutes.\n\n💼 Once our team is online, your request will be accepted and pushed for delivery.",
            reply_markup=InlineKeyboardMarkup(keyboard + payment_keyboard)
        )

    elif query.data == 'payment_info':
        await query.message.reply_photo(
            photo=open("paytm_qr.png", "rb"),
            caption=(
                "💸 *How to Pay:*\n\n"
                "Scan the QR code above or use any UPI app (PhonePe, GPay, Paytm):\n"
                "`afnansidd110-1@okicici`\n"
                "Amount: As per your selected service.\n\n"
                "📤 After payment, reply with screenshot or click below."
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📤 Submit Payment Screenshot", switch_inline_query_current_chat="Payment Screenshot: ")]
            ]),
            parse_mode="Markdown"
        )

    elif query.data == 'faq':
        await query.message.reply_text(
            "📖 *FAQs:*\n"
            "1. Delivery Time? → Usually 5–60 mins\n"
            "2. Is it Safe? → Yes, via organic/non-drop\n"
            "3. Will it drop? → <5% drop possible\n"
            "4. Support Time? → 10AM to 11PM IST",
            parse_mode="Markdown"
        )

    elif query.data == 'track':
        await query.message.reply_text(
            "📦 *Track Order:*\nReply with your Order ID (e.g. `LYC240710153045`) to get the latest status.",
            parse_mode="Markdown"
        )

    elif query.data == 'admin_view_orders':
        if orders_log:
            orders_text = "\n".join([f"{oid} - {typ} - @{uid}" for oid, uid, typ in orders_log[-5:]])
            await query.message.reply_text(f"🧾 Last 5 Orders:\n{orders_text}")
        else:
            await query.message.reply_text("🧾 No orders yet.")

    elif query.data == 'admin_check_payments':
        await query.message.reply_text("💰 Payment Screenshot Summary:\nPlease verify manually in chat/gallery.")

    else:
        await query.message.reply_text(f"You selected: {query.data}. Please send your link after payment.")

# Message Handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    if user_message.upper().startswith("LYC"):
        await update.message.reply_text(
            f"🔎 Tracking Order ID: {user_message}\nStatus: In queue / Processing.\nYou'll get a confirmation shortly."
        )
    elif user_message.lower().startswith("payment screenshot") or update.message.photo:
        await update.message.reply_text("📩 Screenshot received. Our team will verify and confirm soon.")
    else:
        await update.message.reply_text(
            f"✅ Link received: {user_message}\nOur team will process shortly."
        )

# Main
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin_panel))
    app.add_handler(CallbackQueryHandler(button, pattern=".*"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_message))
    print("Bot is running...")
    app.run_polling()
