import sys
import random
from questions import questionsDict
from datetime import date

def main():
    retry = False
    while retry:
        used_questions = []
        questions10 = []
        answers10 = []
        questionsList = list(questionsDict)
        questions10 = get_10_questions(questionsList, questions10, used_questions)
        answers10 = ask_10_questions(questions10, answers10)
        score = validate(questions10, answers10)
        print(f'{score}/10')


def get_10_questions(qList, q10, used_q):
    while True:
        q = random.choice(range(len(qList)))
        if q not in used_q:
            q10.append(qList[q])
            used_q.append(q)
            if len(q10) == 10:
                break
        else:
            continue
    return q10

def ask_10_questions(q10, a10):
    for question in q10:
        print(question)
        a10.append(input('Answer: ').strip().lower())
    return a10

def validate(q10, a10):
    score = 0
    for a, q in zip(a10, q10):
        if a == questionsDict[q]:
            print('Correct')
            score += 1
        else:
            print('Incorrect')
            score = score
    return score
