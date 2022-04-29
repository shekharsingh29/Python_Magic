class Question:
    def __init__(self):
        self.question_num = 1
        self.correct_res = 0

    def next_question(self, question):
        print("{} ) {} ? Please respond True/False. \n".format(self.question_num, question["text"]))
        return input("Response: ")





