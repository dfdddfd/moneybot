class Command:
    name = '내돈'
    aliases = ['지갑', '돈', '내정보']

    async def run(self, client, message, ext):
        if str(ext.first_member.id) not in client.db: return
        await message.channel.send(f'{client.db[str(ext.first_member.id)]["money"]}원')