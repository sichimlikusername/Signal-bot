import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("BTCUSD", callback_data="BTCUSD")]
    ]

    # MUHIM: update.message o‘rniga effective_message
    await update.effective_message.reply_text(
        "Salom 👋\nSizga qaysi para kerak?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "BTCUSD":
        keyboard = [
            [
                InlineKeyboardButton("M1", callback_data="BTCUSD_1"),
                InlineKeyboardButton("M5", callback_data="BTCUSD_5"),
                InlineKeyboardButton("M15", callback_data="BTCUSD_15"),
                InlineKeyboardButton("H1", callback_data="BTCUSD_60"),
            ]
        ]
        await query.edit_message_text(
            "Timeframe tanlang:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    tf = query.data.split("_")[1]
    url = f"https://www.tradingview.com/chart/?symbol=BINANCE:BTCUSDT&interval={tf}"

    # BU YER HAM TO‘G‘RI
    await query.message.reply_text(
        f"📊 BTCUSD | TF: {tf}\nReal vaqtdagi grafik:\n{url}"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.run_polling()
