import discord
import asyncio
import random
import pickle
import time
import os
print("Loading... ")

global jackpot
jackpot = 0

hashing = "stopdigging"
values = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101, ' ': 103, '0': 107, '1': 109, '2': 113, '3': 127, '4': 131, '5': 137, '6': 139, '7': 149, '8': 151, '9': 157, '.': 163, ',': 167, 'å' : 173, 'ä' : 179, 'ö' : 181, 'A' : 191, 'B' : 193,  'C' : 197, 'D' : 199, 'E' : 211, 'F' : 223, 'G' : 227, 'H' : 233, 'I' : 239, 'J' : 241, 'K' : 251, 'L' : 257, 'M' : 263, 'N' : 263, 'O' : 269, 'P' : 271, 'Q' : 277, 'R' : 283, 'S' : 293, 'T' : 307, 'U' : 311, 'V' : 313, 'W' : 317, 'X' : 331, 'Y' : 337, 'Z' : 347, 'Å' : 349, 'Ä' : 353, 'Ö' : 359}

pi = 3.14

def cutoffHash(password):
    hashing = str(password)
    if len(hashing) > 2:
        if len(hashing) > 3:
            if len(hashing) > 4:
                if len(hashing) > 5:
                    if len(hashing) > 6:
                        if len(hashing) > 7:
                            if len(hashing) > 8:
                                if len(hashing) > 9:
                                    if len(hashing) > 10:
                                        if len(hashing) > 11:
                                            if len(hashing) > 12:
                                                if len(hashing) > 13:  
                                                    if len(hashing) > 14:
                                                        if len(hashing) > 15:
                                                            if len(hashing) > 16:
                                                                if len(hashing) > 17:
                                                                    if len(hashing) > 18:
                                                                        if len(hashing) > 19:
                                                                            if len(hashing) == 20:
                                                                                password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]] * values[hashing[10]] * values[hashing[11]] * values[hashing[12]] * values[hashing[13]] * values[hashing[14]] * values[hashing[15]] * values[hashing[16]] * values[hashing[17]] * values[hashing[18]] * values[hashing[19]]
                                                                            else:
                                                                                password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]] * values[hashing[10]] * values[hashing[11]] * values[hashing[12]] * values[hashing[13]] * values[hashing[14]] * values[hashing[15]] * values[hashing[16]] * values[hashing[17]] * values[hashing[18]]
                                                                        else:
                                                                            password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]] * values[hashing[10]] * values[hashing[11]] * values[hashing[12]] * values[hashing[13]] * values[hashing[14]] * values[hashing[15]] * values[hashing[16]] * values[hashing[17]]
                                                                    else:
                                                                        password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]] * values[hashing[10]] * values[hashing[11]] * values[hashing[12]] * values[hashing[13]] * values[hashing[14]] * values[hashing[15]] * values[hashing[16]]
                                                                else:
                                                                    password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]] * values[hashing[10]] * values[hashing[11]] * values[hashing[12]] * values[hashing[13]] * values[hashing[14]] * values[hashing[15]]
                                                            else:
                                                                password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]] * values[hashing[10]] * values[hashing[11]] * values[hashing[12]] * values[hashing[13]] * values[hashing[14]]
                                                        else:
                                                            password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]] * values[hashing[10]] * values[hashing[11]] * values[hashing[12]] * values[hashing[13]]
                                                    else:
                                                        password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]] * values[hashing[10]] * values[hashing[11]] * values[hashing[12]]
                                                else:
                                                    password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]] * values[hashing[10]] * values[hashing[11]]
                                            else:
                                                password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]] * values[hashing[10]]
                                        else:
                                            password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]] * values[hashing[9]]
                                    else:
                                        password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]] * values[hashing[8]]
                                else:
                                    password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]] * values[hashing[7]]
                            else:
                                password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]] * values[hashing[6]]
                        else:
                            password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]] * values[hashing[5]]
                    else:
                        password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]] * values[hashing[4]]
                else:
                    password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]] * values[hashing[3]]
            else:
                password = values[hashing[0]] * values[hashing[1]] * values[hashing[2]]
        else:
            password = values[hashing[0]] * values[hashing[1]]
    else:
        print ("Too short.")


    return password


