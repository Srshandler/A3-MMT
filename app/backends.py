from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CPF_CNPJBackend(ModelBackend):
    def authenticate(self, request, cpf_cnpj=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(cpf_cnpj=cpf_cnpj)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
