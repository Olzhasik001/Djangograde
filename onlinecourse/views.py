from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Submission, Question, Choice

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        enrollment = Enrollment.objects.get(user=request.user, course=course)
        submission = Submission.objects.create(enrollment=enrollment)
        for question in course.question_set.all():
            for choice in question.choice_set.all():
                if str(choice.id) in request.POST.getlist('choice_' + str(question.id)):
                    submission.choices.add(choice)
        submission.save()
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    context = {
        'course': get_object_or_404(Course, pk=course_id),
        'score': 80,
        'passed': True
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)