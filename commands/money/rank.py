from discord import Embed

class Command:
    name = '랭킹'
    aliases = ['순위']

    async def run(self, client, message, ext):
        r = []
        u = []
        for m in message.guild.members:
            if str(m.id) not in client.db: continue
            u.append([m.name, client.db[str(m.id)]['money']])
        u = list(reversed(sorted(u, key = lambda x: x[1])))
        a = 1
        for i in u:
            r.append(f'**{a}.** `{i[0]}` **- {i[1]}원**')
            a += 1

        await message.channel.send(embed = Embed(title = f'{message.guild.name} 랭킹', description = '\n'.join(r)))