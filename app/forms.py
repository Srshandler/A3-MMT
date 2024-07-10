from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Cliente, Telefone

class SignupForm(UserCreationForm):
    nome = forms.CharField(max_length=255, required=True)
    cpf_cnpj = forms.CharField(max_length=14, required=True)
    tipo_cliente = forms.ChoiceField(choices=Cliente.TipoCliente.choices, required=True)
    email = forms.EmailField(required=True)
    numero_telefone = forms.CharField(max_length=20, required=True)

    class Meta(UserCreationForm.Meta):
        model = Cliente
        fields = ('nome', 'cpf_cnpj', 'tipo_cliente', 'email', 'password1', 'password2')