class cao:
    black = "\033[30m"
    gray = "\033[2m"
    reset = "\033[0m"
    darkRed = "\033[31m"
    red = "\033[91m"
    darkGreen = "\033[32m"
    green = "\033[92m"
    darkYellow = "\033[33m"
    yellow = "\033[93m"
    darkBlue = "\033[34m"
    blue = "\033[94m"
    darkPurle = "\033[35m"
    purple = "\033[95m"
    darkCyan = "\033[36m"
    cyan = "\033[96m"
    bold = "\033[1m"
    italic = "\033[3m"
    underline = "\033[4m"
    whiteHighlight = "\033[7m"
    strikethrough = "\033[9m"

faltecCreditsOutputRaw = "" # Output thing that we'll do later
faltecCreditsRawInt = 2 # This starts at 2 so that it'll choose the letter 2 paces ahead for later
with open("faltecsave.faltec", "r") as faltecSaveFile: # Open the file
    faltecSaveContent = faltecSaveFile.read() # Read the file and store it's contents in this variable
    faltecCreditsRaw, faltecHistoryRaw = faltecSaveContent.split("|") # Split the contents of the variable we stored before to differentiate credits from history

faltecCredits = eval(faltecCreditsRaw)

"""{
    '213252576957825024' : leoCredits, # Leo
    '192266786559885322' : teoCredits, # Teo
    '264013801932718081' : eliasCredits, # Elias
    '309662642778275840' : fredrikCredits, # Fredrik
    '291160703547604993' : antonCredits, # Anton
    '294375877289181184' : carlCredits, # Carl
    '370637848866455556' : faltecBotCredits, # FaltecBot
    '395361984801144832' : faltecKasinoCredits, # FaltecKasino (pengar temporär)
    'eliasPenshop' : eliasPenshopCredits,
    'kasinoJackpot' : kasinoJackpotCredits # Jackpot vinst i slot machine
}"""

faltecCreditsHistory = eval(faltecHistoryRaw)

"""{
    'leo' : [''],
    'teo' : [''],
    'elias' : [':'],
    'fredrik' : [''],
    'anton' : [''],
    'carl' : [''],
}"""

faltecIds = {
    'leo' : 213252576957825024, 
    'teo' : 192266786559885322,
    'elias' : 264013801932718081,
    'fredrik' : 309662642778275840,
    'anton' : 291160703547604993,
    'carl' : 294375877289181184,
    'mobileElias' : 368678351021539328,
    'faltecBot': 370637848866455556,
    'faltecKasino' : 395361984801144832,
}


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message_delete(message):
    print('\n' + str(message.author) + '\'s message got deleted: ' + message.content + '\n')

