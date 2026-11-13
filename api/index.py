from flask import Flask, request, jsonify
import os
import asyncio
from telegram import Bot

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL = "@mshsheen71"
bot = Bot(token=TOKEN)

async def handle_message(msg):
    text = msg.get("text") or msg.get("caption") or ""
    if not text:
        return
    chat_id = msg["chat"]["id"]
    clean = f"مناقصة جديدة\n{text}\n----------------\nالمصدر: @mshsheen71"
    await bot.send_message(chat_id=CHANNEL, text=clean)
    await bot.send_message(chat_id=chat_id, text="تم الاستلام ✅")

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(force=True, silent=True) or {}
    msg = data.get("message")
    if msg:
        asyncio.run(handle_message(msg))
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run()
