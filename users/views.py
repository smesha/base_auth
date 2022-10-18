from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout

from django.conf import settings
from . import forms
from .email_sending import send_mail_for_password_reset


class UrlRedirect:

	def get_success_url(self):
		return self.get_next_redirect_url() or self.get_default_redirect_url() 

	def get_next_redirect_url(self):
		return self.request.GET.get('next', None)

	def get_default_redirect_url(self):
		return settings.LOGIN_REDIRECT_URL

class Signin(View, UrlRedirect):
	template = settings.USERS["templates"]["signin"]
	form_class = forms.SigninForm

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			next_page = self.get_default_redirect_url()
			if next_page == request.path:
				raise ValueError(
					"Ваш LOGIN_REDIRECT_URL указывает на страницу входа. Хотя так не должно быть, потому что образуется цикличное перенаправление"
					)
			return redirect(next_page)

		return super().dispatch(request, *args, **kwargs)

	def get(self, request):
		form = self.form_class(request)
		return render(request,
			      self.template,
			      {"form": form})

	def post(self, request):
		form = self.form_class(request, request.POST)

		if form.is_valid():
			login(request,
				  form.get_user())

			next_page = self.get_success_url()
			return redirect(next_page)

		return render(request,
			      self.template,
			      {"form": form})

class Logout(View, UrlRedirect):
	logout_template = settings.USERS["templates"]["logout"]
	confirm_logout_template = settings.USERS["templates"]["confirm_logout"]
	

	def get_default_redirect_url(self):
		if settings.LOGOUT_REDIRECT_URL:
		        return reverse(settings.LOGOUT_REDIRECT_URL)
		else:
			return self.request.path

	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request):
		logout(request)
		next_page = self.get_success_url()

		if next_page != request.path:
			return redirect(next_page)

		return render(request, self.logout_template)

	def get(self, request):
		return render(request, self.confirm_logout_template)


class Signup(View, UrlRedirect):
        template = settings.USERS["templates"]["signin"]
        form_class = forms.SignupForm

        def dispatch(self, request, *args, **kwargs):
                return super().dispatch(request, *args, **kwargs)

        def get(self, request):
                form = self.form_class()
                return render(request, self.template, {"form": form})

        def post(self, request):
                form = self.form_class(request.POST)
                if form.is_valid():
	                form.save()
	                return redirect("users:signin")
                return render()


class PasswordReset(View, UrlRedirect):
        template = settings.USERS["templates"]["password_reset"]
        form_class = forms.PasswordResetForm
        
        def get(self, request):
                form = self.form_class()
                return render(request, self.template, {"form": form})

        def post(self, request):
                form = self.form_class(request.POST)

                if form.is_valid():
                        form.save(request=request, from_email=settings.DEFAULT_FROM_EMAIL)
                        return redirect("users:password_reset_done")
                

class PasswordResetDone(View):
        template = settings.USERS["templates"]["password_reset_done"]
        
        def get(self, request):
                return render(request, self.template)

class Reset(View):
        pass

class ResetDone(View):
        pass
