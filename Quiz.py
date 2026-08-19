import sys
import random
from questions import questionsDict
from datetime import date

def main():
    used_questions = []
    questions10 = []
    answers10 = []
    questionsList = list(questionsDict)
    questions10 = get_10_questions(questionsList, questions10, used_questions)
    answers10 = ask_10_questions(questions10, answers10)

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
