class Command:
    name = '탈퇴'

    async def run(self, client, message, ext):
        del client.db.data[str(message.author.id)]
        await message.channel.send('완료했습니다')