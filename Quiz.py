import random
from questions import questions

keys = list(questions)
keys_used = list()
score = 0

def quiz_answers(question):
    print(question)
    return input('Answer ').strip().lower()

def quiz_validate(answer, question):
    if answer.strip().lower() == question:
        score += 1
    else:
        score = score
    return score
        



for key in keys:
    key = random.choice(len(keys)) #len(keys) is the number of questions(30) in the list of questions, keys, which are copied from the dictionary
    if key not in keys_used:
        key.append(keys_used) #keys_used is a list of random numbers which correspond to an item from keys, the list which contains all the questions(copied form the dictionary)
        dict_value = questions[keys[key]] #keys[key] is the question from the dictionary copied to the list keys. question[keys[keys]] is the value which corresponds to the same key in the dictionary
        quiz_validate(quiz_answers(keys[key]), dict_value) #keys[key] == dict_key/quiz_question from the dictionary/ quiz_answers returns the answer to the question of the dictionary
        break
    else:
        continue
    

