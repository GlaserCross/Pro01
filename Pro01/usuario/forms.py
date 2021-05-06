from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
	username = forms.CharField(label='Nombre de usuario', min_length=4, max_length=150)
	first_name = forms.CharField(label = 'Nombres', max_length=150)
	last_name = forms.CharField(label = 'Apellidos', max_length=150)
	email = forms.EmailField(label='Ingrese email')
	password1 = forms.CharField(label='Ingrese contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Ingrese contraseña nuevamente', widget=forms.PasswordInput)
	#choices = [('Vendedor','Vendedor'),
			#('Repartidor','Repartidor'),
			#('Comprador','Comprador')]
	#tipo = forms.ChoiceField (label ='Tipo de cuenta', choices=choices)
	is_repartidor = False
	is_vendedor = True
	is_comprador = False
	#is_vendedor = forms.BooleanField (label='Cuenta de Vendedor', required=False)
	#is_repartidor = forms.BooleanField (label =' Cuenta de Repartidor?', required=False)
	#is_comprador = forms.BooleanField (label ='Cuenta de Comprador', required=False)

	def clean_tipo(self):
		is_vendedor = self.cleaned_data.get('is_vendedor')
		is_comprador = self.cleaned_data.get('is_comprador')
		is_repartidor = self.cleaned_data.get('is_repartidor')

		suma = [is_vendedor, is_comprador, is_repartidor]
		result = 0
		for num in suma:
			result+= num
		if result>1 or result == 0:
			raise ValidationError("Solo puede seleccionar un tipo de usuario!")
			return is_vendedor 
	#def clean_username(self):
		#username = self.cleaned_data['username']
		#r = User.objects.filter(username=username)
		#if r.count():
			#raise  ValidationError("Usuario ya existe!")
			#return username
	#choices = [('Vendedor'),
			#('Repartidor'),
			#('Comprador')]

	#def porFavorFunciona(self):
	#tipo = self.cleaned_data['cuenta']
	#if tipo== 'Vendedor':
		#is_vendedor=True
	#elif tipo == 'Repartidor':
		#is_repartidor = True
	#elif tipo == 'Comprador':
		#is_repartidor = True
	#return is_repartidor, is_vendedor, is_comprador

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		if r.count():
			raise  ValidationError("Correo ya en uso!")
			return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise ValidationError("Las contraseñas no coinciden")
			
			return password1
	#def clean_tipo(self):
		#cleaned_data = super().clean()
		#if cleaned_data['is_vendedor']


		#is_vendedor = self.is_vendedor
		#is_repartidor = self.is_repartidor
		#is_comprador = self.is_comprador
		#if cleaned_data['is_vendedor'] and cleaned_data['is_comprador'] and cleaned_data['is_repartidor'] or cleaned_data['is_vendedor'] and cleaned_data['is_comprador'] or cleaned_data['is_vendedor'] and cleaned_data['is_repartidor'] or cleaned_data['is_repartidor'] and cleaned_data['is_vendedor']:
			#return ValidationError("Solo puede seleccionar un tipo de usuario")
			#return is_vendedor
		#suma = [is_vendedor, is_comprador, is_repartidor]
		#result = 0
		#for num in suma:
			#result+= num
		#if result>1:
			#return ValidationError("Solo puede seleccionar un tipo de usuario!")
			#return is_vendedor

		#if result== 0 or (is_comprador == False and is_vendedor == False and is_repartidor == False):
			#return ValidationError("Debe seleccionar al menos un tipo de usuario!")
			#return is_vendedor
	class Meta(UserCreationForm):
		model = User
		fields = ["username", "first_name", "last_name", "email","password1","password2","is_vendedor","is_repartidor","is_comprador"]
