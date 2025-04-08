from os import system, getcwd, listdir

class TextAdventure():
    def __init__(self, lang:int):
        import xp
        self.extraturns = 0
        self.wskips = 0
        self.valids = 0
        self.repeated = 0
        self.hold_xp = 0
        self.xpsystem = xp.XP(850, 1000, self.hold_xp, 0, 50, 100)
        self.shopitems = {
            'XP bonus': ['ADDXP', 250, 20],
        }
        import json
        from os import system, getcwd, path
        print("You must have an active internet connection to play this game!")
        system("timeout -1")
        
        self.dir_path = path.dirname(path.realpath(__file__))
        self.lang = lang
        if not isinstance(self.lang, int) or self.lang not in [1, 2, 3]:
            raise Exception("Valid language codes are: 1 for english, and 2 for Spanish.")
        elif self.lang == 1:
            self.gameReady = 1
        else:
            raise Exception("Currently only English is supported. Stay tuned for updates!")
    def get_filenames_list(self, path):
        """
        Returns a list of filenames in the given directory path. [OLD - will be removed sometime soon]
        """
        try:
            filenames = listdir(path)
            return filenames
        except FileNotFoundError:
            return f"Error: Directory not found: {path}"
        except NotADirectoryError:
            return f"Error: Not a directory: {path}"
    def ShowMenu(self):
        from response_handler import inquire
        menu1 = inquire("Choose an option", ["Go to the Point Shop", "Continue playing"], "WordGame Menu", "Response1")
        if menu1['Response1'] == "Go to the Point Shop":
            self.PointShop()
        else:
            self.StartGame(10,True)
    def PointShop(self):
        from response_handler import inquire
        def confirm_purchase(item):
            shop2 = inquire(f"Are you sure you want to buy {item}?", ['Yes', 'No'], 'Point Shop', 'Response3')
            if shop2['Response3'] == 'Yes': return True
            if shop2['Response3'] == 'No': return False
        shop1 = inquire("Choose an item", [list(self.shopitems.keys()), "Exit"], 'Point Shop', 'Response2')
        if shop1['Response2'] in list(self.shopitems.keys()):
            if self.shopitems[shop1['Response2']][0] == 'ADDXP':
                if confirm_purchase(shop1['Response2']): pass
                else: self.PointShop()
                self.xpsystem.points -= self.shopitems[shop1['Response2']][2]
                self.xpsystem.award_xp(self.shopitems[shop1['Response2']][1])
    def StartGame(self, turns:int, xp_on:bool):
        import random, json, requests, xp, getsyn
        from response_handler import inquire
        system("cls")
        self.turns = turns
        
        
        if self.gameReady == 1:
            print("\nPlease wait while I find words with synonyms...")
            for turn in range(self.turns):
            
                word = "DONOTCHANGEME"
                while getsyn.get_syns(word, True) == "Error":
                    with open(f'{self.dir_path}\\wordlist-english.json') as wordlist:
                        load_word = json.load(wordlist)
                        word = random.choice(list(dict(load_word).keys()))
                    if f"{word}.bak" in self.get_filenames_list(f"{self.dir_path}\\badwords"): continue
                    if getsyn.get_syns(word, True) in [[], "Error"]:
                        with open(f'{self.dir_path}\\badwords\\{word}.bak', "x") as badfile:
                            badfile.write(f"{word}")
                        pass

                # need to remove this soon
                if True:
                    
                    word2 = getsyn.get_syns(word, False)
                    if word2 != [] and getsyn.get_ants(word, False) != "Error" and getsyn.get_syns(word, False) != "Error":

                        self.valids += 1
                        if self.valids <= turns:
                            self.extraturns += 1
                        else:
                            pass
                        response = inquire("Answer", [getsyn.get_ants(word, False), getsyn.get_syns(word, False)], f"Choose a synonym for {word}", "Response")
                        if response['Response'] in word2:
                            print("Correct!")
                            if xp_on == True: self.xpsystem.award_xp(random.randint(0, self.xpsystem.xp_per_level))
                            system("timeout -1")
                        else:
                            print("Incorrect! Correct synonyms are:")
                            
                            print(word2)
                            if xp_on == True: self.xpsystem.revoke_xp(random.randint(0, self.xpsystem.xp_per_level))
                            system("timeout -1")
                    else:
                        
                        self.extraturns =+ 1

                else:
                    print("Error:", response.status_code, response.text)
                    self.extraturns =+ 1
                    print(self.extraturns)
            if self.extraturns != 0:
                for repeat in range(self.extraturns):
                    system("cls")
                    
                    self.repeated = 1
                    self.StartGame(self.extraturns, xp_on)
                
textadv = TextAdventure(1)
textadv.PointShop()
print(textadv.get_filenames_list(f"{textadv.dir_path}\\badwords"))
