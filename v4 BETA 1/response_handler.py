# ui-main.py
from __future__ import print_function, unicode_literals
from os import system
system("py -m pip install PyInquirer")



import PyInquirer
from pprint import pprint


style = PyInquirer.style_from_dict({
    PyInquirer.Token.Separator: '#cc5454',
    PyInquirer.Token.QuestionMark: '#673ab7 bold',
    PyInquirer.Token.Selected: '#cc5454',  # default
    PyInquirer.Token.Pointer: '#673ab7 bold',
    PyInquirer.Token.Instruction: '',  # default
    PyInquirer.Token.Answer: '#f44336 bold',
    PyInquirer.Token.Question: '',
})

def inquire(separator:str, itemnames:list, message:str, name:str):
    
    questions = [
        {
            'type': 'list',
            'message': message,
            'name': name,
            'choices': [PyInquirer.Separator(f'= {separator} =')],
            'validate': lambda answer: 'You must choose at least one response.' \
                if len(answer) == 0 else True
        }
    ]
    for item in range(len(itemnames)):
        if isinstance(itemnames[item], list):
            
            for item2 in range(len(itemnames[item])):
                
                dict(questions[0])['choices'].append(str(list(itemnames[item])[item2]))
                
        
    answers = PyInquirer.prompt(questions, style=style)
    
    return answers
