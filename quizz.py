from ClassQuizz.question import Question
from numpy.random import randint
question_promo = [
    "What color are apples?\n (a)Red (b)Green (c)Black (D)Yellow",
    "What color are Banana?\n (a)Red (b)Green (c)Black (D)Yellow",
    "What color are Stawberries?\n (a)Red (b)Green (c)Black (D)Yellow",
    "What is 1 + 1"
]

congratulations =[
    'Good Job!',
    'Amazing!',
    'Excellent!',
    'Wow!'
]

Ouranswer = [
    'a',
    'd',
    'a',
    2,
]

questions = []

for i in range(len(question_promo)):
    questions.append(Question(i,question_promo[i],Ouranswer[i]))

def rand(congratulations):
    x = randint(0,len(questions))
    return congratulations[x]

def run_test(questions):
    score = 0
    for question in questions:
        if(questions.index(question) == 3):
            print("Question " + str(question.number + 1) + ": " + question.question)
            try:
                answer = int(input('Nhap dap an: '))
                if answer == question.answer:
                    score += 1
                    print(rand(congratulations))
                else:
                    score = 0
                    print('Stupid!!')
            except:
                print('Invaild Value')
        else:
            print("Question " + str(question.number+1) + ": " + question.question)
            answer = input('Chon dap an: ')
            if answer == question.answer:
                score += 1
                print(rand(congratulations) + ' You got 1 score\n')
    print("Total: "+ str(score) + "/"+str(len(questions)) + "correct")

run_test(questions)
