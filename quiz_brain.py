class QuizBrain:

    def __init__(self, questions_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        """Checks if there are any questions left to answer."""
        if self.question_number < len(self.questions_list):
            return True

    def next_question(self):
        """Presents the next question to the user."""
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}. {current_question.text} True or False? ")
        solution = current_question.answer
        self.check_answer(answer, solution)

    def check_answer(self, answer, solution):
        """Checks if the user's answer is correct and updates the score."""
        if answer.lower() == solution.lower():
            self.score += 1
            print("You got it right!")
            if self.question_number < 11:
                print(f"Score: {self.score}/12")
        else:
            print(f"That's wrong. The correct answer was {solution}.")
        if self.question_number == 12:
            print(f"You've completed the quiz. Final score: {self.score}/12")
