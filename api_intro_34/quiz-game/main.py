from data import question_data
from question_model import Question

question_game = Question()


for question in question_data:
    response = question_game.next_question(question)
    if response == question["answer"]:
        question_game.correct_res +=1
        print("Your response is correct")

    else: 
        print("Your response is incorrect")

    print("Score: {}/{}".format(question_game.correct_res, question_game.question_num))
    question_game.question_num += 1
