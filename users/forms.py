from django.contrib.auth import forms as auth_forms
from django.contrib.auth.tokens import default_token_generator


class SigninForm(auth_forms.AuthenticationForm):
	pass


class SignupForm(auth_forms.UserCreationForm):
	pass

class PasswordResetForm(auth_forms.PasswordResetForm):
        def save(
                self,
                domain_override=None,
                subject_template_name="auth/password_reset_subject.txt",
                email_template_name="auth/password_reset_email.html",
                use_https=False,
                token_generator=default_token_generator,
                from_email=None,
                request=None,
                html_email_template_name=None,
                extra_email_context=None,
        ):
                super().save(
                        domain_override=domain_override,
                        subject_template_name=subject_template_name,
                        email_template_name=email_template_name,
                        use_https=use_https,
                        token_generator=token_generator,
                        from_email=from_email,
                        request=request,
                        html_email_template_name=html_email_template_name,
                        extra_email_context=extra_email_context
                )
