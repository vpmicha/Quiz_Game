import random
import sys
from questions import questions
from datetime import date


keys = list(questions)
keys_used = list()

def main():
    for _ in range(10):
        score = random_select()
    best_score = scoring_system(score)
    retry = retry_system()
    save = saving_system(retry, score)

def random_select():
    for key in keys:
        key = random.choice(range(len(keys))) #len(keys) is the number of questions(30) in the list of questions, keys, which are copied from the dictionary
        if key not in keys_used:
            keys.append(key) #keys_used is a list of random numbers which correspond to an item from keys, the list which contains all the questions(copied form the dictionary)
            dict_value = questions[keys[key]] #keys[key] is the question from the dictionary copied to the list keys. question[keys[keys]] is the value which corresponds to the same key in the dictionary
            return quiz_validate(quiz_answers(keys[key]), dict_value) #keys[key] == dict_key/quiz_question from the dictionary/ quiz_answers returns the answer to the question of the dictionary
        else:
            continue

def quiz_answers(question):
    print(question)
    return input('Answer: ').strip().lower()

def quiz_validate(answer, question):
    score = 0
    if answer.strip().lower() == question:
        print('Correct')
        score += 1
    else:
        print('Incorrect')
        score += 0
    return score

def scoring_system(score):
    best_score = 0
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

def saving_system(retry, best_score):

    if not retry: #If player wants to end the game/doesnt want to retry
        try:
            with open('Quiz_Game HighScore', 'a') as file:
                file.write(f"On {date.today()}, the HighScore was {best_score}")
        except OSError:
            print('Could not save your HighScore to a file')
            sys.exit()

if __name__ == '__main__':
    main()

                



    

