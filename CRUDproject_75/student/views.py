from django.shortcuts import get_object_or_404, redirect, render
from .models import Student
from .forms import StudentForm
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'student/home.html'
    def get(self, request, *args, **kwargs):
        students = Student.objects.all().order_by('roll_number')
        form = StudentForm()
        return render(request, self.template_name, {'students': students, 'form': form})
    
    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
        students = Student.objects.all().order_by('roll_number')
        return render(request, self.template_name, {'students': students, 'form': form})


class UpdateStudent(TemplateView):
    template_name='student/update.html'
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(instance=student)

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'student': student
            }
        )

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('home')

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'student': student
            }
        )

class DeleteStudent(TemplateView):
    def get(self, request, roll_number):
            student = get_object_or_404(
                Student,
                roll_number=roll_number
            )

            student.delete()

            return redirect('home')