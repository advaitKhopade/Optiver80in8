from django.shortcuts import render, redirect
from django.http import HttpResponse
from .math_quiz import MathQuiz

def quiz_view(request):
    quiz = MathQuiz()
    question, correct_answer, options = quiz.generate_question()

    if request.method == "POST":
        selected_option = request.POST.get('option')
        if selected_option:
            selected_option = float(selected_option)
            correct = round(selected_option, 3) == round(correct_answer, 3)
            
            if correct:
                quiz.correct_answers += 1
                
            quiz.current_question += 1
            
            if quiz.current_question > quiz.total_questions:
                return redirect('quiz_result')
            
            question, correct_answer, options = quiz.generate_question()

    context = {
        'question': question,
        'options': options,
        'current_question': quiz.current_question,
        'total_questions': quiz.total_questions,
        'time_left': quiz.time_left,
    }
    return render(request, 'quiz_page.html', context)

def quiz_result(request):
    quiz = MathQuiz()
    context = {
        'total_questions': quiz.total_questions,
        'correct_answers': quiz.correct_answers,
    }
    return render(request, 'quiz_result.html', context)

def feedback_view(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user_ip = request.META.get('REMOTE_ADDR')
        
        # You can save the feedback and IP to a database or send it to your email.
        print(f"Feedback received: {comment}")
        print(f"From IP: {user_ip}")
        
        # Redirect back to home after submitting feedback
        return redirect('home')
    return render(request, 'quiz_home.html')
