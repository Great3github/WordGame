import json, requests
def get_syns(word:str):
    """
    Gets synonyms for any word using the Datamuse API
    """
    api_url = 'https://api.datamuse.com/words?ml={}'.format(word)
    response = requests.get(api_url)
    
    approved = []
    for i in list(eval(response.text)):
        if list(dict(i)['tags'])[0] == 'syn':
            approved.append(dict(i)['word'])
    if approved == []: print("No synonyms found, or the word is invalid.")
    return approved
