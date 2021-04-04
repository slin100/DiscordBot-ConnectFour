import discord

class emoji:
    white = "⬜"
    black = "⬛"
    green = "🟩"
    red = "🟥"
    one = "1️⃣"
    two = "2️⃣"
    three = "3️⃣"
    four = "4️⃣"
    five = "5️⃣"
    six = "6️⃣"
    seven = "7️⃣"

Player = []
PlayerLog = [None]
winner = []

def Map4():
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    p1 = [emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white]
    p2 = [emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white]
    p3 = [emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white]
    p4 = [emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white]
    p5 = [emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white]
    p6 = [emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white, emoji.white]

Map4()
def MapText(Rowlist):
    plist = [p1,p2,p3,p4,p5,p6]
    FullMap = f"{emoji.one}{emoji.two}{emoji.three}{emoji.four}{emoji.five}{emoji.six}{emoji.seven}"
    num = -1
    for p in plist:
        num += 1
        try:FullMap += f"\n{p[0]}{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}    {Rowlist[num]}"
        except:FullMap += f"\n{p[0]}{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}"
    return FullMap

def win(PlayerSymbole, x,y):
    winn = False
    # look wagerecht
    plist = [p1,p2,p3,p4,p5,p6]
    for p in plist:
        count = 0
        for i in range(6):
            if count >= 4:
                winn = True
            if p[i]  == PlayerSymbole:
                count += 1
            else:
                count = 0
    # look vertical
    for i in range(6):
        count = 0
        for p in plist:
            if p[i]  == PlayerSymbole:
                count += 1
                if count >= 4:
                    winn = True
            else:
                count = 0
    # look cross
    # /
    inRow = 1
    # Geht von unten links nach oben rechts
    try :
        if plist[y-1][x] == plist[y-2][x+1]:
            inRow += 1
            try:
                if plist[y-3][x+2] == plist[y-2][x+1]:
                    inRow += 1
                    try:
                        if plist[y-3][x+2] == plist[y-4][x+3]:
                            inRow += 1
                    except: pass
            except: pass
    except: pass

    # Geht von oben rechts nach unten links
    try:
        if plist[y-1][x] == plist[y][x-1]:
            inRow += 1
            try:
                if plist[y+1][x-2] == plist[y][x-1]:
                    inRow += 1
                    try:
                        if plist[y+1][x-2] == plist[y+2][x-3]:
                            inRow += 1
                    except: pass
            except: pass
    except: pass
    if inRow >= 4:
        winn = True
    # \
    inRow = 1
    # Geht von links nach unten rechts
    try:
        if plist[y-1][x] == plist[y][x+1]:
            inRow += 1
            try:
                if plist[y+1][x+2] == plist[y-1][x]:
                    inRow += 1
                    try:
                        if plist[y+2][x+3] == plist[y][x+1]:
                            inRow += 1
                    except: pass
            except: pass
    except: pass

    # Geht von unten rechts nach oben links
    try:
        if plist[y-1][x] == plist[y-2][x-1]:
            inRow += 1
            try:
                if plist[y-3][x-2] == plist[y-1][x]:
                    inRow += 1
                    try:
                        if plist[y-4][x-3] == plist[y-1][x]:
                            inRow += 1
                    except: pass
            except: pass
    except: pass
    if inRow >= 4:
        winn = True

    if winn:
        if PlayerSymbole == emoji.green:
            winner.append(Player[0])
        else:
            winner.append(Player[1])
        winner.append(PlayerSymbole)
    

def place(nowPlayer,x):
    x = int(x) - 1
    symbol = ""
    try:
        if nowPlayer == Player[0]:
            symbol = emoji.green
    except:
        if len(Player) == 0:
            Player.append(nowPlayer)
            if nowPlayer == Player[0]:
                symbol = emoji.green
    try:
        if nowPlayer == Player[1]:
            symbol = emoji.red
    except:
        if nowPlayer != Player[0]:
            Player.append(nowPlayer)
            if nowPlayer == Player[1]:
                symbol = emoji.red
        try:
            if len(Player) > 2:
                return
        except:
            pass
    if p6[x] != emoji.white:
        if p5[x] != emoji.white:
            if p4[x] != emoji.white:
                if p3[x] != emoji.white:
                    if p2[x] != emoji.white:
                        if p1[x] != emoji.white:
                            return
                        else:
                            p1[x] = p1[x].replace(emoji.white,symbol)
                            y = 1
                    else: 
                        p2[x] = p2[x].replace(emoji.white,symbol)
                        y = 2
                else: 
                    p3[x] = p3[x].replace(emoji.white,symbol)
                    y = 3
            else: 
                p4[x] = p4[x].replace(emoji.white,symbol)
                y = 4
        else: 
            p5[x] = p5[x].replace(emoji.white,symbol)
            y = 5
    else: 
        p6[x] = p6[x].replace(emoji.white,symbol)
        y = 6
    win(symbol,x,y)
        


class MyClient(discord.Client):
    # Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt.")

    # Wenn Nachricht gepostet wird
    async def on_message(self, message):
        if message.author == client.user:
            return
        elif message.content.startswith("$clear"):
            Map4()
            winner.clear()
            Player.clear()
            PlayerLog.clear()
            PlayerLog.append(None)
            FullMap = MapText()
            await message.channel.send('Spielfeld ist geräumt')
            await message.channel.send(f"```{FullMap}```")

        elif message.content.startswith("help"):
            await message.channel.send('Say "$4 [x]" to play \n Say clear to start a new game')

        elif message.content.startswith("$4"):
            if message.author == PlayerLog[0]:
                await message.channel.send("Warte! Dein gegner hat seinen zug noch nicht gemacht.")
                return
            else:
                try:place_x = message.content.split(' ')[1]
                except:place_x = message.content.split('4')[1]
                place(message.author,place_x)
                try: FullMap = MapText([f"{emoji.green} {Player[0]}", "Spielt gegen",f"{emoji.red} {Player[1]}", f"{PlayerLog[0]} ist am zug"])
                except: FullMap = MapText("")
                try: await message.channel.send(f"```{FullMap} {winner[0]} {winner[1]} hat gewonnen```")
                except: await message.channel.send(f"```{FullMap}```")
                PlayerLog.clear()
                PlayerLog.append(message.author)



client = MyClient()
client.run("NzkwNjM5NzI1MTk4NDQyNTQ3.X-Dinw.sj3z7j21uu3NIxPSq4lN9kQiMRY")
