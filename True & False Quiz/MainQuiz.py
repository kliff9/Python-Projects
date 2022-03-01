from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
#This Loops Each question and awnser in the question data to import into seperate unkown objects into the question bank
for x in question_data:
   text = x['text'] 
   answer = x['answer']
   question = Question(text, answer) 
   question_bank.append(question)

quiz = QuizBrain(question_bank)
print(quiz.question_number)
while quiz.still_has_question():
  quiz.newQuestion()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")



