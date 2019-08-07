import discord
import random
import random
import time
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
arr = ['3star', '2star', '1star']
rate = [2, 18, 80]#控制機率
img_3star='<:s3tar:576360579644784651>'#discord img
img_2star='<:s2tar:576360578357133343>'
img_1star='<:s1tar:576360195341680648>'

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def 抽卡(ctx,som:str=''):#som為抓 "!抽卡" 後的文字
    card = [None]*10
    for i in range(10):
        prob_card=arr[random_index(rate)]#先給定  避免每次if都是不同的
		
        if prob_card == '3star':#去discord加入三星的表情後，反斜線\+表情按送出，所顯示的那一串 自行更改
            card[i]=img_3star
        elif prob_card == '2star':
            card[i]=img_2star
        elif prob_card == '1star':
            card[i]=img_1star
        else:
            card[i]=img_1star

    if card.count(img_1star)==10:#保底
        for x in range(9,-1,-1):
            if  card[x]==img_1star:
                card[x]=img_2star
                break

    msg=''
    if card.count(img_1star)==9:#保底嘲諷
        if card.count(img_3star)!=1:
            msg='笑死 +19 非洲人4你?'+'<:bla:576508370920407259>'

    if card.count(img_3star)>=1:#抽到彩的恭喜
        msg='太神啦 中了'+str(card.count(img_3star))+'張彩!'+'<:wa:576506556032483329>'

    lol="".join('%s' %id for id in card)
    await ctx.send(str(ctx.message.author)+' > '+lol+msg+'\t'+som)#ctx.message.author獲取discord用戶id

@bot.command()
async def 抽卡機率(ctx):
    await ctx.send( "★3.."+'{:>5}'.format(str(rate[0]))+"%\n"
                    "★2.."+'{:>5}'.format(str(rate[1]))+"%\n"
                    "★1.."+'{:>5}'.format(str(rate[2]))+"%\n")

@bot.command()
async def 加倍(ctx):
    global rate
    rate = [4,18,78]
    await ctx.send('加倍成功')

@bot.command()
async def 取消加倍(ctx):
    global rate
    rate = [2,18,80]
    await ctx.send('取消加倍成功')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="爆射抽卡ㄐ器人 by沒心", description="沒有反應，就只是一個抽卡ㄐ器人，以下是指令", color=0xcc25de)
    embed.add_field(name="!抽卡", value="抽10張卡 有保底", inline=False)
    embed.add_field(name="!抽卡 空格 \'任意文字\' ", value="與抽卡相同，後方輸入的任意文字會回傳", inline=False)
    embed.add_field(name="!抽卡機率", value="顯示當前抽卡機率", inline=False)
    embed.add_field(name="!加倍", value="加倍成三星機率4%", inline=False)
    embed.add_field(name="!取消加倍", value="變成未加倍時的機率2%", inline=False)
    await ctx.send(embed=embed)

def random_index(rate):
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index

bot.run('your discord bot token')#輸入你的discord bot token