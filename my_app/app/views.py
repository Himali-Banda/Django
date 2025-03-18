from django.shortcuts import render, HttpResponse

# Create your views here.
 from django.urls import reverse_lazy
 from django.views.generic.edit import CreateView
 from app.form import CustomUserCreationForm


 def demoFunction(request):
    demo={'name':'Himali'}
    return render(request,'index.html',demo)

class SignUp(CreateView):
      form_class = CustomUserCreationForm
      success_url = reverse_lazy('login')
      template_name = 'register.html'

      def demFunction(request):
     return render(request,"home/index.html")

class Login(CreateView):
      form_class = CustomUserCreationForm
      template_name = 'index.html'


