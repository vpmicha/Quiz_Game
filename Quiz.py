import random
from questions import questions

keys = list(questions)
keys_used = list()
best_score = 0
score = 0

def main():
    for _ in range(10):
        score = random_select()
    best_score = scoring_system(score)
    retry = retry_system()

def random_select():
    for key in keys:
        key = random.choice(len(keys)) #len(keys) is the number of questions(30) in the list of questions, keys, which are copied from the dictionary
        if key not in keys_used:
            key.append(keys_used) #keys_used is a list of random numbers which correspond to an item from keys, the list which contains all the questions(copied form the dictionary)
            dict_value = questions[keys[key]] #keys[key] is the question from the dictionary copied to the list keys. question[keys[keys]] is the value which corresponds to the same key in the dictionary
            return quiz_validate(quiz_answers(keys[key]), dict_value) #keys[key] == dict_key/quiz_question from the dictionary/ quiz_answers returns the answer to the question of the dictionary
        else:
            continue

def quiz_answers(question):
    print(question)
    return input('Answer ').strip().lower()

def quiz_validate(answer, question):
    if answer.strip().lower() == question:
        print('Correct')
        score += 1
    else:
        print('Incorrect')
        score = score
    return score

def scoring_system(score):
    if score >= best_score:
        best_score = score
        return best_score
    else:
        return best_score

def retry_system():
    retry = input('Do you want to retry? ').lower().strip()
    if retry == 'yes':
        return True
    else:
        return False


    

