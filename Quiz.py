import sys
import random
from questions import questionsDict, indices
from datetime import date


def main():
    highscore = 0
    while True:
        used_questions = []
        questions10 = []
        answers10 = []
        questionsList = list(questionsDict)
        questions10 = get_10_questions(questionsList, questions10, used_questions)
        all_time_highscore = get_all_time_highscore(highscore)
        answers10 = ask_10_questions(questions10, answers10, all_time_highscore, highscore)
        scores = validate(questions10, answers10, highscore, all_time_highscore)
        score = scores[0]
        highscore = scores[1]
        all_time_highscore = scores[2]
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
            print(question)
            a10.append(input('Answer: ').strip().lower())
        return a10
    except (EOFError, KeyboardInterrupt):
        sys.exit('Thank you for playing!')

def validate(q10, a10, highscore, all_time_highscore):
    score = 0
    for a, q, i in zip(a10, q10, indices):
        if a == questionsDict[q].lower().strip():
            print(f'{i}: Correct')
            score += 1
        else:
            print(f'{i}: Incorrect')
    if score >= highscore:
        highscore = score
    if score >= all_time_highscore:
        all_time_highscore = score
    return [score, highscore, all_time_highscore]

def save_highscore(highscore):
    while True:
        r = input('Do you want to play again?(Yes/No) ').strip().lower()
        if r == 'yes':
            return True
        elif r == 'no':
            try:
                with open('HighScore.txt', 'a') as file:
                    file.write(f'On {date.today()} the HighScore was: {highscore}\n')
                return 'Stop'
            except OSError:
                sys.exit('Could not save HighScore to a file, sorry.')

def get_all_time_highscore(highscore):
    lines = []
    past_scores = []
    try:
        with open('HighScore.txt', 'r') as file:
            for line in file:
                lines.append(line)

            for line in lines:
                _, past_highscores = line.split(': ')
                past_highscores = past_highscores.strip().lower()
                past_scores.append(int(past_highscores))
            
            past_highscore = 0
            for i in range(len(past_scores)):
                if past_highscore <= past_scores[i]:
                    past_highscore = past_scores[i]
        if past_highscore <= highscore:
            past_highscore = highscore

    except (OSError, ValueError, IndexError):
        past_highscore = 0

    return past_highscore

if __name__ == '__main__':
    main()

