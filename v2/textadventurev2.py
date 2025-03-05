from os import system, getcwd, listdir
class TextAdventure():
    def __init__(self, lang:int):
        
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
        Returns a list of filenames in the given directory path.
        """
        try:
            filenames = listdir(path)
            return filenames
        except FileNotFoundError:
            return f"Error: Directory not found: {path}"
        except NotADirectoryError:
            return f"Error: Not a directory: {path}"
        
    def StartGame(self, turns:int):
        import random, json, requests
        self.turns = turns
        self.extraturns = 0
        self.valids = 0
        
        if self.gameReady == 1:
            print("\nPlease wait while I choose words...")
            for turn in range(self.turns):
                # Changed code starts here
                
                with open(f'{self.dir_path}/wordlist-english.json') as wordlist:
                    load_word = json.load(wordlist)
                    word = random.choice(list(dict(load_word).keys()))
                api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
                response = requests.get(api_url, headers={'X-Api-Key': 'HNw+KdqDT14/u02rKgC+Dw==IdMSW7fPUKFbAyWf'})
                if response.status_code == requests.codes.ok:
                    
                    word2 = list(dict(eval(response.text)).values())[1]
                    if word2 != []:

                        self.valids += 1
                        ask = input(f"Find a synonym for {word}: ")
                        if ask in word2:
                            print("Correct!")
                            system("timeout -1")
                        else:
                            print("Incorrect! Moving on...")
                            system("timeout -1")
                    else:
                        
                        self.extraturns = 1

                else:
                    print("Error:", response.status_code, response.text)
                    self.extraturns = 1
                    print(self.extraturns)
            if self.extraturns != 0:
                while self.valids != turns:
                    system("cls")
                    self.StartGame(self.extraturns)
                exit()
textadv = TextAdventure(1)
textadv.StartGame(2)