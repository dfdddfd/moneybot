class Command:
    name = '내돈'
    aliases = ['지갑', '돈', '내정보']

    async def run(self, client, message, ext):
        nl = '\n'
        u = client.db[str(ext.first_member.id)]
        sstr = "stock"
        await message.channel.send(f'**돈**\n{u["money"]}원\n\n**주식**\n```\n{nl.join([f"{i} {u[sstr][i]}개" for i in u[sstr]])}\n```')