@client.event
async def on_message(message):
    slotMachine = [":cherries:", ":strawberry:", ":grapes:", ":peach:", ":pear:",
                   ":watermelon:", ":pineapple:", "<:FALTEC:422810411998380042>"]
    # Fun stuff
    if len(message.content) > 300 and not int(message.author.id) == 370637848866455556 and not int(message.author.id) == 172002275412279296:
        book = message.content.split(' ')
        tldr1 = random.choice(book) + " "
        tldr2 = random.choice(book) + " "
        tldr3 = random.choice(book) + " "
        tldr4 = random.choice(book) + " "
        tldr5 = random.choice(book) + " "
        tldr6 = random.choice(book) + " "
        await client.send_message(message.channel, "**TLDR: **" + tldr1 + tldr2 + tldr3 + tldr4 + tldr5 + tldr6)
    if message.content.lower == "k" and message.author.id == faltecIds["fredrik"]:
        await client.send_message(message.channel, 'Verkar som Fredrik inte bryr sig :/')
    if "pixop" in message.content.lower() and not int(message.author.id) == 370637848866455556:
        await client.send_message(message.channel, 'Pixop!')
    
    
    # Fun commands
    if message.content.startswith('?leaderboard'):
        await client.send_message(message.channel, 'https://mee6.xyz/leaderboard/333984467288850436')
    if message.content.startswith('?riktighacker'):
        await client.send_message(message.channel, '83.249.166.50')
    if message.content.startswith('?snabbtengwar'):
        await client.send_message(message.channel, 'https://i.imgur.com/ra40Upd.png')
    if message.content.startswith('?tänker'):
        await client.send_message(message.channel, '*Drar med händerna längs med sitt långa gråa skägg*')
    if message.content.startswith('?uttal'):
        await client.send_message(message.channel, 'https://i.imgur.com/u494eC9.png')
    if message.content.startswith('?view'):
        await client.send_message(message.channel, "**Allas credits:**\n" + '**Fredrik: **' + str(faltecCredits["309662642778275840"]) + ' Credits' + '\n**Anton: **' + str(faltecCredits["291160703547604993"]) + ' Credits' + '\n**Leo: **' + str(faltecCredits["213252576957825024"]) + ' Credits' + '\n**Teo: **' + str(faltecCredits["192266786559885322"]) + ' Credits' + '\n**Elias: **' + str(faltecCredits["264013801932718081"]) + ' Credits' + '\n**Carl: **' + str(faltecCredits["294375877289181184"]) + ' Credits')
    
    # Useful stuff
    async def circleAreaCalculator(r):
        if r.isdigit():
            r = float(r)
            a = r ** 2 * pi
            await client.send_message(message.channel, '**Cirkelns area är: **' + str(a))
        elif r.isalpha():
            await client.send_message(message.channel, '**Du skrev ingen siffra**')
        else:
            r = float(r)
            a = r ** 2 * pi
            await client.send_message(message.channel, '**Cirkelns area är: **' + str(a))

    async def circleOmkretsCalculator(r):
        if r.isdigit():
            r = float(r)
            o = r * 2 * pi
            await client.send_message(message.channel, '**Cirkelns omkrets är: **' + str(o))
        elif r.isalpha():
            await client.send_message(message.channel, '**Du skrev ingen siffra**')
        else:
            r = float(r)
            o = r * 2 * pi
            await client.send_message(message.channel, '**Cirkelns omkrets är: **' + str(o))

    if message.content.startswith('?circle area'):
        junkCircle, junkArea, circleRadius = message.content.split(" ")
        await circleAreaCalculator(circleRadius)

    if message.content.startswith('?circle omkrets'):
        junkCircle, junkArea, circleRadius = message.content.split(" ")
        await circleOmkretsCalculator(circleRadius)

    #### CASINO ####
    # Slot Machine
    if message.content.startswith('::spin'):
        spinJunk, amount = message.content.split(' ')
        amount = int(amount)
        if amount % 2 == 0 and amount <= 500:
            # PAY COMMAND HERE
            global jackpot
            jackpot += amount / 2
            returnAmount = 0
            spinResults = [random.choice(slotMachine), random.choice(slotMachine), random.choice(slotMachine), ]
            comparisonList = []
            spinWinCode = 0
            jackpotState = False
            for result in spinResults:  # Loops every result in spin result (3x)
                if result not in comparisonList:
                    comparisonList.append(result)  # It'll add the result to the list
                    # When the for loop comes again it'll check the list to see if the item already exists, so it's a duplicate and adds 1 to the spin win code
                    print(comparisonList)
                else:
                    spinWinCode += 1
                    print(str(spinWinCode))
            if spinResults == ["<:FALTEC:422810411998380042>", "<:FALTEC:422810411998380042>", "<:FALTEC:422810411998380042>"]:
                jackpotState = True
            print("Jackpot is now: " + str(jackpot))
            spinMessage = await client.send_message(message.channel, "Spinning...")
            await client.edit_message(spinMessage, "Spinning...\n" + spinResults[0])
            time.sleep(1)
            await client.edit_message(spinMessage, "Spinning...\n" + spinResults[0] + spinResults[1])
            time.sleep(1)
            await client.edit_message(spinMessage, "Spinning...\n" + spinResults[0] + spinResults[1] + spinResults[2])
            time.sleep(0.5)
            if spinWinCode == 0:
                await client.edit_message(spinMessage, "Spinning...\n" + spinResults[0] + spinResults[1] + spinResults[2] + "\nDu förlorade " + str(amount) + "₡!")
            elif spinWinCode == 1:
                await client.edit_message(spinMessage, "Spinning...\n" + spinResults[0] + spinResults[1] + spinResults[2] + "\nDu vann " + str(amount*2) + "₡!")
            elif spinWinCode == 2 and jackpotState == False:
                await client.edit_message(spinMessage, "Spinning...\n" + spinResults[0] + spinResults[1] + spinResults[2] + "\nDu vann " + str(amount*3) + "₡!")
            elif spinWinCode == 2 and jackpotState == True:
                await client.edit_message(spinMessage, "Spinning...\n" + spinResults[0] + spinResults[1] + spinResults[2] + "\nDU FICK JAAAACKPOOOTT!!!")
                jackpotState = False
        else:
            await client.send_message(message.channel, "Antingen försöker du lägga in ett udda antal Credits vilket inte är möjligt, eller så har du lagt in för mycket Credits, max Credits är 500₡")


    # Help
    if message.content.startswith('?help'):
        await client.send_message(message.channel, """**__Commands:__**
**Knasiga commands:**
 • ?leaderboard - Skickar länken till mee6 lvl leaderboarden
 • ?riktighacker - Visar IP Adressen till en idiot
 • ?snabbtengwar - Visar de flesta bokstäver i Tengwar alfabetet
 • ?uttal - Visar hur man uttalar alla bokstäver i Sindarin
 • ?tänker - Använd när någon frågar något och du tänker på ett svar
 
**Användbara commands:**
 • ?ch-<text> - Hashar meddelandet du skriver, t.ex: `?hash-test` kommer hasha ordet test, ordet kan max vara 20 bokstäver långt
 • ?circle area <radie> - Räknar ut arean på en cirkel från <radie>
 • ?circle omkrets <radie> - Räknar ut omkretsen på en cirkel från <radie>
 
**Credit commands:**
 • ?credits - Visar hur många credits du har
 • ?credits <person> - Visar hur många credits <person> har
 • ?credits send <antal> <person> <anledning> - Skickar <antal> credits till <person> på grund av <anledning>
 • ?credits history - Visar alla transaktioner du har genomfört
 
**Bank commands:**
 • ~~?bank loan <antal> <anledning> - Fråga efter ett <antal> credits lån från banken på grund av <anledning>~~
 
**Casino commands:**
 • ::slots <antal> - Använd en slot machine, den väljer 3 random frukter och beroende på vad som kommer fram vinner du olika mycket. \n2st av samma frukt: 2x<antal>, 3st av samma frukt: 4x<antal>, 3st FALTEC: JACKPOT
 • ~~::roulette <antal> <färg> - Om det blir din färg får du tillbaka <antal> * 2, om du valde grön och det sen blev grön så får du tillbaka <antal> * 14
Det finns 13 röda rutor, 13 svarta rutor 2 gröna rutor~~"""
)

    if message.content.startswith('?ping'):
        print (message.content)
        print (message.author.id)
        print (message.channel)
        await client.send_message(message.channel, "**Meddelande: **" + str(message.content))
        await client.send_message(message.channel, "**Skrivare: **" + str(message.author.id))
        await client.send_message(message.channel, "**Kanal: **" + str(message.channel))
        await client.send_message(message.channel, "Pong!")
    
    # Gain credits
    if not message.content.startswith('?') and not message.content.startswith('::'):
        lastMessage = message.content
        lastAuthor = int(message.author.id)
        nameJunk = str(message.author)
        writerName, nameJunkTheSequel = nameJunk.split("#")
        creditsAmount = random.randint(0, 5)
        print (cao.green + writerName + cao.reset + "(" + str(message.channel) + ")" + " : " + str(lastMessage) + cao.blue + " (" + str(lastAuthor) + ")" + cao.reset)
        if lastAuthor == faltecIds["fredrik"]:
            print (cao.yellow + "Fredrik got " + str(creditsAmount) + " Credits!" + cao.reset)
            faltecCredits["309662642778275840"] += creditsAmount
        if lastAuthor == faltecIds["anton"]:
            print (cao.yellow + "Anton got " + str(creditsAmount) + " Credits!" + cao.reset)
            faltecCredits["291160703547604993"] += creditsAmount
        if lastAuthor == faltecIds["leo"]:
            print (cao.yellow + "Leo got " + str(creditsAmount) + " Credits!" + cao.reset)
            faltecCredits["213252576957825024"] += creditsAmount
        if lastAuthor == faltecIds["teo"]:
            print (cao.yellow + "Teo got " + str(creditsAmount) + " Credits!" + cao.reset)
            faltecCredits["192266786559885322"] += creditsAmount
        if lastAuthor == faltecIds["elias"] or lastAuthor == faltecIds["mobileElias"]:
            print (cao.yellow + "Elias got " + str(creditsAmount) + " Credits!" + cao.reset)
            faltecCredits["264013801932718081"] += creditsAmount
        if lastAuthor == faltecIds["carl"]:
            print (cao.yellow + "Carl-Johan got " + str(creditsAmount) + " Credits!" + cao.reset)
            faltecCredits["294375877289181184"] += creditsAmount
    
    # Check credits
    if message.content.startswith('?credits') and ' ' not in message.content:
        pointerChecker = int(message.author.id)
        print (str(message.author) + " has viewed their credits!")
        if pointerChecker == faltecIds["fredrik"]:
            await client.send_message(message.channel, str(faltecCredits["309662642778275840"]) + ' Credits')
        elif pointerChecker == faltecIds["anton"]:
            await client.send_message(message.channel, str(faltecCredits["291160703547604993"]) + ' Credits')
        elif pointerChecker == faltecIds["leo"]:
            await client.send_message(message.channel, str(faltecCredits["213252576957825024"]) + ' Credits')
        elif pointerChecker == faltecIds["teo"]:
            await client.send_message(message.channel, str(faltecCredits["192266786559885322"]) + ' Credits')
        elif pointerChecker == faltecIds["elias"] or pointerChecker == faltecIds["mobileElias"]:
            await client.send_message(message.channel, str(faltecCredits["264013801932718081"]) + ' Credits')
        elif pointerChecker == faltecIds["carl"]:
            await client.send_message(message.channel, str(faltecCredits["294375877289181184"]) + ' Credits')
        elif pointerChecker == faltecIds["faltecKasino"]:
            await client.send_message(message.channel, str(faltecCredits["395361984801144832"]) + ' Credits')

    #Check other peoples credits
    if message.content.startswith('?credits ') and 'send' not in message.content and 'history' not in message.content:
        firstPart, otherUserStageOne = message.content.split(" ")
        otherUser = str(otherUserStageOne.lower())
        if otherUser == "fredrik":
            print (str(message.author) + " has checked Fredrik's credits!")
            await client.send_message(message.channel, 'Fredrik har ' + str(faltecCredits["309662642778275840"]) + ' Credits')
        if otherUser == "anton":
            print (str(message.author) + " has checked Anton's credits!")
            await client.send_message(message.channel, 'Anton har ' + str(faltecCredits["291160703547604993"]) + ' Credits')
        if otherUser == "leo":
            print (str(message.author) + " has checked Leo's credits!")
            await client.send_message(message.channel, 'Leo har ' + str(faltecCredits["213252576957825024"]) + ' Credits')
        if otherUser == "teo":
            print (str(message.author) + " has checked Teo's credits!")
            await client.send_message(message.channel, 'Teo har ' + str(faltecCredits["192266786559885322"]) + ' Credits')
        if otherUser == "elias":
            print (str(message.author) + " has checked Elias's credits!")
            await client.send_message(message.channel, 'Elias har ' + str(faltecCredits["264013801932718081"]) + ' Credits')
        if otherUser == "calle" or otherUser == "carl" or otherUser == "carl-johan" or otherUser == "carl johan":
            print (str(message.author) + " has checked Calle's credits!")
            await client.send_message(message.channel, 'Carl har ' + str(faltecCredits["294375877289181184"]) + ' Credits')
        if otherUser == "kasino" or otherUser == "falteckasino" and str(message.author.id) == "213252576957825024":
            print (str(message.author) + " has checked Kasinons credits!")
            await client.send_message(message.channel, 'Kasinot har ' + str(faltecCredits['395361984801144832']) + ' Credits')

    #View transfers
    if message.content.startswith('?credits history'):
        pointerChecker = int(message.author.id)
        print(str(message.author) + " has viewed their payment history!")
        print(str(pointerChecker))
        if pointerChecker == faltecIds["fredrik"]:
            await client.send_message(message.channel, "\n".join(faltecCreditsHistory['fredrik']))
        elif pointerChecker == faltecIds["anton"]:
            await client.send_message(message.channel, "\n".join(faltecCreditsHistory['anton']))
        elif pointerChecker == faltecIds["leo"]:
            await client.send_message(message.channel, "\n".join(faltecCreditsHistory['leo']))
        elif pointerChecker == faltecIds["teo"]:
            await client.send_message(message.channel, "\n".join(faltecCreditsHistory['teo']))
        elif pointerChecker == faltecIds["elias"] or pointerChecker == faltecIds["mobileElias"]:
            await client.send_message(message.channel, "\n".join(faltecCreditsHistory['elias']))
        elif pointerChecker == faltecIds["carl"]:
            await client.send_message(message.channel, "\n".join(faltecCreditsHistory['carl']))
    
    #Cutoff Hash
    if message.content.startswith('?ch'):
        chJunk, word = message.content.split("-")
        if len(word) <= 20 and len(word) >= 2:
            chWord = cutoffHash(word)
            print (str(message.author) + " hashade ordet " + str(word) + " och det blev " + str(chWord))
            await client.send_message(message.channel, "**Din hash är:**\n" + str(chWord))
            
    # Transfer
    if message.content.startswith("?credits send "):
        switch_one = False
        switch_two = False
        noSender = 0
        noReciever = 0
        sendJunk, sendJunkTheSequel, amount_raw, reciever, reason = message.content.split(" ")
        simpleReciever = reciever.lower()
        simpleAuthor = 'null'
        sender = str(message.author.id)
        amount = int(amount_raw)
        if int(message.author.id) == faltecIds["fredrik"]:
            simpleAuthor = 'fredrik'
        elif int(message.author.id) == faltecIds["anton"]:
            simpleAuthor = 'anton'
        elif int(message.author.id) == faltecIds["leo"]:
            simpleAuthor = 'leo'
        elif int(message.author.id) == faltecIds["teo"]:
            simpleAuthor = 'teo'
        elif int(message.author.id) == faltecIds["elias"] or message.author.id == faltecIds["mobileElias"]:
            simpleAuthor = 'elias'
        elif int(message.author.id) == faltecIds["carl"]:
            simpleAuthor = 'carl'
        if amount < 1000000:
            for ident in faltecIds:
                if reciever.lower() == ident:
                    reciever = str(faltecIds[ident])
            # Verification that the account exists.
            for profile in faltecCredits:
                if sender == profile and faltecCredits[profile] >= amount and amount > 0 and switch_one == False:
                    switch_one = True
                    noSender = 1
                if reciever == profile and switch_two == False:
                    switch_two = True
                    noReciever = 1
            # Sending the value.
            for profile in faltecCredits:
                if sender == profile and switch_one == True and switch_two == True:
                    faltecCredits[profile] = faltecCredits[profile] - amount
                if reciever == profile and switch_one == True and switch_two == True:
                    faltecCredits[profile] = faltecCredits[profile] + amount
                    await client.send_message(message.channel, "Skickade " + str(amount) + " credits till <@" + reciever + "> ")
                    print (str(message.author) + " --- " + str(amount) + " ---> " + simpleReciever.capitalize())
                    faltecCreditsHistory[simpleAuthor].insert(0, '**' + time.strftime("%d/%m/%Y") + '**' + ': Skickade du ' + str(amount) + ' Credits till ' + simpleReciever.capitalize() + ' På grund av: **' + reason + '**')
                    faltecCreditsHistory[simpleReciever].insert(0, '`' + time.strftime("%d/%m/%Y") + ': Skickade ' + simpleAuthor.capitalize() + ' ' + str(amount) + ' Credits till dig på grund av: ' + reason + '`')
            if noSender ==  0:
                await client.send_message(message.channel, "Du har inte tillräckligt mycket credits för att genomföra den här transaktionen")
                print (str(message.author) + " försökte skicka för mycket till " + simpleReciever.capitalize())
            if noReciever == 0:
                await client.send_message(message.channel, "Personen som du försöker skicka till finns inte eller så skicka du för mycket (eller negativt)")
                print (str(message.author) + " försökte skicka " + str(amount) + " till en person som inte fanns (" + reciever + ")")
        else:
            await client.send_message(message.channel, "Du försöker skicka lite mycket nu.")
        switch_one = False
        switch_two = False
        noSender = 0
        noReciever = 0
    with open("faltecsave.faltec", "w") as faltecSaveFile:
        faltecSaveFile.truncate()
        faltecSaveFile.write(str(faltecCredits) + "|" +  str(faltecCreditsHistory))
            
client.run('not for you')
