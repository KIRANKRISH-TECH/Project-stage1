# from django.shortcuts import render, redirect
# from .forms import studentForm, contactForm,contacteForm

# # def member(request):
# #     return HttpResponse("Hello world")

# def home(request):
#     return render(request, 'file1.html')

# def student_view(request):
#     if request.method == "POST":
#         form = studentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_view')
#     else:
#         form = studentForm()
#     return render(request, 'student.html', {'form': form})

    

# def contact_view(request):  

#     if request.method == "POST":
#         form =contactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_view')
#     else:
#         form = contactForm()
#     return render(request, 'contact.html', {'form': form})


# def contacte_view(request):
#     if request.method == "POST":
#         form =contacteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contacte_view')
#     else:
#         form = contacteForm()
#     return render(request, 'contacte.html', {'form': form})





  
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if not username or not email or not password:
            messages.error(request, 'All fields are required.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Full name already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')

    return render(request, 'login.html')





# Create your views here.





