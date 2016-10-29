# Mashup Who
# It's Doctor Who...put in a blender.

import random, time

import textwrap

from PIL import Image, ImageFont, ImageDraw

import tweepy
from keys2 import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

user = api.me()

Doctor_List = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth",
          "Tenth", "Eleventh", "Twelfth"]

Companion_List = ["Rose", "Susan", "Clara", "Martha", "Ace", "Peri", "Jo", "Sarah", "Romana", "K9",
                  "Turlough", "Mel", "Frobisher", "Jamie", "Liz", "Amy", "Adric", "Nyssa", "Bernice",
                  "the Brigadier", "Leela", "Donna", "Steven", "Sam", "Evelyn", "Charley"]

Place_List =["Mondas", "Telos", "Midnight", "Karfel", "Earth", "Mars", "Peladon", "Androzani Major",
              "Vortis", "Marinus", "the prison planet Desperus", "the peaceful Traken Union", "New Earth", "Draconia", "Metebelis 3",
              "the Eye of Orion", "Spiridon", "Zeta Minor", "Karn", "Kastria", "Gallifrey", "Pluto",
              "Ribos", "Tara", "Atrios", "Eden", "Skonnos", "Argolis", "Alzarius", "Terradon", "Frontios",
              "Jaconda", "Varos", "Segonax", "Necros", "Svartos", "the Moon", "a space station",
              "an undersea base", "Ancient Rome", "Cardiff", "London", "New York", "Hong Kong", "12th century England",
             "Atlantis", "Brighton", "19th century Yorkshire", "Essex", "an interstellar liner",
             "an abandoned hypervessel", "an advanced research station", "Paris in 1979", "Aridius", "Melbourne", "Tibet",
             "Tigella", "Slough", "Shepherds Bush", "Ealing", "Sarn", "Thoros Beta", "Buenos Aires", "Platform One",
             "a barren ice planet", "a harsh desert planet", "a lush jungle planet", "Alfava Metraxis", "Darillium",
             "18th century Cornwall", "Hull", "New Orleans", "Renaissance Italy", "1980s Seville", "1980s Amsterdam", "Deva Loka",
             "Asgard","Azure","Bonarcha Anarda","Dulkis","Florana","Galsec Seven","Hyspero","Inter Minor","Kahler","Kantra","Kaldor",
             "Krontep","Lakertya","Lobos","Melissa Majoria","Messaline","New Alexandria","New Venus","Obsidian","Red Rocket Rising",
             "Riftan Five","Salvak","Shan Shen","the fifth moon of Sinda Callesta","Sirius IV","Terra Alpha","Trion","Vulpana",
             "Woman Wept","Xeros","Xeriphas","Zeen 4","17th century England", "Aberdeen", "Croydon", "the village of Little Hodcombe",
             "the village of Cheldon Boniface", "Leadworth", "Devil's End", "Demons Run", "Carbury, beside Vortigern's Lake",
             "the end of the universe", "the beginning of time"]

Monster_List =["Vervoids", "Daleks", "Sontarans", "Cybermen", "Weeping Angels", "Zygons", "Slitheen", "Drahvins",
              "Macra", "Krotons", "Nestene", "Axons", "Kraals and their androids", "Rutans", "(and profit hungry) Usurians", "Nimon",
              "Magnus Greel and his Peking Homunculus", "Chronovores", "Ice Warriors", "Vardans",
              "Tractators", "(and easily bored) Gods of Ragnarok", "Gelth", "Sycorax", "Racnoss", "Carrionites", "Pyroviles",
              "Silents", "Headless Monks", "Sandmen", "Shakri", "Autons", "Wirrn", "Voord",
              "Krynoids", "Ogrons", "Jagaroth", "Krillitane", "Davros and an armada of his Daleks", "Missy and an army of Cybermen",
               "Master and an army of killer robots", "Futurekind", "Family of Blood", "Vashta Nerada",
               "Great Intelligence controlling a horde of Yeti-like robots", "(no really!) Bandrils, armed with bendalypse warheads", "Drashigs", "Movellans",
               "Mandrels","Gaztaks","Terileptils and their androids", "Eternals", "(and profit hungry) Mentors", "Chelonians", "Mire",
               "Eknodine","Queen Xanxia and her space hopping planet Zanak","nucleus of the Swarm"]

