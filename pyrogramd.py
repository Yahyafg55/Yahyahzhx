from pyrogram import Client, filters

bot_token = "6969577050:AAFeNsbUqhXzHMiHpB45f4DTTLWZWWDYhk8"

api_id = 10027276
api_hash = "ce5e8cd00a5bdd3c09c5f1489c4fb858"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

