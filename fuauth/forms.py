from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm, UserChangeForm as AuthUserChangeForm
from django import forms

from fuauth.models import User

class UserCreationForm(AuthUserCreationForm):

	#TODO - Determine if newsletter line is needed
	receive_newsletter = forms.BooleanField(required=False)

	class Meta:
		model = User
		fields = ['name', 'email', 'phone_number', 'carrier', 'user_timezone', 
		'is_staff', 'is_active', 'receive_newsletter']

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.default_manager.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(
			self.error_messages['duplicate_username'],
			code='duplicate_username',
		)

class UserChangeForm(AuthUserChangeForm):

	#TODO - Determine if newsletter line is needed
	receive_newsletter = forms.BooleanField(required=False)

	class Meta:
		model = User
		fields = ['name', 'email', 'phone_number', 'carrier', 'user_timezone', 
		'is_staff', 'is_active', 'receive_newsletter']