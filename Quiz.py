from os import SCHED_OTHER
import sys
import random
from questions import questionsDict
from datetime import date


def main():
    highscore = 0
    while True:
        used_questions = []
        questions10 = []
        answers10 = []
        questionsList = list(questionsDict)
        questions10 = get_10_questions(questionsList, questions10, used_questions)
        all_time_highscore = get_all_time_highscore()
        answers10 = ask_10_questions(questions10, answers10, all_time_highscore, highscore)
        score = validate(questions10, answers10, highscore)
        print(f'{score}/10')
        retry = save_highscore(highscore)
        if retry == 'Stop':
            sys.exit('Thank you for playing!')

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

def ask_10_questions(q10, a10, aths, chs):
    try:
        for question in q10:
            print(f'All time HighScore: {aths}/Current HighScore: {chs}')
            print(chs)
            print(question)
            a10.append(input('Answer: ').strip().lower())
        return a10
    except (EOFError, KeyboardInterrupt):
        sys.exit('Thank you for playing!')

def validate(q10, a10, highscore, all_time_highscore):
    score = 0
    for a, q in zip(a10, q10):
        if a == questionsDict[q]:
            print(f'{a10.index()}: Correct')
            score += 1
        else:
            print(f'{a10.index()}: Incorrect')
            score = score
    if score >= highscore:
        highscore = score
    if score >= all_time_highscore:
        all_time_highscore = score
    
    return score

def save_highscore(highscore):
    while True:
        r = input('Do you want to play again?(Yes/No) ').strip().lower()
        if r == 'Yes':
            return True
        elif r == 'No':
            try:
                with open('HighScore.txt', 'a') as file:
                    file.write(f'On {date.today()} the HighScore was: {highscore}.')
                return 'Stop'
            except OSError:
                sys.exit('Could not save HighScore to a file, sorry.')

def get_all_time_highscore():
    lines = []
    try:
        with open('HighScore.txt', 'r') as file:
            for line in file:
                lines.append(line)
            last_line = lines[-1]
            _, last_highscore = last_line.split(': ')
            last_highscore = last_highscore.strip('.')
    except OSError:
        last_highscore = 0

    return last_highscore



