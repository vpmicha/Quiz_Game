import sys
import random
from questions import questionsDict
from datetime import date

questions10 = []
used_questions = []

def main():
    questionsList = list(questionsDict)
    get_10_questions(questionsList, questions10)

def get_10_questions(qList, q10):
    for _ in range(10):
        q = random.choice(range(len(qList)))
        if q not in used_questions:
            q10.append(qList[q])
        else:
            continue
    return q10

        






