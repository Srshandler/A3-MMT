from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from app.models import Cliente
from .forms import SignupForm

# Create your views here.
def home_page(request):
    return render(request, 'base/home.html')

def index_page(request):
    return render(request, 'index.html')

def form(request):
    return render(request, 'form.html')


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        cpf_cnpj = request.POST.get('cpf_cnpj')
        password = request.POST.get('password')

        try:
            user = Cliente.objects.get(cpf_cnpj=cpf_cnpj)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, cpf_cnpj=cpf_cnpj, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'cpf_cnpj or password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.cpf_cnpj = user.cpf_cnpj.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during account creation')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)
