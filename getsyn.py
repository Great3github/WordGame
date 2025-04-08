import json, requests, random, os
def get_syns(word:str, checkmode:bool):
    """
    Gets synonyms for any word using the Datamuse API
    """
    api_url = 'https://api.datamuse.com/words?ml={}'.format(word)
    response = requests.get(api_url)
    
    approved = []
    for i in list(eval(response.text)):
        try:
            if list(dict(i)['tags'])[0] == 'syn':
                approved.append(dict(i)['word'])
        except: break
    if checkmode == True and approved != []: return "Success"
    elif approved == [] and checkmode == True: return "Error"
    if approved == []: return "Error"
    return approved
def get_ants(word:str, checkmode:bool):
    api_url = 'https://api.datamuse.com/words?rel_ant={}'.format(word)
    response = requests.get(api_url)
    ants = []
    for i in list(eval(response.text)):
        ants.append(dict(i)['word'])
    
    if checkmode == True and ants != []: return "Success"
    elif ants == [] and checkmode == True: return "Error"
    if ants == []: return "Error"
    return ants
def random_lookup(word:str, lang:int, popup:bool):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    """
    Get a random output from the Datamuse API. 1 for English, 2 for Spanish
    """
    
    types = ['ml', 'sl', 'sp', 'rel_jja', 'rel_jjb', 'rel_syn', 'rel_trg', 'rel_ant', 'rel_spc', 'rel_gen', 'rel_com', 'rel_bga', 'rel_bgb', 'rel_hom', 'rel_cns', 'lc', 'rc']
    type = random.choice(types)
    if lang == 1: api_url = 'https://api.datamuse.com/words?{}={}'.format(type, word)
    else: api_url = 'https://api.datamuse.com/words?ml={}&v=es'.format(word)
    
    response = requests.get(api_url)
    return response.text

    