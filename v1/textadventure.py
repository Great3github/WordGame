from os import system, getcwd, listdir
class TextAdventure():
    def __init__(self, lang:int):
        import json
        from os import system, getcwd, path
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
        import random, json
        self.turns = turns
        filename_list = self.get_filenames_list(f"{self.dir_path}/textadventure-lang/words-english/files/")
        if self.gameReady == 1:
            for turn in range(self.turns):
                wordfile = random.choice(filename_list)
                with open(f"{self.dir_path}/textadventure-lang/words-english/files/{wordfile}", "r") as file:
                    wordjson = json.load(file)
                    old = list(dict(wordjson).values())[4]
                    jdump_old = json.dumps(old)
                if str(list(dict(wordjson).values())[4]) != "[]" or [] or None:
                    print(f"using file {wordfile}...")
                    wordask = input(f"Find a synonym for {list(dict(wordjson).values())[2]}: ")
                    if wordask.lower() in list(dict(wordjson).values())[4]:
                        print("Correct!")
                    else:
                        print("Incorrect! The correct answers were:")
                        print(list(dict(wordjson).values())[4])
                        rewrite = input("Is there a mistake in my sources? [Y/N] [NONFUNCTIONAL - DO NOT USE]: ")
                        if rewrite == "y" or "Y":
                            
                            rewrite2 = input("Add, Delete, Modify or exit? > ")
                            if rewrite2 == "add":
                                clist = list(dict(wordjson).values())[4]
                                add = input("Type string to add, or type _exit to exit. > ")
                                if add != "_exit":
                                    clist.append(add)
                                    print(clist)
                                    system("timeout -1")
                                    system(f"{self.dir_path}\\fart.exe {self.dir_path}\\textadventure-lang\\words-english\\files\\{wordfile} '{jdump_old}' '{json.dumps(clist)}'")
                                    print(jdump_old)
                                    print(json.dumps(clist))
                                    exit()
                elif list(dict(wordjson).values())[4] == []:
                    print("invalid word, skipping")
                    self.turns = self.turns + 1
                    continue
textadv = TextAdventure(1)
textadv.StartGame(2)