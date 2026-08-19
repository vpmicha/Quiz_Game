import sys
import random
from questions import questionsDict
from datetime import date

used_questions = []

def main():
    questionsList = list(questionsDict)
    questions10 =get_10_questions(questionsList, questions10)
    answers10 = ask_10_questions(questions10, answers10)

def get_10_questions(qList, q10):
    for _ in range(10):
        q = random.choice(range(len(qList)))
        if q not in used_questions:
            q10.append(qList[q])
            
        else:
            continue
    return q10

def ask_10_questions(q10, a10):
    for question in q10:
        print(question)
        a10.append(input('Answer: ').strip().lower())
    return a10









