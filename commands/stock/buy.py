class Command:
    name = '매도'
    use = '매도 [갯수] [주식이름]'

    async def run(self, client, message, ext):
        length = client.get_int_msg(message, ext)
        if not length: return 
        try: stock = str(ext.args[1])
        except: return
        if stock not in client.stock.db: return
        if stock not in client.db[str(message.author.id)]['stock']: return
        if length > client.db[str(message.author.id)]['stock'][stock]: return await message.channel.send('부족')
        client.db[str(message.author.id)]['money'] += client.stock.get(stock) * length
        client.db[str(message.author.id)]['stock'][stock] -= length
        await message.channel.send(f'{stock}를 {length}개 판매했어요')
        