Team_List = ["Marco Polo", "Dr. Samuel Johnson", "Captain Jack Harkness", "Professor River Song", "Queen Elizabeth I",
             "an honourable Ice Lord", "some Judoon", "William Shakespeare", "the Shadow Proclamation", "some Thals", "UNIT",
             "Kate Lethbridge-Stewart", "Alpha Centauri", "a group of Draconians", "a friendy Exxillon", "Torchwood",
             "Charles Darwin", "Charles Dickens", "Winston Churchill", "Dr. Grace Holloway", "the Sisterhood of Karn",
             "the White Guardian", "the mathematicians of Logopolis", "the Face of Boe", "Brigadier Bambera", "Strax",
             "Madame Vastra and Jenny", "Clyde and Rani", "a Zygon duplicate of Osgood", "Mickey Smith", "Wilfred Mott", "Craig Owens and Sophie",
             "shape-changing android Kamelion", "incompetent journalist Jeremy Fitzoliver", "Iris Wildthyme", "a Lurman theatre troupe",
             "Harry Sullivan", "a Knight of the Grand Order of Oberon", "Professor Chronotis", "some surviving Menoptera", "an escaped Tharil",
             "Minnie and the Silver Cloak", "a Chimeron queen escaping from bounty hunters", "the Moxx of Balhoon",
             "a small group of disaffected rebels", "Drax", "Rodan", "Sergeant Benton", "Captain Yates", "Captain Avery and his pirate crew",
             "a Scotland Yard policeman found unconscious in a drawer", "an out of work actor minding a restaurant for a friend",
             "leading flower artist Amelia Ducat", "Professor Amelia Rumford", "Binro the Heretic", "a group of Outlers",
             "the Royal Navy", "a squadron of Spitfires", "Charlotte Bronte", "a crashed spaceship of Rills and Chumblies",
             "Dorium Maldovar", "a Teselecta duplicate of the Doctor", "Commodore 'Tonker' Travers"]

Monster_Adjective_List = ["fearsome", "murderous", "villainous", "terrifying", "evil", "dastardly", "merciless", "pitiless"]

Threat_List = ["menaced", "threatened", "occupied", "under attack", "overrun", "beseiged", "half destroyed", "invaded", "taken over", "controlled",
               "infiltrated"]

Deus_List = ["by using the sonic screwdriver", "by initiating Time Ram", "by engaging them in a battle of wits",
             "by giving them a stern talking to", "by leading an uprising", "by causing them never to have existed",
             "by tricking them into blowing up their own planet", "by reversing the polarity of the neutron flow",
             "by triggering a ray phase shift", "by using the Hand of Omega", "by activating the Time Destructor",
             "by releasing deadly hexachromite gas", "by letting the Brigadier blow them up", "by sabotaging their computers",
             "by trapping them in their own universe", "by fighting a duel for the planet",
             "by sending their ships into an orbit around the Sun", "by using a metal virus", "by entombing them in their bunker",
             "by making them experience emotions", "by tripping them up with the Doctor's scarf", "by harnessing the positive energy of everyone on the planet",
             "by accelerating their life-cycle", "by separating them from their leader, rendering the remainder harmless", "by erasing them from time with the Demat gun",
             "by dropping them into a crack in space-time", "when the Doctor uses his own regeneration energy against the invaders",
             "by alerting the planet to the catastrophe, having already experienced it in a parallel universe",
             "by convincing them that further fighting would be dishonourable",
             "by rendering them unable to distinguish themselves from the population they have invaded",
             "by reassembling a Time Lord statue made of Validium","by harnessing the energy released by the Blinovitch Limitation Effect",
             "when they prove unable to cope with a companion's foolhardy act of self-sacrifice","by encouraging them to play the Game of Rassilon"]
             
count = 0

print("Places:")
print(len(Place_List))

print("Monsters:")
print(len(Monster_List))

print("Allies:")
print(len(Team_List))

print("Endings:")
print(len(Deus_List))

while count < 12000:

    #Generate story string
    Doctor = random.choice(Doctor_List)

    Companion = random.choice(Companion_List)

    Place = random.choice(Place_List)
    Monster = random.choice(Monster_List)
    Team = random.choice(Team_List)
    Deus = random.choice(Deus_List)
    Threat = random.choice(Threat_List)
    Monster_Adjective = random.choice(Monster_Adjective_List)


    story1 = "The TARDIS brings the " + Doctor + " Doctor and " + Companion + " to " + Place + "," + " only to find it " + Threat + " by the " + Monster_Adjective + " " + Monster + ". "
    story2 = "With the help of " + Team + "," + " the Doctor and " + Companion + " defeat them " + Deus + "."
    story = story1 + story2
    story = textwrap.fill(story, 54)

    print("\nVworp Vworp!...")
    print(story)

    # Turn text into JPEG
    img = Image.open("template.jpg")
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype("nunito-light.ttf", 26)
    regular_font = ImageFont.truetype("nunito-light.ttf", 22)
    draw.text((225,55),"Vworp Vworp!",(0,0,0),font=title_font)
    draw.text((20, 100),story,(0,0,0),font=regular_font) # second set of numbers represent colour
    img.save("story.jpg")
    print("\nImage generated")

    # Tweet image    
    tweet = api.update_with_media("story.jpg")
    print("Adventure tweeted")

    count += 1
    print("Sleeping now...")
    time.sleep(600)
    
    
