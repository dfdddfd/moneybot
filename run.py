from extension.bot import MoneyBot
bot = MoneyBot()

@bot.event
async def on_ready(): print('Bot Ready')

@bot.event
async def on_message(message): await bot.use_cmd(message)

bot.run_bot()