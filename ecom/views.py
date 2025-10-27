from django.shortcuts import render, redirect
from .forms import studentForm, contactForm,contacteForm

# def member(request):
#     return HttpResponse("Hello world")

def home(request):
    return render(request, 'file1.html')

def student_view(request):
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_view')
    else:
        form = studentForm()
    return render(request, 'student.html', {'form': form})

    

def contact_view(request):  

    if request.method == "POST":
        form =contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_view')
    else:
        form = contactForm()
    return render(request, 'contact.html', {'form': form})


def contacte_view(request):
    if request.method == "POST":
        form =contacteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacte_view')
    else:
        form = contacteForm()
    return render(request, 'contacte.html', {'form': form})





  

        





# Create your views here.





