from ClassQuizz.question import Question

question_promo = [
    "What color are apples?\n (a)Red (b)Green (c)Black (D)Yellow",
    "What color are Banana?\n (a)Red (b)Green (c)Black (D)Yellow",
    "What color are Stawberries?\n (a)Red (b)Green (c)Black (D)Yellow",
    "What is 1 + 1 \n"
]

questions = [
    Question(question_promo[0],'a'),
    Question(question_promo[1],'d'),
    Question(question_promo[2],'a'),
    Question(question_promo[3],2),
]


def run_test(questions):
    score = 0
    for question in questions:
        if(questions.index(question) == 3):
            print(question.question)
            try:
                answer = int(input('Nhap dap an: '))
                if answer == question.answer:
                    score += 1
                    print('You got 1 score')
                else:
                    score = 0
                    print('Stupid!!')
            except:
                print('Invaild Value')
        else:
            print(question.question)
            answer = input('Chon dap an: ')
            if answer == question.answer:
                score += 1
                print('You got 1 score')
    print("Total: "+ str(score) + "/"+str(len(questions)) + "correct")

run_test(questions)
