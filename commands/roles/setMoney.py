class Command:
    name = '돈설정'
    aliases = ['돈셋']
    use = '돈설정 [돈양] [유저]'

    need_role = 'set_money'

    async def run(self, client, message, ext):
        user = ext.first_member
        if str(user.id) not in client.db: return
        money = client.get_int_msg(message, ext)
        if not money: return 
        client.db[str(user.id)]['money'] = money
        await message.channel.send(f'{user.mention}님의 돈을 {money}로 설정했어요!')
        