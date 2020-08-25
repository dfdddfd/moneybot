class Command:
    name = '송금'
    use = '송금 [돈양] [유저]'

    async def run(self, client, message, ext):
        user = ext.first_member
        if str(user.id) not in client.db: return
        money = client.get_int_msg(message, ext)
        if not money: return 
        if money > client.db[str(message.author.id)]['money']: return await message.channel.send('부족')
        client.db[str(user.id)]['money'] += money
        client.db[str(message.author.id)]['money'] -= money
        await message.channel.send(f'{user.mention}님에게 {money}원을 보냈어요!')
        