from pyrogram import Client, filters

bot = Client("my_account",
            api_id = 1072589,
            api_hash = "5b1fa7e368f8d838d8abcaec822fb69e"
            )


@bot.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")


bot.run()
