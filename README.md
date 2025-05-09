# My word game
## MASSIVE update coming soon! Here are the details:
- Faster method: This update brings a new method of choosing words, where whenever it finds a word without a synonym, it creates a file at ./badwords/{word}.bak. Whenever it tries a word and it is in this file list, it skips going online to find out if it's a synonym and just moves on to the next word
- v2 UI: Starting from this version, WordGame will now use PyInquirer for all of its menus and questions.
- Questions Update: From this version on, all questions will be multiple choice
- Points: A new point shop with all-new powerups will be added, and will use the Points that were introduced in v3.
- Game Menu: A new game menu is in the works, serving as the 'title screen menu' that most games have
- More options for customization: With this new update, it will be easier to customize the point shop items, powerup counts, etc.
### A beta version has been released, and most of these features are now available! There are still some bugs that will be fixed in the official release.
## Plans for future updates
- Saving progress to a file
- Adding more powerups
## v1
Uses a full local list of everything in the English dictionary, one word per file, 100K+ word files. Everything is coded as a class for maximum flexibility.\
\
By default, it starts with 2 turns.
### Flowchart
Get list of all word files > Choose random file > Read word from file > Ask user for synonym\
If synonym valid, say so and continue\
If invalid synonym, say so and continue
## v2
Contacts api-ninjas.com to search in a thesaurus for a random word chosen with wordlist-english.json\
\
By default, it starts with 10 turns, with all the code inside a class
### Flowchart
Choose word from json > Look it up at api-ninjas > Prompt user for synonym\
If word is found in api response, say 'Correct!' and move on\
If word is not found in response, say 'Incorrect', display valid synonyms, and move on.
## v3
Uses the Datamuse API to look up a random word found in wordlist-english.json. It also contains an XP system for the user to use.\
\
By default, it starts with 10 turns, with all code in a class.
### Flowchart
Get list of all words from json > Choose random word > Check if word has synonym > if synonym found, ask user for synonym > if not, repeat.\
If synonym valid, say so, award xp, and continue\
If invalid synonym, say so, revoke xp, and continue

