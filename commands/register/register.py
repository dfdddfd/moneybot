class Command:
    name = '가입'
    no_signin = True

    async def run(self, client, message, ext):
        client.db[str(message.author.id)] = {
            'money': 0,
            'roles': [],
            'stock': {
                
            }
        }
        await message.channel.send('완료했습니다')