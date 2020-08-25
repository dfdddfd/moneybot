from kiki_random import percent

class Command:
    name = '도박'
    cooltime = 60

    async def run(self, client, message, ext):
        money = client.get_int_msg(message, ext)
        if not money: return 
        if money > client.db[str(message.author.id)]['money']: return await message.channel.send('부족')
        res = percent(50)
        if res: client.db[str(message.author.id)]['money'] += money
        else: client.db[str(message.author.id)]['money'] -= money
        await message.channel.send(f'{"성공" if res else "실폐"}해서 {money}원을 {"얻" if res else "잃"}었습니다')