def load_questions(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    questions = []
    i=0
    while i<len(lines):
        if lines[i].strip()=="":
            i+=1
            continue

        question = lines[i].strip()
        options=[lines[i+1].strip(), lines[i+2].strip(), lines[i+3].strip(), lines[i+4].strip()]
        answer=int(lines[i+5].strip())
        questions.append({"question": question, "options": options, "answer": answer})
        i+=6

    return questions


def kbc_game():
    print("Welcome to Kaun Banega Crorepati!")
    print("answer the following questions , you will be given 4 choices for each question and according to that you will be given prize money ")
    print("so lets play then kaun banega crorepati!")

    file_path="questions.txt"
    questions=load_questions(file_path)

    prize_money=[1000, 5000, 10000, 50000]
    total_prize=0

    for i,q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for option in q["options"]:
            print(option)

        try:
            user_answer=int(input("enter your answer(1-4): "))
        except ValueError:
            print("Invalid input ,please enter a number from 1 and 4")
            continue

        if user_answer == q["answer"]:
           total_prize+=prize_money[i]
           print(f"correct!you won {prize_money[i]}.\n")
        else:
           print("wrong answer! game over")
           break

    print(f"Thanks for Playing! you've won a total prize of {total_prize}")

#if __name__=="main":
kbc_game()