class Command:
    name = '매수'
    use = '매수 [갯수] [주식이름]'

    async def run(self, client, message, ext):
        length = client.get_int_msg(message, ext)
        if not length: return 
        try: stock = str(ext.args[1])
        except: return
        if stock not in client.stock.db: return
        money = client.stock.get(stock) * length
        if money > client.db[str(message.author.id)]['money']: return await message.channel.send('부족')
        client.db[str(message.author.id)]['money'] -= money
        if stock not in client.db[str(message.author.id)]['stock']: client.db[str(message.author.id)]['stock'][stock] = 0
        client.db[str(message.author.id)]['stock'][stock] += length
        await message.channel.send(f'{stock}를 {length}개 구매했어요')
        