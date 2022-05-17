BOT_PREFIX = "-"

import asyncio
from cgitb import text
import datetime
from socket import AI_ADDRCONFIG
import discord
from discord.ext import commands
import json 
from discord.ext.commands import MissingPermissions

with open("setting.json", "r", encoding="utF8") as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    status_w = discord.Status.online
    activity_w = discord.Activity(type=discord.ActivityType.playing, name="✏️| 開發By: Mauna")
    await bot.change_presence(status= status_w, activity=activity_w)
    print("機器人已啟動!!", bot.user.name)
    Channel = bot.get_channel(int(jdata["GIVE_ROLE_CHANNEL"]))
    text = "🙋 各位客官 伺服器現正封測中🙋\n如果想要及時獲得封測更新訊息，請點擊下方表情符號獲得【遊客】身分！"
    Moji = await Channel.send(text)
    await Moji.add_reaction('🏃')

@bot.event
async def on_member_join(member):
    try:
        channel = bot.get_channel(int(jdata["WELCOME_CHANNEL_ID"]))
        try:
            embed = discord.Embed(colour=discord.Colour.from_rgb(204, 255, 229))
            embed.set_author(name=member, icon_url=member.avatar_url)
            embed.add_field(name=":loudspeaker: __歡迎加入星魂秋夢|Minecraft伺服器__ :loudspeaker:" ,value=f"\u200B\n讓我們一起見證【星魂秋夢】的成長\n\u200B", inline=False)
            embed.add_field(name=":mag: Discord永久連結" ,value=f"\u200B\n連結 ➽ https://discord.gg/Yeqa6VRbMG\n\u200B", inline=False)
            embed.add_field(name=":speech_balloon: 伺服器簡介" ,value=f"\u200B\n伺服器為生存RPG、有天賦、技能、特殊物品\n抽獎、稱號等等多種有趣系統生存\n資源界與生存界、資源界會定期洗白!", inline=False)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/482941525764997120/975448860199649330/logo.png?width=906&height=906")
            embed.set_image(url="https://media.discordapp.net/attachments/482941525764997120/975450790867120148/350kb_1.gif")
            time = datetime.datetime.now().replace(microsecond=0)
            embed.set_footer(text=F"by 小安Mauan • {time}", icon_url = "https://media.discordapp.net/attachments/970840936789708820/975567403641606154/c533eb6c-aa49-4450-b203-36b0bd920f3a.jpg")
            await channel.send(embed=embed)
            await member.send(F"你好，歡迎 `{member}` 的加入\n【星魂秋夢】－ Minecraft正版伺服器\n==========================\n有任何問題都可以向工作人員詢問。\n🔔目前伺服器仍在建設中🔔\n🔔伺服器將於5月初刪檔封測，🔔\n🔔並於6月底正式開放伺服器🔔\n=========================")
        except Exception as e:
            raise e
    except Exception as e:
        raise e

@bot.event
async def on_member_remove(member):
    try:
        channel = bot.get_channel(int(jdata["LEAVE_CHANNEL_ID"]))
        try:
            embed = discord.Embed(colour=discord.Colour.from_rgb(255, 204, 255))
            embed.set_author(name=member, icon_url=member.avatar_url)
            embed.add_field(name=":eyes: __玩家離開通知__ :eyes:", value=f"喔不... {member.mention} 離我們而去了QQ", inline=False)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/482941525764997120/975454144078970900/unknown.png")
            time = datetime.datetime.now().replace(microsecond=0)
            embed.set_footer(text=F"by 小安Mauan • {time}", icon_url = "https://media.discordapp.net/attachments/970840936789708820/975567403641606154/c533eb6c-aa49-4450-b203-36b0bd920f3a.jpg")
            await channel.send(embed=embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e

@bot.event
async def on_reaction_add(reaction, user):
    Channel = bot.get_channel(int(jdata["GIVE_ROLE_CHANNEL"]))
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "🏃":
      Role = discord.utils.get(user.guild.roles, name="YOU_ROLE_NAME")
      await user.add_roles(Role)

@bot.event
async def on_reaction_remove(reaction, user):
    Channel = bot.get_channel(int(jdata["GIVE_ROLE_CHANNEL"]))
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "🏃":
      Role = discord.utils.get(user.guild.roles, name="YOU_ROLE_NAME")
      await user.remove_roles(Role) 

@bot.command()
@commands.has_permissions(manage_messages=True)
async def sayd(ctx, *,msg):
    await ctx.message.delete()
    await ctx.send(msg)

@sayd.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
       np = "【沫】:你沒有權限這樣做!"
       await ctx.message.delete()
       await ctx.channel.send(np, delete_after=3.0)

@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    authors = {}
    async for message in ctx.channel.history(limit=amount + 1):
        if message.author not in authors:
            authors[message.author] = 1
        else:
            authors[message.author] += 1
        await message.delete()

    msg = "\n".join([f"已經刪除了 `{author}` 說的 `{amount}` 句話" for author,
                     amount in authors.items()])
    await ctx.channel.send(msg, delete_after=5.0)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
       np = "【沫】:你沒有權限這樣做!"
       await ctx.message.delete()
       await ctx.channel.send(np, delete_after=3.0)
       
@bot.command()
async def CTM(ctx):
    guild = ctx.guild
    await ctx.send(f"群組成員數量: {guild.member_count}") 

@bot.command()
async def userinfo(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author      
    date_format = "%Y %b %d %I:%M %p"
    embed = discord.Embed(title="查詢指令為 -user @用戶 (請勿用以騷擾玩家)", color=0x7ce4fe)
    embed.set_author(name="用戶資料查詢工具", icon_url="https://media.discordapp.net/attachments/970840936789708820/975805407262015598/stsmall507x507-pad600x600f8f8f8.u2.jpg")
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="\u200B", value=f"\u200B")
    embed.add_field(name="\u200B", value=f"\u200B")
    embed.add_field(name="\u200B", value=f"\u200B")
    embed.add_field(name="用戶名", value=user.mention)
    embed.add_field(name="加入日期", value=user.joined_at.strftime(date_format))
    embed.add_field(name="創建日期", value=user.created_at.strftime(date_format))
    embed.add_field(name="\u200B", value=f"\u200B")
    embed.add_field(name="\u200B", value=f"\u200B")
    embed.add_field(name="\u200B", value=f"\u200B")
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="身分組 [{}]".format(len(user.roles)-1), value=role_string)
    embed.add_field(name="用戶ID", value=user.id)
    embed.add_field(name="群組用戶總數", value=f"{ctx.guild.member_count}")
    embed.add_field(name="\u200B", value=f"\u200B")
    embed.add_field(name="\u200B", value=f"\u200B")
    embed.add_field(name="\u200B", value=f"\u200B")
    time = datetime.datetime.now().replace(microsecond=0)
    embed.set_footer(text=F"✏️| 開發By Mauna • {time}", icon_url = "https://media.discordapp.net/attachments/970840936789708820/975567403641606154/c533eb6c-aa49-4450-b203-36b0bd920f3a.jpg")
    return await ctx.send(embed=embed)

bot.run(jdata["BOT_TOKEN"])