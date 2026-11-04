from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Submission, Question, Choice

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=1)
    return render(request, 'onlinecourse/exam_result_bootstrap.html', {'course': course})

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course,
        'score': 80,
        'passed': True
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
