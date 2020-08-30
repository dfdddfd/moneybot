class Command:
    name = 'hellothisisverification'

    async def run(self, client, message, ext):
        await message.channel.send('코드 사용자#태그(ID)')
