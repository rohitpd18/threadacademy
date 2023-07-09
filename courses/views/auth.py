from django.shortcuts import render , redirect
from django.contrib.auth import logout , login
from courses.forms import RegistrationForm , LoginForm
from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class SignupView(FormView):
    template_name="courses/signup.html" 
    form_class = RegistrationForm
    success_url  = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'courses/login.html', {'form': form})

def signout(request ):
    logout(request)
    return redirect("home")

