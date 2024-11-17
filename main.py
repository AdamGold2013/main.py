meme_dict = {
            "LOL": "very funny",
            "CRINGE": "something wierd",
            "SHEESH": "nice",
            "SKIBIDI": "evil, not cool",
            "FANUM TAX": "to steal",
            "SIGMA": "handsome",
            "BRUH": "dude",
            "OHIO": "this word is a name for a us state but it also means: something wierd",
            "GYAT": "sorry this word is not appropriate"
            }
while True:
    word = input("print in a modern word you don't understand (In capital letters!) if you don't get you're answer that means the word is not found: ")
    if word in "LOL":
        print("very funny")
    elif word in "CRINGE":
        print("something wierd")
    elif word in "SHEESH":
        print("nice")
    elif word in "SKIBIDI":
        print("evil, not cool")
    elif word in "FANUM TAX":
        print("to steal")
    elif word in "SIGMA":
        print("handsome")
    elif word in "BRUH":
        print("dude")
    elif word in "OHIO":
        print("this word is a name for a us state but it also means: something very wierd, insane")
    elif word in "GYAT":
        print("sorry this word is not appropriate")
    elif word in meme_dict.keys() == False:
        print('Error, sorry word not found')
