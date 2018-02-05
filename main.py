import discord
from discord import Webhook, AsyncWebhookAdapter
import random
import KEYS
import sqlite3
import aiohttp
import json
import time
import asyncio

conn = sqlite3.connect("daten.db")
cur = conn.cursor()

global version
version = "2.0 ALPHA"

global gamestatus
# gamestatus = "!help @Logit | TheBotDev"
gamestatus = "!help - V 2.0 ALPHA"



class MyClient(discord.Client):
    async def on_ready(self):
        game = discord.Game(name=gamestatus)
        await client.change_presence(status=discord.Status.online, game=game)
        global clientname
        clientname = "test-bot"
        cur.execute("CREATE TABLE IF NOT EXISTS server_settings (gid INTEGER, prefix TEXT)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS premium_user (username TEXT, userid INTEGER, key INTEGER, server INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS premium (servername TEXT, serverid INTEGER, key INTEGER, status TEXT)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS server_logs(gid INTEGER, a1 INTEGER, a2 INTEGER, a3 INTEGER, a4 INTEGER, a5 INTEGER, a6 INTEGER, a7 INTEGER, a8 INTEGER, a9 INTEGER, a10 INTEGER, a11 INTEGER, a12 INTEGER, a13 INTEGER, a14 INTEGER, a15 INTEGER, a16 INTEGER, a17 INTEGER, a18 INTEGER, a19 INTEGER, a31 INTEGER, a32 INTEGER, a33 INTEGER, a34 INTEGER, activated TEXT, channelid INTEGER, owner INTEGER)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS server_game_settings (activated INTEGER, channel INTEGER, guildid INTEGER)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS server_game_accounts (userid INTEGER, money INTEGER, banned INTEGER, serverid INTEGER)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS support (channel INTEGER, messageUser TEXT, message TEXT, server INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS webhook (server INTEGER, url TEXT)")
        # cur.execute("CREATE TABLE IF NOT EXISTS levels (gid INTEGER, lvl10 INTEGER, lvl5 INTEGER, lvl10 INTEGER, lvl15 INTEGER, lvl20 INTEGER, lvl25 INTEGER, lvl30, lvl50 INTEGER, lvl100 INTEGER)")
        # cur.execute("CREATE TABLE IF NOT EXISTS level_user (gid INTEGER, aktlvl INTEGER, aktxp INTEGER)")

        print("Erfolgreich eingeloggt!\n")
        print("""================\n""")
	# Get emojis for the Setup and for the games
        emojilist = client.get_guild(394139572260438020)
        emojilist2 = client.get_guild(398121407847989248)
        basechip = client.get_user(333220752117596160)
        counter = 0
        counter2 = 0
        for emojis in emojilist2.emojis:
            if counter2 == 0:
                global moneyicon
                moneyicon = client.get_emoji(emojis.id)
            if counter2 == 1:
                global n1
                n1 = client.get_emoji(emojis.id)
            elif counter2 == 2:
                global n2
                n2 = client.get_emoji(emojis.id)
            elif counter2 == 3:
                global n3
                n3 = client.get_emoji(emojis.id)
            elif counter2 == 4:
                global n4
                n4 = client.get_emoji(emojis.id)
            elif counter2 == 5:
                global n5
                n5 = client.get_emoji(emojis.id)
            elif counter2 == 6:
                global premium
                premium = client.get_emoji(emojis.id)
            elif counter2 == 7:
                global horse
                horse = client.get_emoji(emojis.id)
            counter2 = counter2 + 1
        for emoji in emojilist.emojis:
            if counter == 0:
                global z10
                z10 = client.get_emoji(emoji.id)
            elif counter == 1:
                global z11
                z11 = client.get_emoji(emoji.id)
            elif counter == 2:
                global z12
                z12 = client.get_emoji(emoji.id)
            elif counter == 3:
                global z13
                z13 = client.get_emoji(emoji.id)
            elif counter == 4:
                global z14
                z14 = client.get_emoji(emoji.id)
            elif counter == 5:
                global z15
                z15 = client.get_emoji(emoji.id)
            elif counter == 6:
                global z16
                z16 = client.get_emoji(emoji.id)
            elif counter == 7:
                global z17
                z17 = client.get_emoji(emoji.id)
            elif counter == 8:
                global z18
                z18 = client.get_emoji(emoji.id)
            elif counter == 9:
                global z19
                z19 = client.get_emoji(emoji.id)
            elif counter == 10:
                global z1
                z1 = client.get_emoji(emoji.id)
            elif counter == 11:
                global z2
                z2 = client.get_emoji(emoji.id)
            elif counter == 12:
                global z3
                z3 = client.get_emoji(emoji.id)
            elif counter == 13:
                global z4
                z4 = client.get_emoji(emoji.id)
            elif counter == 14:
                global z5
                z5 = client.get_emoji(emoji.id)
            elif counter == 15:
                global z6
                z6 = client.get_emoji(emoji.id)
            elif counter == 16:
                global z7
                z7 = client.get_emoji(emoji.id)
            elif counter == 17:
                global z8
                z8 = client.get_emoji(emoji.id)
            elif counter == 18:
                global z9
                z9 = client.get_emoji(emoji.id)
            elif counter == 19:
                global hype
                hype = client.get_emoji(emoji.id)
            elif counter == 20:
                global off
                off = client.get_emoji
            elif counter == 21:
                global on
                on = client.get_emoji

            elif counter == 22:
                global z210
                z210 = client.get_emoji
            elif counter == 23:
                global z215
                z215 = client.get_emoji
            elif counter == 24:
                global z20
                z20 = client.get_emoji
            elif counter == 25:
                global z25
                z25 = client.get_emoji
            elif counter == 26:
                global z30
                z30 = client.get_emoji
            elif counter == 27:
                global z50
                z50 = client.get_emoji

            counter = counter + 1

    async def on_message(self, message):
        guild = message.guild.id
        cur.execute("SELECT prefix FROM server_settings WHERE gid=?", (guild,))
        global prefix
        prefix = cur.fetchone()[0]
        inleng = len(prefix)
        cur.execute("SELECT status FROM premium WHERE serverid=?", (message.guild.id,))
        global statuspremium
        statuspremium = cur.fetchall()
        # Generell STAFF
        if message.content.startswith(prefix):
            invoke = message.content[inleng:].split(" ")[0]
            if invoke == "ping":
                await message.channel.send(content="Pong!")
            if invoke == "update":
                cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (message.guild.id,))
                loexi = cur.fetchall()
                print(loexi)
                if str(loexi) != "[(None,)]":
                    cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (message.guild.id,))
                    log = cur.fetchone()[0]
                    print(log)
                    cur.execute("SELECT server FROM webhook WHERE server=?", (message.guild.id,))
                    webhshex = cur.fetchall()
                    if str(webhshex) == "[]":
                        try:
                            webh = await log.create_webhook(name="Logit")
                            cur.execute("INSERT INTO webhook (server, url) VALUES (?,?)", (message.guild.id, webh.url))
                            conn.commit()
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(webh.url, adapter=AsyncWebhookAdapter(session))
                                await webhook.send(username='Logit',
                                                   avatar_url="https://cdn.discordapp.com/app-icons/398933329862328330/e33eff5bb64f94c2d013bc9e6de01393.png",
                                                   embed=discord.Embed(color=discord.Color.green(),
                                                                       description="Es funktioniert"))

                        except discord.errors.Forbidden:
                            await message.channel.send(
                                content="Das Setup wurde abgebrochen! Leider habe ich nicht die Permission um einen WebHook zu erstellen (WebHooks verwalten), aber das ist sehr wichtig für diese Funktion!")
            if invoke == "replace":
                def c(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m

                await message.channel.send(content="Sende mir den Text")
                temp = await client.wait_for("message", check=c, timeout=None)
                message1 = (temp.content).replace("n11", str(z11))
                message2 = (message1).replace("n12", str(z12))
                message3 = (message2).replace("n13", str(z13))
                message4 = (message3).replace("n14", str(z14))
                message5 = (message4).replace("n15", str(z15))
                message6 = (message5).replace("n16", str(z16))
                message7 = (message6).replace("n17", str(z17))
                message8 = (message7).replace("n18", str(z18))
                message9 = (message8).replace("n19", str(z19))
                message10 = message9
                await message.channel.send(content=message10)

            # ___ ___ ___ __  __ ___ _   _ __  __ 
            # | _ \ _ \ __|  \/  |_ _| | | |  \/  |
            # |  _/   / _|| |\/| || || |_| | |\/| |
            # |_| |_|_\___|_|  |_|___|\___/|_|  |_|

            if invoke == "activate" or invoke == "premiumactivate" or invoke == "activatepremium" or invoke == "activatePremium" or invoke == "pa" or invoke == "ap":
                if message.author.guild_permissions.administrator == True or message.author.id == DEINE_USER_ID:
                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    await message.channel.send(
                        content="Oh cool du möchtest Premium aktivieren? Bitte sei dir sicher das nur du und ich diesen Channel sehen können. Nun sende bitte deinen 'Key' direckt unter dieser Nachricht. Dein 'Key' sollte folgendermaßen aussehen: `xxxxxxxxxxxxxxxx`")
                    ke = await client.wait_for("message", check=c, timeout=None)
                    key = ke.content
                    try:
                        int(key)
                        if len(key) == 16 or len(key) == 15:
                            cur.execute("SELECT server FROM premium_user WHERE key=?", (int(key),))
                            exists = cur.fetchall()
                            cur.execute("SELECT userid FROM premium_user WHERE key=?", (int(key),))
                            user = cur.fetchone()[0]
                            if user == 0 or user == message.author.id:
                                print(exists)
                                if str(exists) == "[(88,)]":
                                    cur.execute("SELECT status FROM premium WHERE key=? AND serverid=?",
                                                (int(key), message.guild.id))
                                    date = cur.fetchall()
                                    if str(date) == "[]":
                                        cur.execute(
                                            "INSERT INTO premium (key, serverid, servername, status) VALUES(?, ?, ?, ?)",
                                            (int(key), message.guild.id, message.author.guild.name, "activated"))

                                        conn.commit()
                                        await message.channel.send(
                                            content="Sehr Gut Premium wurde erfolgreich für diesen Server aktiviert :tada:, wenn du irgendwelche Vorschläge oder so hast kontaktiere mich bitte. Dann noch viel Spaß mit dem Bot.")
                                    else:
                                        await message.channel.send(
                                            content="Cool dass du an einer Premium Version meines Bot's interressiert bist, und dass du deinen Key gleich 2 mal einlösen willst aber ich denke 1 mal reicht aus^^")
                                elif str(exists) == "[(1,)]":
                                    cur.execute("UPDATE premium_user SET server=0 WHERE key=?", (int(key),))
                                    conn.commit()
                                    cur.execute("SELECT status FROM premium WHERE key=? AND serverid=?",
                                                (int(key), message.guild.id))
                                    date = cur.fetchall()
                                    if str(date) == "[]":
                                        cur.execute(
                                            "INSERT INTO premium (key, serverid, servername, status) VALUES(?, ?, ?, ?)",
                                            (int(key), message.guild.id, message.author.guild.name, "activated"))
                                        conn.commit()
                                        await message.channel.send(
                                            content="Sehr Gut Premium wurde erfolgreich für diesen Server aktiviert :tada:, wenn du irgendwelche Vorschläge oder so hast kontaktiere mich bitte. Dann noch viel Spaß mit dem Bot..")
                                    else:
                                        await message.channel.send(
                                            content="Cool dass du an einer Premium Version meines Bot's interressiert bist, und dass du deinen Key gleich 2 mal einlösen willst aber ich denke 1 mal reicht aus^^")
                                elif str(exists) == "[(0,)]":
                                    await message.channel.send(
                                        content="Es tut mir wirklich leid aber der Key ist berreits auf einem anderen Server aktiviert.")
                            else:
                                await message.channel.send(
                                    content="Das ist nicht dein Key! Bitte kaufe dir deinen eigenen auf [Patrreon](https://patreon.com/TheBotDev)")
                        else:
                            await message.channel.send(content="Die Länge von deinem Key ist falsch!")

                    except:
                        await message.channel.send(content="Kein gültiger Key eingegeben")
                else:
                    sorry = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Diesen Command können leider nur Administartoren ausführen").set_thumbnail(
                        url="https://thebotdev.de/assets/img/alert.png"))
                    await asyncio.sleep(20)
                    await sorry.delete()
            if invoke == "premium":
                cur.execute("SELECT status FROM premium WHERE serverid=?", (message.guild.id,))
                stat = cur.fetchall()
                status = "error to read database"
                if str(stat) == "[]":
                    status = "Premium is not activated for this server"
                else:
                    status = "Bot is premium here"
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Premium Dashboard")
                embed.add_field(name="status:", value=status, inline=False)
                embed.add_field(name="Info:",
                                value="You can see from the fact that this icon %s is before a setting, that it only works when you own Premium. To buy Premium please enter **!buypremium**" % (
                                    str(premium)), inline=False)
                embed.add_field(name="Why premium?",
                                value="I sell premium for my bots not because I want to deduct money from someone, but because I have certain expenses for my bots and I try to get this money back by selling the premium rank (1$ for one server | 3$ for infinite number of servers)",
                                inline=False)
                embed.add_field(name="What do i get if i buy premium?",
                                value="If you buy premium, you get access to more features from this bot and the premium role on my server with it you can access more channels on this server.")
                await message.channel.send(embed=embed)

            if invoke == "buypremium":
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Buy Premium <3", url="https://patreon.com/TheBotDev")
                embed.add_field(name="How do i buy premium?",
                                value="To get the Premium Rank you need to be on TheBotDev Support Server, where you will receive a private message with your product key as soon as you buy the Premium Rank for one (1$) or for an infinite number of servers (3$), which you can then activate with %sactivatePremium on your server." % (
                                    prefix))
                embed.add_field(name="Where could i buy Premium?",
                                value="You could buy premium for this bot on [Patreon](https://patreon.com/TheBotDev), but you have to be on [TheBotDev Support Server](https://discord.gg/HD7x2vx)")
                embed.add_field(name="How do i activate Premium?",
                                value="After you have bought the premium rank on Patreon you get a private message from my bot which sends you a 16 digits long code, which them you can activate your server with the %sactivatePremium command" % (
                                    str(prefix)))
                await message.channel.send(embed=embed)

            # ___   _   __  __ ___ ___ 
            # / __| /_\ |  \/  | __/ __|
            # | (_ |/ _ \| |\/| | _|\__ \
            # \___/_/ \_\_|  |_|___|___/

            # Iam sorry, but i dont publish all the games from my Bot, because i sell them on patreon

            if invoke == "acc":
                ban = "unknown"
                cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                            (message.author.id, message.guild.id))
                existiertacc = cur.fetchall()
                if str(existiertacc) == "[]":
                    cur.execute("INSERT INTO server_game_accounts (userid, money, banned, serverid) VALUES(?,?,?,?)",
                                (message.author.id, 2500, 0, message.guild.id))
                    conn.commit()
                    await message.channel.send(
                        content="Your account has been successfully created! For more infos please enter %sacc or type in %sgames to get a list with all games" % (
                        prefix, prefix))
                else:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                (message.author.id, message.guild.id))
                    money = cur.fetchone()[0]
                    cur.execute("SELECT banned FROM server_game_accounts WHERE userid=? AND serverid=?",
                                (message.author.id, message.guild.id))
                    banned = cur.fetchall()
                    if str(banned) != "[]":
                        cur.execute("SELECT banned FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (message.author.id, message.guild.id))
                        userban = cur.fetchone()[0]
                        if userban == 1:
                            ban = "banned for games by the server admin"
                        elif userban == 0:
                            ban = "Your not banned for games"
                    else:
                        ban = "Your not banned for games"
                    embed = discord.Embed(color=0x64efff)
                    embed.set_author(name="Account")
                    embed.add_field(name="money:", value=str(money) + str(moneyicon), inline=True)
                    embed.add_field(name="ban status:", value=ban, inline=True)
                    embed.add_field(name="Games", value=prefix + "games", inline=False)
                    await message.channel.send(embed=embed)

            if invoke == "number":
                cur.execute("SELECT channel FROM server_game_settings WHERE guildid=?", (message.guild.id,))
                channel = cur.fetchone()[0]
                if channel == message.channel.id:
                    abfrage = await message.channel.send(
                        content=":one: 1-10 costs: 10%s win: 100%s\n:two: 1-20 costs: 10%s win: 200%s\n:three: 1-30 costs: 10%s win: 3000%s\n:four: 1-40 costs: 10%s win: 4000%s\n:five: 1-50 costs: 10%s win: 5555%s" % (
                        str(moneyicon), str(moneyicon), str(moneyicon), str(moneyicon), str(moneyicon), str(moneyicon),
                        str(moneyicon), str(moneyicon), str(moneyicon), str(moneyicon)))
                    try:
                        await abfrage.add_reaction(n1)
                        await abfrage.add_reaction(n2)
                        await abfrage.add_reaction(n3)
                        await abfrage.add_reaction(n4)
                        await abfrage.add_reaction(n5)
                    except discord.errors.Forbidden:
                        await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                       description="Error! Couldnt start the game! I do not have the permissions for adding reactions"))
                else:
                    information = await message.channel.send(
                        content="This is not a game channel or games are not allowed on this server, if you are the admin and want to set it up type in !setupG")
                    await asyncio.sleep(20)
                    await information.delete()


            # PREFIX
            elif invoke == "PREFIX":
                chapre = prefix + "pchange"
                hel = prefix + "help"
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Prefix")
                embed.add_field(name="current Prefix:", value=prefix, inline=False)
                embed.add_field(name="change Prefix:", value=chapre, inline=False)
                embed.add_field(name="more help:", value=hel, inline=True)
                await message.channel.send(embed=embed)
            elif invoke == "pchange":
                if message.author.guild_permissions.administrator == True or message.author.id == 333220752117596160:
                    gid = message.guild.id
                    await message.channel.send(embed=discord.Embed(color=0x64efff,
                                                                   description="Your current prefix is %s Now just send me the new prefix" % prefix))

                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    waitfor = await client.wait_for("message", check=c, timeout=None)
                    newprefix = waitfor.content
                    cur.execute("UPDATE server_settings SET prefix=? WHERE gid=?", (newprefix, gid))
                    conn.commit()
                    await message.channel.send(content="Successful new prefix is " + str(newprefix))
                else:
                    await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                   description="This command can only use administrators, sorry").set_thumbnail(
                        url="https://thebotdev.de/assets/img/alert.png"))
            elif invoke == "changelog":
                await message.channel.send(content=msgChangeLog)
            elif invoke == "info":
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Botinfo",
                                 icon_url="https://thebotdev.de/assets/img/Fragezeichen.png")
                embed.add_field(name="Bot by:", value="BaseChip#2390", inline=False)
                embed.add_field(name="Project:", value="TheBotDev", inline=False)
                embed.add_field(name="Invite me to your server:",
                                value="[invite](https://discordapp.com/oauth2/authorize?client_id=398933329862328330&permissions=1342663878&scope=bot)",
                                inline=False)
                embed.add_field(name="My Support Server:", value="https://discord.gg/HD7x2vx", inline=False)
                embed.add_field(name="Bot Lists:",
                                value="[DiscordBots](https://discordbots.org/bot/398933329862328330)", inline=False)
                embed.add_field(name="Version:", value=version, inline=False)
				embed.add_field(name="GitHub", value="[This is a fork from GitHub](https://github.com/BaseChip)", inline=False)
                embed.add_field(name="Libary", value="discord.py rewrite api", inline=False)
                # embed.add_field(name="", value="")
                embed.set_footer(text="Thanks for using!")
                await message.channel.send(embed=embed)

            elif invoke == "replaceinfo":
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Replace Info",
                                 icon_url="https://thebotdev.de/assets/img/Fragezeichen.png")
                embed.add_field(name="Available Emojis",
                                value=" n11 -> %s\nn12 -> %s\nn13 -> %s\nn14 -> %s\nn15 -> %s\nn16 -> %s\nn17 -> %s\nn18 -> %s\nn19 -> %s" % (
                                str(z11), str(z12), str(z13), str(z14), str(z15), str(z16), str(z17), str(z18),
                                str(z19)))
                await message.channel.send(embed=embed)

            elif invoke == "rules" and message.channel.id != 404911854112997377:
                embed = discord.Embed(title="Rules ",
                                      description="A function to create rules is not built into this bot, but here are two bots which can create rules for you",
                                      color=0x00ff00)
                embed.add_field(name="Rules Bot (from me)", value="https://discord.gg/HD7x2vx", inline=False)
                embed.add_field(name="Flash", value="https://flashbot.de", inline=True)
                await message.channel.send(embed=embed)

            elif invoke == "help" or invoke == "Help" or invoke == "Support" or invoke == "Hilfe":
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Help", icon_url="https://thebotdev.de/assets/img/Fragezeichen.png")
                embed.add_field(name="Prefix",
                                value="➥" + prefix + "**PREFIX** -> shows the informations about this command\n➥" + prefix + "**pchange** -> change the bots prefix",
                                inline=False)
                embed.add_field(name="Logs",
                                value="➥" + prefix + "**log** -> shows information abaout Logs on your server\n➥" + prefix + "**setupL** -> Setup the servers logs",
                                inline=False)
                embed.add_field(name="Admin Staff",
                                value="➥" + prefix + "**ban** -> Ban a user\n➥" + prefix + "**kick** -> Kick a user\n➥" + prefix + "**ping** -> Shows that the Bot is online",
                                inline=False)
                embed.add_field(name="Messages",
                                value="➥" + prefix + "**send** [The Message] -> sends your message\n" + "➥" + prefix + "**message** -> Creates messages with a colored Border\n➥" + prefix + "**replaceinfo** -> Infos to the replace command\n➥" + prefix + "**replace** -> Replace to some usefull emojis")
                embed.add_field(name="Games",
                                value="➥%ssetupG\n➥%sgames\n➥%snumber\n➥%s%sdon\n➥%s%srace\n➥%s%saddmoney\n➥%s%sremovemoney" % (
                                prefix, prefix, prefix, str(premium), prefix, str(premium), prefix, str(premium),
                                prefix, str(premium), prefix), inline=False)
                embed.add_field(name="General things",
                                value="➥%s**info**\n➥%s**send** [the message]\n➥%s**rules**" % (prefix, prefix, prefix),
                                inline=False)
                embed.add_field(name="Premium",
                                value="➥%s**ap**\n➥%s**premium**\n➥%s**buypremium**" % (prefix, prefix, prefix))
                await message.channel.send(embed=embed)

            # Level
            # elif invoke=="LevelSetup" or invoke=="Levelsetup" or invoke=="levelsetup":
            #	await message.channel.send(embed=discord.Embed(color=discord.Color.green(), description="The setup for creating a levelbot is started. I could give the users a role when they reach the levels 10,15,20,25,30,50,100, now please click the numbers below to set up the role the user should get if he reach this level"))

            # Admin stuff
            elif invoke == "leave":
                if message.author.id == 333220752117596160 and message.author.name == "BaseChip":
                    await message.guild.leave()

                else:
                    await message.channel.send(
                        content="WOW an hidden feature, but this feature could only use BaseChip - sorry")
            elif invoke == "ban":
                if message.author.guild_permissions.administrator == True or message.author.id == 333220752117596160:
                    await message.channel.send(content="Please mention now the User i should ban")

                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    usr = await client.wait_for("message", check=c, timeout=None)
                    usertoban = usr.mentions[0]
                    await message.channel.send(content="If I should ban " + str(
                        usertoban.mention) + " then please send me now the reason and otherwise please send `n`")
                    reas = await client.wait_for("message", check=c, timeout=None)
                    if reas.content != "n":
                        try:
                            await message.author.guild.ban(usertoban,
                                                           reason=reas.content + "  | Banned by: " + reas.author.name,
                                                           delete_message_days=7)
                        except discord.errors.Forbidden:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Error i dont have the permissions to ban"))
                else:
                    sorry = await message.channel.send(content="sorry this command can only use admins")
                    await asyncio.sleep(20)
                    await sorry.delete()

            elif invoke == "kick":
                if message.author.guild_permissions.administrator == True or message.author.id == 333220752117596160:
                    await message.channel.send(content="Please mention now the User i should kick")

                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    usr = await client.wait_for("message", check=c, timeout=None)
                    usertoban = usr.mentions[0]
                    await message.channel.send(content="If I should ban " + str(
                        usertoban.mention) + " then please send me now the reason and otherwise please send `n`")
                    reas = await client.wait_for("message", check=c, timeout=None)
                    if reas.content != "n":
                        try:
                            await message.author.guild.kick(usertoban,
                                                            reason=reas.content + "  | Kicked by: " + reas.author.name)
                        except discord.errors.Forbidden:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Error i dont have the permissions to ban"))
                else:
                    sorry = await message.channel.send(content="sorry this command can only use admins")
                    await asyncio.sleep(20)
                    await sorry.delete()

            # logs
            elif invoke == "log":
                gid = message.guild.id
                cur.execute("SELECT activated FROM server_logs WHERE gid=?", (gid,))
                status = cur.fetchone()[0]
                if status == "yes":
                    act = "Logs are enabled on this server"
                else:
                    act = "Logs are not created here "
                hel = prefix + "help"
                change = prefix + "setupL"
                embed = discord.Embed(color=0x64efff)
                embed.set_author(name="Logs")
                embed.add_field(name="Status:", value=act, inline=False)
                embed.add_field(name="Set up logs:", value=change, inline=False)
                embed.add_field(name="more help:", value=hel, inline=True)
                await message.channel.send(embed=embed)
            elif invoke == "setupL":
                if message.author.guild_permissions.administrator == True or message.author.id == 333220752117596160:
                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    await message.channel.send(embed=discord.Embed(color=0x64efff,
                                                                   description="Okay first of all please mention the channel where i should send all logs to like #YourChannel"))
                    waitforchannel = await client.wait_for("message", check=c, timeout=None)
                    log = waitforchannel.channel_mentions[0]
                    logchannel = log.id
                    cur.execute("SELECT server FROM webhook WHERE server=?", (message.guild.id,))
                    webhshex = cur.fetchall()
                    if str(webhshex) == "[]":
                        print(webhshex)
                        try:
                            webh = await log.create_webhook(name="Logit")
                            cur.execute("INSERT INTO webhook (server, url) VALUES (?,?)", (message.guild.id, webh.url))
                            conn.commit()
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(webh.url, adapter=AsyncWebhookAdapter(session))
                                await webhook.send(username='Logit',
                                                   avatar_url="https://cdn.discordapp.com/app-icons/398933329862328330/e33eff5bb64f94c2d013bc9e6de01393.png",
                                                   embed=discord.Embed(color=discord.Color.green(),
                                                                       description="It worked"))

                        except discord.errors.Forbidden:
                            await message.channel.send(
                                content="Setup has been cancelled! Unfortunately I don't have the authorization to create a webhook (manage_webhooks), but this is urgently needed for this function.")
                    else:
                        cur.execute("SELECT url FROM webhook WHERE server=?", (message.guild.id,))
                        url = cur.fetchone()[0]
                        try:
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
                                await webhook.send(username='Logit',
                                                   avatar_url="https://cdn.discordapp.com/app-icons/398933329862328330/e33eff5bb64f94c2d013bc9e6de01393.png",
                                                   embed=discord.Embed(color=discord.Color.green(),
                                                                       description="Webhook existiert bereits"))
                        except discord.errors.NotFound:
                            await message.channel.send("Please kick the bot and invite him again - thx")
                    print(logchannel)
                    if logchannel != None:
                        gid = message.guild.id
                        auth = message.author.id
                        embed = discord.Embed(description="to activate a function please click the number for this setting",color=0x64efff)
                        embed.set_author(name="Setup | Logs")
                        embed.add_field(name="member join", value="1", inline=False)
                        embed.add_field(name="member leave", value="2", inline=False)
                        embed.add_field(name="member update (e.g changed Nickname...)", value="3", inline=False)
                        embed.add_field(name="member ban", value="4", inline=False)
                        embed.add_field(name="member unban", value="5", inline=False)
                        embed.add_field(name="message delete", value="6", inline=False)
                        embed.add_field(name="bulk message delete", value="7", inline=False)
                        embed.add_field(name="message edit", value="8", inline=False)
                        embed.add_field(name="channel create", value="9", inline=False)
                        embed.add_field(name="channel update", value="10", inline=False)
                        embed.add_field(name="channel delete", value="11", inline=False)
                        embed.add_field(name="member joins a voice channel", value="12", inline=False)
                        embed.add_field(name="emoji add/update/remove to the server", value="13", inline=False)
                        embed.add_field(name="reaction add", value="14", inline=False)
                        embed.add_field(name="reaction remove", value="15", inline=False)
                        embed.add_field(name="reaction clear", value="16", inline=False)
                        embed.add_field(name="role create", value="17", inline=False)
                        embed.add_field(name="role delete", value="18", inline=False)
                        embed.add_field(name="role update", value="19", inline=False)
                        embed.set_footer(text="You could click so many nummbers as you want to activate")

                        cur.execute("UPDATE server_logs SET owner=?, activated='yes', channelid=? WHERE gid=?",(auth, logchannel, gid))
                        conn.commit()

                        msg = await message.channel.send(embed=embed)
                        try:
                            await msg.add_reaction(z1)
                            await msg.add_reaction(z2)
                            await msg.add_reaction(z3)
                            await msg.add_reaction(z4)
                            await msg.add_reaction(z5)
                            await msg.add_reaction(z6)
                            await msg.add_reaction(z7)
                            await msg.add_reaction(z8)
                            await msg.add_reaction(z9)
                            await msg.add_reaction(z10)
                            await msg.add_reaction(z11)
                            await msg.add_reaction(z12)
                            await msg.add_reaction(z13)
                            await msg.add_reaction(z14)
                            await msg.add_reaction(z15)
                            await msg.add_reaction(z16)
                            await msg.add_reaction(z17)
                            await msg.add_reaction(z18)
                            await msg.add_reaction(z19)
                        except discord.errors.Forbidden:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Error! setup is stopped! I do not have the permissions for adding reactions"))
                        except discord.errors.NotFound:
                            await message.channel.send(
                                content="Sorry! something went wrong! I couldnt find my emojis. Please join https://discord.gg/HD7x2vx to get help from me")
                        except discord.errors.HTTPException:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Error! I have a temporary issue. Please try it again or join my support server to get help https://discord.gg/HD7x2vx "))
                    else:
                        await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Error! setup is broken up! Your input wasnt okay it should look like this **386425937748819978**"))
                else:
                    sorry = await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description="This command can only use administrators, sorry").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))
                    await asyncio.sleep(20)
                    await sorry.delete()

            elif invoke == "send":
                if message.author.guild_permissions.administrator == True or message.author.id == 333220752117596160:
                    me = (message.content).replace("send", "")
                    mes = (me).replace(str(prefix), "")
                    try:
                        await message.channel.send(content=mes)
                    except discord.errors.HTTPException:
                        await message.channel.send(embed=discord.Embed(color=0x64efff,
                                                                       description=prefix + "send [The Message I should send]"))
                else:
                    sorry = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="This command can only use administrators, sorry").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))
                    await asyncio.sleep(20)
                    await sorry.delete()
            elif invoke == "message":
                setup = await message.channel.send(embed=discord.Embed(color=discord.Color.magenta(), description="OK! The setup for creating a message is started. Please send now the color, which should have the border (green/red/magenta/blue/gold) and don't worry about this message and which ones will be written during setup I delete later:) "))

                # time.sleep(4)

                def checkmsg(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m

                msgwaitfor = await client.wait_for("message", check=checkmsg, timeout=None)
                if msgwaitfor != None:

                    if msgwaitfor.content == "green":
                        print("Color: Green")
                        cg = await message.channel.send(embed=discord.Embed(color=discord.Color.green(), description="You have chosen the color green. As an example of what the message looks like later, this message has already colored the border. So now please send me the text, which your message should have"))

                        def checkg(m):
                            if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m

                        msg2 = await client.wait_for("message", check=checkg, timeout=None)
                        text = await message.channel.send(
                            embed=discord.Embed(color=discord.Color.green(), description=msg2.content))
                        try:
                            await message.delete()
                            await setup.delete()
                            await msgwaitfor.delete()
                            await cg.delete()
                        except:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description="Oh it looks like that i have to correct myself. I said i am going to delete all messages, but it seems to be that i do not have the permissions to delete messages (manage messages)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))

                    elif msgwaitfor.content == "red":
                        print("Color: Red")
                        cg = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="You have chosen the color red. As an example of what the message looks like later, this message has already colored the border. So now please send me the text, which your message should have"))

                        def checkr(m):
                            if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m

                        msg2 = await client.wait_for("message", check=None, timeout=None)
                        text = await message.channel.send(
                            embed=discord.Embed(color=discord.Color.red(), description=msg2.content))
                        try:
                            await message.delete()
                            await setup.delete()
                            await msgwaitfor.delete()
                            await cg.delete()
                        except:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description="Oh it looks like that i have to correct myself. I said i am going to delete all messages, but it seems to be that i do not have the permissions to delete messages (manage messages)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))




                    elif msgwaitfor.content == "blue":
                        print("Color: Blue")
                        cg = await message.channel.send(embed=discord.Embed(color=discord.Color.blue(),
                                                                            description="You have chosen the color blue. As an example of what the message looks like later, this message has already colored the border. So now please send me the text, which your message should have"))

                        def checkb(m):
                            if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m

                        msg2 = await client.wait_for("message", check=checkb, timeout=None)
                        text = await message.channel.send(
                            embed=discord.Embed(color=discord.Color.blue(), description=msg2.content))
                        try:
                            await message.delete()
                            await setup.delete()
                            await msgwaitfor.delete()
                            await cg.delete()
                        except:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Oh it looks like that i have to correct myself. I said i am going to delete all messages, but it seems to be that i do not have the permissions to delete messages (manage messages)").set_thumbnail(
                                url="https://thebotdev.de/assets/img/alert.png"))



                    elif msgwaitfor.content == "magenta":
                        print("Color: Magenta")
                        cg = await message.channel.send(embed=discord.Embed(color=discord.Color.magenta(),
                                                                            description="You have chosen the color magenta. As an example of what the message looks like later, this message has already colored the border. So now please send me the text, which your message should have"))

                        def checkm(m):
                            if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m

                        msg2 = await client.wait_for("message", check=checkm, timeout=None)
                        text = await message.channel.send(
                            embed=discord.Embed(color=discord.Color.magenta(), description=msg2.content))
                        try:
                            await message.delete()
                            await setup.delete()
                            await msgwaitfor.delete()
                            await cg.delete()
                        except:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Oh it looks like that i have to correct myself. I said i am going to delete all messages, but it seems to be that i do not have the permissions to delete messages (manage messages)").set_thumbnail(
                                url="https://thebotdev.de/assets/img/alert.png"))


                    elif msgwaitfor.content == "gold":
                        print("Color: Gold")
                        cg = await message.channel.send(embed=discord.Embed(color=discord.Color.gold(),
                                                                            description="You have chosen the color gold - ok its more yellow, but its called gold. As an example of what the message looks like later, this message has already colored the border. So now please send me the text, which your message should have"))

                        def checkgold(m):
                            if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m

                        msg2 = await client.wait_for("message", check=checkgold, timeout=None)
                        text = await message.channel.send(
                            embed=discord.Embed(color=discord.Color.gold(), description=msg2.content))
                        try:
                            await message.delete()
                            await setup.delete()
                            await msgwaitfor.delete()
                            await cg.delete()
                        except:
                            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                                           description="Oh it looks like that i have to correct myself. I said i am going to delete all messages, but it seems to be that i do not have the permissions to delete messages (manage messages)").set_thumbnail(
                                url="https://thebotdev.de/assets/img/alert.png"))

                    else:
                        print("Farbe nicht erkannt")
        elif message.mentions != None:
            for mentionsn in message.mentions:
                if mentionsn == client.user:
                    await message.channel.send(
                        content="Oh Hello! Here are my most useful commands " + prefix + "help and " + prefix + "info\n Thanks for using!")

    async def on_raw_reaction_add(self, emoji, message_id, channel_id, user_id):
        gu = client.get_channel(channel_id)
        guild = gu.guild.id
        gugui = client.get_guild(guild)
        usr = gugui.get_member(user_id)
        gid = gugui.id
        cur.execute("SELECT owner FROM server_logs WHERE gid=?", (gid,))
        owner = cur.fetchone()[0]
        cur.execute("SELECT channel FROM server_game_settings WHERE guildid=?", (gid,))
        chan = cur.fetchall()
        # cur.execute("SELECT channelid FROM server_logs WHERE gid=?")
        # chann = cur.fetchone()[0]	
        if str(chan) != "[]" and user_id != client.user.id:
            print(channel_id)
            cur.execute("SELECT channel FROM server_game_settings WHERE guildid=?", (gid,))
            chan = cur.fetchone()[0]
            print(chan)

            def c(m):
                if m.author.id == user_id:
                    return m

            if chan == channel_id:
                if emoji.id == n1.id:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?", (user_id, gid))
                    Usersmoney = cur.fetchall()
                    if str(Usersmoney) == "[]":
                        msg = await gu.send(
                            content="I'm sorry, but you can't play the game yet because you don't have an account. To create one simply type %sacc to create one and get 2500" % (
                                prefix) + str(moneyicon))
                        await asyncio.sleep(60)
                        await msg.delete()
                    else:
                        cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (user_id, gid))
                        money = cur.fetchone()[0]
                        if money >= 10:
                            newmoney = money - 10
                            cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                        (newmoney, user_id, gid))
                            conn.commit()
                            await gu.send(
                                content="So I have now thought a number which is between 1 and 10, now please send me the number where you think I thought it was (only the number e. g. `5`)")
                            gedacht = await client.wait_for("message", check=c, timeout=None)
                            botsgedacht = random.randint(1, 10)
                            if botsgedacht == int(gedacht.content):
                                await gu.send(content="Wow that was right! My number was " + str(botsgedacht))
                                newmoney = money + 100
                                cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                            (newmoney, user_id, gid))
                                conn.commit()
                            else:
                                await gu.send(
                                    content="Iam sorry that was not what i thought my number was " + str(botsgedacht))
                        else:
                            await gu.send(
                                content="Oh, you can't play this games any more because you have not enough money;( Your money: " + str(
                                    money))
                elif emoji.id == n2.id:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?", (user_id, gid))
                    Usersmoney = cur.fetchall()
                    if str(Usersmoney) == "[]":
                        msg = await gu.send(
                            content="I'm sorry, but you can't play the game yet because you don't have an account. To create one simply type %sacc to create one and get 2500" % (
                                prefix) + str(moneyicon))
                        await asyncio.sleep(60)
                        await msg.delete()
                    else:
                        cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (user_id, gid))
                        money = cur.fetchone()[0]
                        if money >= 10:
                            newmoney = money - 10
                            cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                        (newmoney, user_id, gid))
                            conn.commit()
                            await gu.send(
                                content="So I have now thought a number which is between 1 and 20, now please send me the number where you think I thought it was (only the number e. g. `5`)")
                            gedacht = await client.wait_for("message", check=c, timeout=None)
                            botsgedacht = random.randint(1, 20)
                            if botsgedacht == int(gedacht.content):
                                await gu.send(content="Wow that was right! My number was " + str(botsgedacht))
                                newmoney = money + 200
                                cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                            (newmoney, user_id, gid))
                                conn.commit()
                            else:
                                await gu.send(
                                    content="Iam sorry that was not what i thought my number was " + str(botsgedacht))
                        else:
                            await gu.send(
                                content="Oh, you can't play this games any more because you have not enough money;( Your money: " + str(
                                    money))

                elif emoji.id == n3.id:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?", (user_id, gid))
                    Usersmoney = cur.fetchall()
                    if str(Usersmoney) == "[]":
                        msg = await gu.send(
                            content="I'm sorry, but you can't play the game yet because you don't have an account. To create one simply type %sacc to create one and get 2500" % (
                                prefix) + str(moneyicon))
                        await asyncio.sleep(60)
                        await msg.delete()
                    else:
                        cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (user_id, gid))
                        money = cur.fetchone()[0]
                        if money >= 10:
                            newmoney = money - 10
                            cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                        (newmoney, user_id, gid))
                            conn.commit()
                            await gu.send(
                                content="So I have now thought a number which is between 1 and 30, now please send me the number where you think I thought it was (only the number e. g. `5`)")
                            gedacht = await client.wait_for("message", check=c, timeout=None)
                            botsgedacht = random.randint(1, 30)
                            if botsgedacht == int(gedacht.content):
                                await gu.send(content="Wow that was right! My number was " + str(botsgedacht))
                                newmoney = money + 3000
                                cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                            (newmoney, user_id, gid))
                                conn.commit()
                            else:
                                await gu.send(
                                    content="Iam sorry that was not what i thought my number was " + str(botsgedacht))
                        else:
                            await gu.send(
                                content="Oh, you can't play this games any more because you have not enough money;( Your money: " + str(
                                    money))

                elif emoji.id == n4.id:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?", (user_id, gid))
                    Usersmoney = cur.fetchall()
                    if str(Usersmoney) == "[]":
                        msg = await gu.send(
                            content="I'm sorry, but you can't play the game yet because you don't have an account. To create one simply type %sacc to create one and get 2500" % (
                                prefix) + str(moneyicon))
                        await asyncio.sleep(60)
                        await msg.delete()
                    else:
                        cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (user_id, gid))
                        money = cur.fetchone()[0]
                        if money >= 10:
                            newmoney = money - 10
                            cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                        (newmoney, user_id, gid))
                            conn.commit()
                            await gu.send(
                                content="So I have now thought a number which is between 1 and 40, now please send me the number where you think I thought it was (only the number e. g. `5`)")
                            gedacht = await client.wait_for("message", check=c, timeout=None)
                            botsgedacht = random.randint(1, 40)
                            if botsgedacht == int(gedacht.content):
                                await gu.send(content="Wow that was right! My number was " + str(botsgedacht))
                                newmoney = money + 40000
                                cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                            (newmoney, user_id, gid))
                                conn.commit()
                            else:
                                await gu.send(
                                    content="Iam sorry that was not what i thought my number was " + str(botsgedacht))
                        else:
                            await gu.send(
                                content="Oh, you can't play this games any more because you have not enough money;( Your money: " + str(
                                    money))

                elif emoji.id == n5.id:
                    cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?", (user_id, gid))
                    Usersmoney = cur.fetchall()
                    if str(Usersmoney) == "[]":
                        msg = await gu.send(
                            content="I'm sorry, but you can't play the game yet because you don't have an account. To create one simply type %sacc to create one and get 2500" % (
                                prefix) + str(moneyicon))
                        await asyncio.sleep(60)
                        await msg.delete()
                    else:
                        cur.execute("SELECT money FROM server_game_accounts WHERE userid=? AND serverid=?",
                                    (user_id, gid))
                        money = cur.fetchone()[0]
                        if money >= 10:
                            newmoney = money - 10
                            cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                        (newmoney, user_id, gid))
                            conn.commit()
                            await gu.send(
                                content="So I have now thought a number which is between 1 and 50, now please send me the number where you think I thought it was (only the number e. g. `5`)")
                            gedacht = await client.wait_for("message", check=c, timeout=None)
                            botsgedacht = random.randint(1, 50)
                            if botsgedacht == int(gedacht.content):
                                await gu.send(content="Wow that was right! My number was " + str(botsgedacht))
                                newmoney = money + 5555
                                cur.execute("UPDATE server_game_accounts SET money=? WHERE userid=? AND serverid=?",
                                            (newmoney, user_id, gid))
                                conn.commit()
                            else:
                                await gu.send(
                                    content="Iam sorry that was not what i thought my number was " + str(botsgedacht))
                        else:
                            await gu.send(
                                content="Oh, you can't play this games any more because you have not enough money;( Your money: " + str(
                                    money))
        if owner == user_id:
            if emoji.id == z1.id:
                cur.execute("UPDATE server_logs SET a1=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z2.id:
                cur.execute("UPDATE server_logs SET a2=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z3.id:
                cur.execute("UPDATE server_logs SET a3=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z4.id:
                cur.execute("UPDATE server_logs SET a4=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z5.id:
                cur.execute("UPDATE server_logs SET a5=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z6.id:
                cur.execute("UPDATE server_logs SET a6=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z7.id:
                cur.execute("UPDATE server_logs SET a7=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z8.id:
                cur.execute("UPDATE server_logs SET a8=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z9.id:
                cur.execute("UPDATE server_logs SET a9=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z10.id:
                cur.execute("UPDATE server_logs SET a10=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z11.id:
                cur.execute("UPDATE server_logs SET a11=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z12.id:
                cur.execute("UPDATE server_logs SET a12=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z13.id:
                cur.execute("UPDATE server_logs SET a13=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z14.id:
                cur.execute("UPDATE server_logs SET a14=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z15.id:
                cur.execute("UPDATE server_logs SET a15=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z16.id:
                cur.execute("UPDATE server_logs SET a16=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z17.id:
                cur.execute("UPDATE server_logs SET a17=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z18.id:
                cur.execute("UPDATE server_logs SET a18=1 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z19.id:
                cur.execute("UPDATE server_logs SET a19=1 WHERE gid=?", (gid,))
                conn.commit()
            else:
                cur.execute("SELECT a14 FROM server_logs WHERE gid=?", (gid,))
                data = cur.fetchone()[0]
                if data == 0 or data == None:
                    pass
                if data == 1:
                    cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
                    ch = cur.fetchone()[0]
                    channel = client.get_channel(ch)
                    await channel.send(embed=discord.Embed(color=discord.Color.green(), description="The User " + str(
                        usr.mention) + " reacted with " + str(emoji)).set_author(name=usr.name + " had reacted",
                                                                                 icon_url=usr.avatar_url))

        else:
            cur.execute("SELECT a14 FROM server_logs WHERE gid=?", (gid,))
            data = cur.fetchone()[0]
            if data == 0 or data == None:
                pass
            if data == 1:
                cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
                ch = cur.fetchone()[0]
                channel = client.get_channel(ch)
                await channel.send(embed=discord.Embed(color=discord.Color.green(), description="The User " + str(
                    usr.mention) + " reacted with " + str(emoji)).set_author(name=usr.name + " had reacted",
                                                                             icon_url=usr.avatar_url))

    async def on_raw_reaction_remove(self, emoji, message_id, channel_id, user_id):
        gu = client.get_channel(channel_id)
        guild = gu.guild.id
        gugui = client.get_guild(guild)
        usr = gugui.get_member(user_id)
        gid = gugui.id
        cur.execute("SELECT owner FROM server_logs WHERE gid=?", (gid,))
        owner = cur.fetchone()[0]
        # cur.execute("SELECT channelid FROM server_logs WHERE gid=?")
        # chann = cur.fetchone()[0]	
        if owner == user_id:
            if emoji.id == z1.id:
                cur.execute("UPDATE server_logs SET a1=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z2.id:
                cur.execute("UPDATE server_logs SET a2=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z3.id:
                cur.execute("UPDATE server_logs SET a3=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z4.id:
                cur.execute("UPDATE server_logs SET a4=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z5.id:
                cur.execute("UPDATE server_logs SET a5=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z6.id:
                cur.execute("UPDATE server_logs SET a6=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z7.id:
                cur.execute("UPDATE server_logs SET a7=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z8.id:
                cur.execute("UPDATE server_logs SET a8=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z9.id:
                cur.execute("UPDATE server_logs SET a9=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z10.id:
                cur.execute("UPDATE server_logs SET a10=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z11.id:
                cur.execute("UPDATE server_logs SET a11=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z12.id:
                cur.execute("UPDATE server_logs SET a12=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z13.id:
                cur.execute("UPDATE server_logs SET a13=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z14.id:
                cur.execute("UPDATE server_logs SET a14=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z15.id:
                cur.execute("UPDATE server_logs SET a15=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z16.id:
                cur.execute("UPDATE server_logs SET a16=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z17.id:
                cur.execute("UPDATE server_logs SET a17=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z18.id:
                cur.execute("UPDATE server_logs SET a18=0 WHERE gid=?", (gid,))
                conn.commit()
            elif emoji.id == z19.id:
                cur.execute("UPDATE server_logs SET a19=0 WHERE gid=?", (gid,))
                conn.commit()
            else:
                cur.execute("SELECT a15 FROM server_logs WHERE gid=?", (gid,))
                data = cur.fetchone()[0]
                if data == 0 or data == None:
                    pass
                if data == 1:
                    cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
                    ch = cur.fetchone()[0]
                    channel = client.get_channel(ch)
                    await channel.send(embed=discord.Embed(color=discord.Color.green(), description="The User " + str(
                        usr.mention) + " removed his reaction: " + str(emoji)).set_author(
                        name=usr.name + " had reacted", icon_url=usr.avatar_url))

        else:
            cur.execute("SELECT a15 FROM server_logs WHERE gid=?", (gid,))
            data = cur.fetchone()[0]
            if data == 0 or data == None:
                pass
            if data == 1:
                cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
                ch = cur.fetchone()[0]
                channel = client.get_channel(ch)
                await channel.send(embed=discord.Embed(color=discord.Color.green(), description="The User " + str(
                    usr.mention) + " removed his reaction: " + str(emoji)).set_author(name=usr.name + " had reacted",
                                                                                      icon_url=usr.avatar_url))

    async def on_raw_reaction_clear(self, message_id, channel_id):
        chan = client.get_channel(channel_id)
        gid = chan.guild.id
        cur.execute("SELECT a16 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=discord.Color.blue(),
                                                   description="Reactions from a message in the channel " + str(
                                                       chan.mention) + "has been cleared").set_author(
                name=chan.guild.name, icon=chan.guild.icon_url))

    async def on_member_join(self, member):
        gid = member.guild.id
        cur.execute("SELECT a1 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            usr = client.get_user(member.id)
            # hype = usr.profile.hypesquad
            # if hype==False:
            #	shype = hype

            embed = discord.Embed(title="User joined the server", color=0x00ff00)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Username:", value=member.name, inline=True)
            embed.add_field(name="Discriminator:", value=member.discriminator, inline=True)
            embed.add_field(name="User ID:", value=member.id, inline=True)
            embed.add_field(name="created at:", value=member.created_at, inline=True)
            # embed.add_field(name="hypesquad:", value=shype, inline=True)
            # embed.add_field(name="nitro:", value="no", inline=True)
            # embed.add_field(name="discord partner:", value="niemals", inline=True)
            await channel.send(embed=embed)

    async def on_member_remove(self, member):
        gid = member.guild.id
        cur.execute("SELECT a2 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            usr = client.get_user(member.id)
            # hype = usr.profile.hypesquad
            # if hype==False:
            #	shype = hype

            embed = discord.Embed(title="User leaved the server", color=discord.Color.red())
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Username:", value=member.name, inline=True)
            embed.add_field(name="Discriminator:", value=member.discriminator, inline=True)
            embed.add_field(name="User ID:", value=member.id, inline=True)
            embed.add_field(name="created at:", value=member.created_at, inline=True)
            # embed.add_field(name="hypesquad:", value=shype, inline=True)
            # embed.add_field(name="nitro:", value="no", inline=True)
            # embed.add_field(name="discord partner:", value="niemals", inline=True)
            await channel.send(embed=embed)

    async def on_member_update(self, before, after):

        gid = before.guild.id
        cur.execute("SELECT a3 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            if before.nick != after.nick:
                await channel.send(embed=discord.Embed(color=0x64efff, description="The User " + str(
                    before.name) + " changed his nick from " + str(before.nick) + " to " + str(after.nick)).set_author(
                    name=before.name, icon_url=before.avatar_url))
            elif before.status != after.status:
                await channel.send(embed=discord.Embed(color=0x64efff, description="The User " + str(
                    before.name) + " changed his status from " + str(before.status) + " to " + str(
                    after.status)).set_author(name=before.name, icon_url=before.avatar_url))
            elif before.game != after.game:
                await channel.send(embed=discord.Embed(color=0x64efff, description="The User " + str(
                    before.name) + " changed his game from " + str(before.game) + " to " + str(after.game)).set_author(
                    name=before.name, icon_url=before.avatar_url))
            elif before.avatar_url != after.avatar_url:
                await channel.send(embed=discord.Embed(color=0x64efff, description="The User " + str(
                    before.name) + " changed his avatar to ->").set_thumbnail(url=after.avatar_url))

            elif before.roles != after.roles:
                if len(before.roles) < len(after.roles):
                    await channel.send(embed=discord.Embed(color=0x64efff, description="The User " + str(
                        before.name) + " was added a role").set_author(name=before.name, icon_url=before.avatar_url))
                elif len(before.roles) > len(after.roles):
                    await channel.send(embed=discord.Embed(color=0x64efff, description="The User " + str(
                        before.name) + " was deleted from a role").set_author(name=before.name,
                                                                              icon_url=before.avatar_url))

    async def on_member_ban(self, guild, user):
        gid = guild.id
        cur.execute("SELECT a4 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=discord.Color.red(), description="The User " + str(
                user.name) + " was banned from the server ").set_author(name=user.name, icon_url=user.avatar_url))

    async def on_member_unban(self, guild, user):
        gid = guild.id
        cur.execute("SELECT a5 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=discord.Color.green(), description="The User " + str(
                user.name) + " was unbanned from the server ").set_author(name=user.name, icon_url=user.avatar_url))

    async def on_raw_message_delete(self, message_id, channel_id):
        channelmessage = client.get_channel(channel_id)
        print(channelmessage.name)
        # message = channel.get_message(message_id)
        gid = channelmessage.guild.id
        guild = channelmessage.guild
        cur.execute("SELECT a6 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            print(message_id)
            # await discord.abc.Messageable.get_message(, id=message_id)
            await channel.send(embed=discord.Embed(color=discord.Color.red(), description="Message in channel " + str(
                channelmessage.mention) + " was deleted.").set_author(name=guild.name + "| Log Deleted Message",
                                                                      icon_url=guild.icon_url))

    async def on_raw_bulk_message_delete(self, message_ids, channel_id):
        channel = client.get_channel(channel_id)
        anzahl = len(message_ids)
        gid = channel.guild.id
        guild = channel.guild
        cur.execute("SELECT a7 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            print(message_id)
            # await discord.abc.Messageable.get_message(, id=message_id)
            await channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                   description=anzahl + "x Messages in the channel " + str(
                                                       channel.mention) + " was deleted.").set_author(
                name=guild.name + "| Log Deleted Message", icon_url=guild.icon_url))

    async def on_message_edit(self, before, after):
        gid = before.author.guild.id
        cur.execute("SELECT a8 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            if before.content != after.content:
                cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
                ch = cur.fetchone()[0]
                channel = client.get_channel(ch)
                if before.content != "":
                    await channel.send(embed=discord.Embed(color=0x64efff, description="The message:\n`" + str(
                        before.content) + "`\n was changed to:\n`" + str(after.content) + "`").set_author(
                        name=before.author, icon_url=before.author.avatar_url))
                else:
                    pass

    async def on_guild_channel_create(self, neuerchannel):
        gid = neuerchannel.guild.id
        cur.execute("SELECT a9 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=0x64efff, description="The channel " + str(
                neuerchannel.mention) + " was created"))

    async def on_guild_channel_delete(self, neuerchannel):
        gid = neuerchannel.guild.id
        cur.execute("SELECT a11 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=0x64efff, description="The channel " + str(
                neuerchannel.name) + " has been deleted"))

    async def on_guild_channel_update(self, before, after):
        gid = before.guild.id
        cur.execute("SELECT a10 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            if before.name != after.name:
                await channel.send(embed=discord.Embed(color=0x64efff, description="The channel's name from " + str(
                    after.mention) + " has been changed from `" + str(before.name) + "` to `" + str(after.name) + "`"))
            elif before.topic != after.topic:
                await channel.send(embed=discord.Embed(color=0x64efff, description="The topic from the channel " + str(
                    after.mention) + " has been changed to:\n `" + str(after.topic) + "`"))
            else:
                await channel.send(embed=discord.Embed(color=0x64efff, description="The channel " + str(
                    after.mention) + " has been updated"))

    async def on_voice_state_update(self, member, before, after):
        memberid = member.id
        memb = member.guild.get_member(memberid)
        gid = member.guild.id
        cur.execute("SELECT a12 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            counterbefore = 0
            counterafter = 0
            if before.channel != None:
                counterbefore = counterbefore + 1
            elif after.channel != None:
                counterafter = counterafter + 1
            if counterbefore < counterafter:
                await channel.send(embed=discord.Embed(color=0x64efff, description="-> The User " + str(
                    member.name) + " jointed " + str(after.channel.name)).set_author(name=member.name,
                                                                                     icon_url=member.avatar_url))
            elif counterbefore > counterafter + 1000000:
                await channel.send(embed=discord.Embed(color=0x64efff,
                                                       description="-> The User " + str(memb.name) + " leaved " + str(
                                                           after.channel.name)).set_author(name=memb.name,
                                                                                           icon_url=memb.avatar_url))

    async def on_guild_emojis_update(self, guild, before, after):
        gid = guild.id
        cur.execute("SELECT a13 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            if len(before) < len(after):
                await channel.send(embed=discord.Embed(color=discord.Color.green(),
                                                       description="-> An Emoji as added to this server ").set_author(
                    name=guild.name, icon_url=guild.icon_url))
            elif len(before) > len(after):
                await channel.send(embed=discord.Embed(color=discord.Color.red(),
                                                       description="<- An Emoji as deleted from this server ").set_author(
                    name=guild.name, icon_url=guild.icon_url))

    async def on_guild_role_create(self, role):
        gid = role.guild.id
        cur.execute("SELECT a17 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=discord.Color.green(), description="The Role `" + str(
                role.name) + "` was created").set_author(name=role.guild.name, icon_url=role.guild.icon_url))

    async def on_guild_role_delete(self, role):
        gid = role.guild.id
        cur.execute("SELECT a18 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            await channel.send(embed=discord.Embed(color=discord.Color.green(), description="The Role `" + str(
                role.name) + "` was deleted").set_author(name=role.guild.name, icon_url=role.guild.icon_url))

    async def on_guild_role_update(self, before, after):
        gid = after.guild.id
        cur.execute("SELECT a19 FROM server_logs WHERE gid=?", (gid,))
        data = cur.fetchone()[0]
        if data == 0 or data == None:
            pass
        if data == 1:
            cur.execute("SELECT channelid FROM server_logs WHERE gid=?", (gid,))
            ch = cur.fetchone()[0]
            channel = client.get_channel(ch)
            if before.name == after.name:
                await channel.send(embed=discord.Embed(color=discord.Color.green(), description="The Role `" + str(
                    after.name) + "` was updated").set_author(name=after.guild.name, icon_url=after.guild.icon_url))
            elif before.name != after.name:
                await channel.send(embed=discord.Embed(color=discord.Color.green(),
                                                       description="The Roles name was changed from `" + str(
                                                           before.name) + "` to `" + str(after.name) + "`").set_author(
                    name=after.guild.name, icon_url=after.guild.icon_url))

    async def on_guild_join(self, guild):

        gid = guild.id
        gnm = guild.name
        prefixnormalsetting = "!"
        cur.execute("INSERT INTO server_settings(gid, prefix) VALUES(?, ?)", (gid, prefixnormalsetting))
        cur.execute("INSERT INTO server_logs(gid) VALUES(?)", (gid,))
        conn.commit()

    async def on_guild_remove(self, guild):
        gid = guild.id
        cur.execute("DELETE FROM server_settings WHERE gid=?", (gid,))
        cur.execute("DELETE FROM server_logs WHERE gid=?", (gid,))
        conn.commit()


client = MyClient()
client.run(KEYS.TOKEN)
