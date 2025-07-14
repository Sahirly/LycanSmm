# 🚀 LycanSmm Telegram Bot

A powerful, feature-rich Telegram bot for managing and selling social media marketing (SMM) services like Instagram, YouTube, and Telegram promotions. Built with Python and python-telegram-bot, it supports admin controls, order tracking, payment via UPI QR, and more!

---

## ✨ Features
- 📸 Instagram, ▶️ YouTube, 📲 Telegram SMM services
- 💳 Dynamic UPI QR code payment instructions
- 🧾 Order creation, tracking, and status updates
- 🛠️ Admin panel with order/payment management
- 🔔 Admin notifications for new orders and payments
- 🚫 User ban/unban system
- 📝 User feedback and admin broadcast
- 🔒 Secure with environment variables

---

## 🛠️ Setup & Installation

1. **Clone the repo:**
   ```sh
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
2. **Install dependencies:**
   ```sh
   pip install -r LycanSmm/requirements.txt
   ```
3. **Set your Telegram bot token:**
   ```sh
   export BOT_TOKEN=your-telegram-bot-token
   ```
4. **Run the bot:**
   ```sh
   python3 LycanSmm/bot.py
   ```

---

## ⚙️ Environment Variables
- `BOT_TOKEN` — Your Telegram bot token from [@BotFather](https://t.me/BotFather)

---

## 📦 Usage
- Start the bot on Telegram and use `/start` to see the menu.
- Admins can use `/admin` for the control panel.
- Users can:
  - Place orders for SMM services
  - Get payment instructions and pay via UPI QR
  - Track orders and submit payment screenshots
  - View their order history
- Admins can:
  - View and manage orders
  - Update order/payment status
  - Broadcast messages
  - Ban/unban users
  - Toggle service availability

---

## 🖼️ Dynamic UPI QR Code
- The bot generates a UPI QR code on the fly for payments—no static image needed!

---

## 👤 Credits
- Developed by Vishnu Nishad
- Powered by [python-telegram-bot](https://python-telegram-bot.org/)

---

## 📝 License
MIT License 
