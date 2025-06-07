from django.shortcuts import render, redirect,get_object_or_404

from .models import Student

def student_list(request):
    students=Student.objects.all()
    return render(request,'vast_app/student_list.html',{'student':students}) 


def student_create(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        course=request.POST['course']
        contact=request.POST['contact']
        Student.objects.create(name=name,email=email,course=course,contact=contact)
        return redirect('list')
    return render(request,'vast_app/student_create.html')

def student_update(request,pk):
    students=get_object_or_404(Student,pk=pk)
    
    if request.method=='POST':
        students.name=request.POST.get['name']
        students.email=request.POST.get['email']
        students.course=request.POST.get['course']
        students.contact=request.POST.get['contact']
        
        students.save()
        return redirect('list')
        
    return render(request,'vast_app/student_create.html',{'student':students})

def student_delete(request,pk):
    students=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        students.delete()
        return redirect('list')
    return render(request,'vast_app/delete.html',{'student':students})