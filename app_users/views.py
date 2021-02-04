from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse


class LoginPage(LoginView):
    template_name = 'app_users/login.html'

    def get_success_url(self):
        return reverse('news')


class LogoutPage(LogoutView):
    template_name = 'app_users/logout.html'

    def get_next_page(self):
        return reverse('news')
