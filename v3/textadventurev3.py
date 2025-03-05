from os import system, getcwd, listdir

class TextAdventure():
    def __init__(self, lang:int):
        self.extraturns = 0
        self.valids = 0
        self.repeated = 0
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
        
    def StartGame(self, turns:int, xp_on:bool):
        import random, json, requests, xp, getsyn
        self.turns = turns
        xpsystem = xp.XP(850, 1000, 0, 0, 50, 100)
        if self.gameReady == 1:
            print("\nPlease wait while I find words with synonyms...")
            for turn in range(self.turns):
                # Changed code starts here
                
                with open(f'{self.dir_path}\\wordlist-english.json') as wordlist:
                    load_word = json.load(wordlist)
                    word = random.choice(list(dict(load_word).keys()))
                
                if True:
                    
                    word2 = getsyn.get_syns(word)
                    if word2 != []:

                        self.valids += 1
                        if self.valids <= turns:
                            self.extraturns += 1
                        else:
                            pass
                        ask = input(f"Find a synonym for {word}: ")
                        if ask in word2:
                            print("Correct!")
                            if xp_on == True: xpsystem.award_xp(random.randint(0, xpsystem.xp_per_level))
                            system("timeout -1")
                        else:
                            print("Incorrect! Correct synonyms are:")
                            
                            print(word2)
                            if xp_on == True: xpsystem.revoke_xp(random.randint(0, xpsystem.xp_per_level))
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
textadv.StartGame(10, True)