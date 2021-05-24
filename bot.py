import discord
bot=discord.Client()
chat=bot.get_channel(843116355947331635)
@bot.event
async def on_ready():
    chat=bot.get_channel(843116355947331635)
    await chat.send("hello! this is testbot")
@bot.event
async def on_message(message):
    if(message.content=="whats your name"):
        chat=bot.get_channel(843116355947331635)
        await chat.send("yo adi my name is bot")
    if(message.content=="YO"):
        chat=bot.get_channel(843116355947331635)
        await chat.send("yo man")
bot.run(token)
