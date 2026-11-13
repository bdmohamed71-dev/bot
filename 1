from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os
TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL = "@mshsheen71"
async def forward_tender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    text = msg.text or msg.caption or ""
    if not text:
        return
    clean = f"📢 مناقصة جديدة | مكة - جدة\n\n{text}\n\n━━━━━━━━━━\n📍 للتقديم: تابع منصة المناقصات\n🔗 @mshsheen71\n#مناقصات_مكة #مناقصات_جدة"
    await context.bot.send_message(chat_id=CHANNEL, text=clean)
    await msg.reply_text("✅ اتنشرت في القناة بنجاح!")
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, forward_tender))
    app.run_polling()
