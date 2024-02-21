from pyrogram import Client, filters

bot_token = "7060710135:AAGt7i_0cP4fP1rAerCksVtBoW_vPVsBRZk"

api_id = 28902527
api_hash = "b7792e9f5adb7fae0566aaf247030b4b"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

