# My word game
## v1
Uses a full local list of everything in the English dictionary, one word per file, 100K+ word files. Everything is coded as a class for maximum flexibility.\
\
By default, it starts with 2 turns.
### Flowchart
Get list of all word files > Choose random file > Read word from file > Ask user for synonym
If synonym valid, say so and continue
If invalid synonym, say so and continue
## v2
Contacts api-ninjas.com to search in a thesaurus for a random word chosen with wordlist-english.json\
\
By default, it starts with 10 turns, with all the code inside a class
### Flowchart
Choose word from json > Look it up at api-ninjas > Prompt user for synonym
If word is found in api response, say 'Correct!' and move on
If word is not found in response, say 'Incorrect', display valid synonyms, and move on.
## v3
Uses the Datamuse API to look up a random word found in wordlist-english.json. It also contains an XP system for the user to use.\
\
By default, it starts with 10 turns, with all code in a class.
### Flowchart
Get list of all words from json > Choose random word > Check if word has synonym > if synonym found, ask user for synonym > if not, repeat
If synonym valid, say so, award xp, and continue
If invalid synonym, say so, revoke xp, and continue

