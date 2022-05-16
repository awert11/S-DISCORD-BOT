BOT_PREFIX = "-"
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = YOUR CHANNEL ID 

from cgitb import text
import datetime
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    status_w = discord.Status.online
    activity_w = discord.Activity(type=discord.ActivityType.playing, name="✏️| 開發By: Mauna")
    await bot.change_presence(status= status_w, activity=activity_w)
    print("機器人已啟動!!", bot.user.name)
    Channel = bot.get_channel(YOUR CHANNEL ID)
    text = "🙋 各位客官 伺服器現正封測中🙋\n如果想要及時獲得封測更新訊息，請點擊下方表情符號獲得【遊客】身分！"
    Moji = await Channel.send(text)
    await Moji.add_reaction('<:tea1:962055684344655913>')

@bot.event
async def on_member_join(member):
    try:
        channel = bot.get_channel(CHANNEL_ID)
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
        channel = bot.get_channel(CHANNEL_ID)
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
    Channel = bot.get_channel(YOUR CHANNEL ID)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "<:tea1:962055684344655913>":
      Role = discord.utils.get(user.guild.roles, name="EDD")
      await user.add_roles(Role)

@bot.event
async def on_reaction_remove(reaction, user):
    Channel = bot.get_channel(YOUR CHANNEL ID)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "<:tea1:962055684344655913>":
      Role = discord.utils.get(user.guild.roles, name="EDD")
      await user.remove_roles(Role) 

bot.run(BOT_TOKEN)