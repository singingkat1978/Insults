#a script to insult people, because calling someone an asshole is just plain boring

import random

col1 = ["artless", "bawdy", "beslubbering", "bootless", "churlish",
        "cockered", "clouted", "craven", "currish", "dankish", "dissembling",
        "droning", "errant", "fawning", "fobbing", "froward", "frothy",
        "gleeking", "goatish", "gorbellied", "impertinent", "infectious",
        "jarring", "loggerheaded", "lumpish", "mammering", "mangled", "mewling",
        "paunchy", "pribbling", "puking", "puny", "qualling", "rank", "reeky",
        "roguish", "ruttish", "saucy", "spleeny", "spongy", "surly", "tottering",
        "unmuzzled", "vain", "venomed", "villainous", "warped", "wayward", "weedy",
        "yeasty"]
col2 = ["base", "bat", "beef", "beetle", "boil", "clapper", "clay", "common", "crook",
        "dismal", "dizzy", "dog", "dread", "earth", "elf", "fat", "fen", "flap",
        "fly", "folly", "fool", "full", "guts", "half", "hasty", "hedge", "hell", "idle", "ill",
        "knotty", "milk", "motley", "onion", "plume", "pottle", "pox", "reeling", "rough", "rude",
        "rump", "shard", "sheep", "spur", "swag", "tardy", "tickle", "toad", "unchin",
        "weather", "apple", "baggage", "barnacle", "bladder", "boar", "bug", "bum",
        "canker", "clack", "clot", "cox", "cod", "death", "dew",
        "flap", "flax", "flirt", "foot", "fustilarian", "giglet", "gudgeon", "haggard",
        "harpy", "hedge", "horn", "hugger", "joit", "lewdster", "lout", "maggot",
        "malt", "mammet", "measle", "minnow", "miscreant", "mold", "mumble", "nut", "pigeon",
        "pig", "puttock", "pumpion", "ratsbane", "scut", "skainsmate", "strumpet", "varlot",
        "vassal", "whey", "wag"]
col3 = ["court", "fowling", "witted", "headed", "brained", "clawed", "brained",
        "kissing", "pated", "dreaming", "eyed", "hearted", "bolted", "vexing",
        "skinned", "kidneyed", "sucked", "mouthed", "bitten", "fallen", "borne", "gorged",
        "griping", "faced", "witted", "hated", "breeding", "nurtured", "livered", "minded",
        "plucked", "deep", "marked", "ripe", "hewn", "growing", "fed", "biting", "galled",
        "bellied", "gaited", "brained", "spotted", "snouted", "john", "pig", "bear", "bailey",
        "blossom", "dish", "pole", "comb", "piece", "token", "berry", "dragon", "wench", "gill",
        "licker", "beast", "mugger", "head", "pie", "worm", "warp", "news", "hook", "egg",
        "nut", "face", "tail"]
col4 = ["bat", "beetle", "crook", "dog", "elf", "sheep", "toad", "barnacle", "boar", "bug", "bum", 
        "clod", "harpy", "lewdster", "lout", "maggot", "minnow", "miscreant", "pigeon",
        "pig", "pumpion", "strumpet", "bear", "dragon", "wench", "beast", "worm"]

player = input("Do you need an insult? ")

if player in ["Yes", "yes", "y", "Y"]:
    while player in ["Yes", "yes", "y", "Y"]:
        print (random.choice(col1) + " " + random.choice(col2) + "-" + random.choice(col3) +
           " " + random.choice(col2) + "-" + random.choice(col3) + " " + random.choice(col4))
        player = input("Do you need an insult? ")
    else:
        print("Goodbye!")

