import random
import time

class MathQuiz:
    def __init__(self):
        self.operations = ['+', '-', '*', '/']
        self.range_min = 0
        self.range_max = 999
        self.correct_answers = 0
        self.current_question = 1
        self.total_questions = 80
        self.time_left = 60  # in seconds

    def generate_number(self):
        # Randomly decide between whole number, decimal, or fraction
        choice = random.choice(['whole', 'decimal', 'fraction'])
        if choice == 'whole':
            return random.randint(int(self.range_min), int(self.range_max))  # Ensure integer range
        elif choice == 'decimal':
            return round(random.uniform(self.range_min, self.range_max), 3)
        elif choice == 'fraction':
            numerator = random.randint(1, 100)
            denominator = random.randint(1, 100)
            return f"{numerator}/{denominator}"
        else:
            return None

    def evaluate_fraction(self, fraction):
        numerator, denominator = map(int, fraction.split('/'))
        return numerator / denominator

    def evaluate_expression(self, a, b, operation):
        if isinstance(a, str):
            a = self.evaluate_fraction(a)
        if isinstance(b, str):
            b = self.evaluate_fraction(b)

        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a / b

    def generate_question(self):
        a = self.generate_number()
        b = self.generate_number()
        operation = random.choice(self.operations)

        correct_answer = self.evaluate_expression(a, b, operation)

        # Generate 3 incorrect but close options
        options = [correct_answer]
        for _ in range(3):
            if isinstance(correct_answer, (int, float)):
                wrong_answer = correct_answer + random.uniform(-5, 5)
            else:  # For fractions, add a small value to the numerator
                wrong_answer = correct_answer + random.uniform(-0.05, 0.05)
            while round(wrong_answer, 4) in [round(opt, 4) for opt in options]:
                if isinstance(correct_answer, (int, float)):
                    wrong_answer = correct_answer + random.uniform(-5, 5)
                else:
                    wrong_answer = correct_answer + random.uniform(-0.05, 0.05)
            options.append(wrong_answer)

        random.shuffle(options)
        return (f"What is {a} {operation} {b}?", correct_answer, options)

    def start_quiz(self):
        start_time = time.time()
        for i in range(80):
            question, correct_answer, options = self.generate_question()
            print(f"Q{i+1}: {question}")
            for j, option in enumerate(options):
                print(f"{j+1}: {option:.4f}")  # Limit options to 4 decimal points

            user_answer = int(input("Your choice (1-4): "))
            selected_answer = options[user_answer - 1]

            if round(selected_answer, 4) == round(correct_answer, 4):
                self.correct_answers += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer:.4f}")

            # Check if time is up
            if time.time() - start_time >= 8 * 60:
                print("Time's up!")
                break

        print(f"You answered {self.correct_answers} questions correctly out of {i+1}.")

if __name__ == "__main__":
    quiz = MathQuiz()
    quiz.start_quiz()
