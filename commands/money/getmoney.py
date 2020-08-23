class Command:
    name = '돈받기'
    cooltime = 60

    async def run(self, client, message, ext):
        client.db[str(message.author.id)]['money'] += 100
        await message.channel.send('100을 받으셨습니다')