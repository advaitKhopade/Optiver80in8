from django.contrib import admin
from django.urls import path
from quiz.views import quiz_view, feedback_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feedback_view, name='home'),  # Use the feedback view as the home page
    path('quiz/', quiz_view, name='quiz'),
    path('feedback/', feedback_view, name='feedback'),  # Feedback form submission
]
