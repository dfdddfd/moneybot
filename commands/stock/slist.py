class Command:
    name = '주식'
    
    async def run(self, client, message, ext):
        nl = '\n'
        await message.channel.send(f'**주식 목록**\n```\n{nl.join([f"{i} - {client.stock.get(i)}원" for i in client.stock.db])}\n```')