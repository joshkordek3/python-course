class list (list):
    def contains (self, item):
        return self.count(item) > 0

class Quiz:
    def __init__ (self, questions, number):
        self.questions = questions
        self.answers = list()
        self.questionNumber = "not started"
        self.quizNumber = number
        self.tries = 0

    def begin (self):
        self.tries += 1
        self.questionNumber = 1
        self.answers = []
        while self.questionNumber <= len(self.questions):
            question = self.questions[self.questionNumber - 1]
            print("")
            print(f"Question {self.questionNumber}:")
            print(indent(1, question.text))
            for i in range(len(question.answers)):
                answer = question.answers[i]
                print(indent(2, f"{alphabet[i].upper()}: {answer.text}"))
            print("")
            answer = input("What is your answer? (input letter) ").lower()
            while (alphabet.count(answer) == 0) or len(answer) > 1 or answer == "" or alphabet.index(answer) >= len(question.answers):
                answer = input("Sorry, I didn't quite catch that, what's your answer? (input letter) ").lower()
            self.answers.append(question.answers[alphabet.index(answer)])
            self.questionNumber += 1

        print("")
        correct = 0
        for i in range(len(self.questions)):
            question = self.questions[i]
            print(f"Question {i + 1}: ")
            print(indent(1, f"Correct answer: {question.correctAnswer.text}"))
            print(indent(1, f"Your answer: {self.answers[i].text}"))
            status = "Wrong"
            if self.answers[i] == question.correctAnswer:
                status = "Correct"
                correct += 1
            print(indent(1, f"State: {status}"))
            print("")
        print(f"Final score: {correct}/{len(self.questions)}")
        if correct == len(self.questions):
            print("Congrats! You got all of the questions correct!")
        else:
            questionsWrong = f"{len(self.questions) - correct} questions"
            if questionsWrong == "1 questions":
                questionsWrong = questionsWrong.rstrip("s")
            tryAgain = input(f"Oops, you got {questionsWrong} wrong, try again? (yes/no) ").lower()
            while not (tryAgain == "yes" or tryAgain == "no"):
                tryAgain = input("Please input yes or no. ").lower()
            if tryAgain == "yes":
                self.begin()
                return
        tries = f"{self.tries} tries"
        if tries == "1 tries":
            tries = tries.rstrip("ies")
            tries += "y"
            tries = "only " + tries
        print(f"\nQuiz number {self.quizNumber} done with {tries}!")

class Question:
    def __init__ (self, question, answers):
        if len(answers) > 26:
            raise TypeError("Can't provide more than 26 answers to one question")
        if len(answers) < 2:
            raise ReferenceError("Can't have less than 2 answers")
        self.answers = answers
        for i in range(len(answers)):
            if self.check(answers[i]):
                self.correctAnswer = answers[i]
                break
        self.text = question

    def check (self, answerGiven):
        for answer in self.answers:
            if answer == answerGiven and answer.isCorrect:
                return True
        return False

class Answer:
    def __init__ (self, text, correct):
        self.text = text
        self.isCorrect = correct

def indent (number, text):
    for i in range(number):
        text = "  " + text
    return text

alphabet = "abcdefghijklmnopqrstuvwxyz"
quizzes = [
    Quiz([
        Question("What does 'raise' do in Python?", [
            Answer("It throws an error", True),
            Answer("It's not a keyword", False),
            Answer("It raises a block of code to execute earlier", False),
            Answer("It makes the program higher priority than the others", False)
        ]),
        Question("What is a Raspberry Pi's operating system?", [
            Answer("Linux", True),
            Answer("Windows", False),
            Answer("Mac OS", False),
            Answer("Chrome OS", False)
        ])
    ], 1)
]
quizNumber = 0
while quizNumber < len(quizzes):
    quizzes[quizNumber].begin()
    if quizNumber + 1 == len(quizzes):
        print("\nYou have completed all of the quizzes!")
        break
    nextQuiz = input(f"Would you like to do the next quiz? (yes/no) ").lower()
    while not (nextQuiz == "yes" or nextQuiz == "no"):
        nextQuiz = input("Please input yes or no. ").lower()
    if nextQuiz == "yes":
        quizNumber += 1
        continue
    print("\nSee you later! :)")
