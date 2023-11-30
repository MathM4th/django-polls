from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from polls.views import QuestionCreateView

User = get_user_model() # obtém o model padrão para usuários do Django

from django.contrib import messages  # importa o form de registro

from accounts.forms import AccountSignupForm

from django.views.generic import TemplateView
from polls.models import Question


class AccountCreateView(CreateView):
    model = User # conecta o model a view
    template_name = 'registration/signup_form.html' # template para o form HTML
    form_class = AccountSignupForm # conecta o form a view
    success_url = reverse_lazy('login') # destino após a criação do novo usuário
    success_message = 'Usuário criado com sucesso!'


    def form_valid(self, form): # executa quando os dados estiverem válidos
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.success_message)
        return super(AccountCreateView, self).form_valid(form)

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/user_form.html'
    fields = ('first_name', 'email', 'imagem', )
    success_url = reverse_lazy('question-list')
    success_message = 'Perfil atualizado com sucesso!'

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        user = self.request.user
        if user is None or not user.is_authenticated or user_id != user.id:
            return User.objects.none()

        return User.objects.filter(id=user.id)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(AccountUpdateView, self).form_valid(form)

class AccountTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super(AccountTemplateView, self).get_context_data(**kwargs)
        voted = QuestionUser.objects.filter(user=self.request.user)
        context['questions_voted'] = voted
 
        return context