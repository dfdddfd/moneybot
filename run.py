from extension.bot import MoneyBot
from asyncio import gather
bot = MoneyBot()

@bot.event
async def on_ready(): 
    print('Bot Ready')
    await gather(
        bot.stock.update_loop('google'),
        bot.stock.update_loop('naver'),
        bot.stock.update_loop('daum')
    )
    
@bot.event
async def on_message(message): await bot.use_cmd(message)

bot.run_bot()