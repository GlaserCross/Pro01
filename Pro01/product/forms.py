from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import product

class RegistroProduct(forms.ModelForm):
	id= forms.CharField(widget=forms.HiddenInput())
	nombre = forms.CharField(max_length=200)
	TIPO_PRODUC = (
        ('F', 'Fruta'),
        ('V','Verdura'),
        ('H','Hortaliza')
        )

	tipo = forms.ChoiceField(choices='TIPO_PRODUC')
	precio = forms.IntegerField()
	image = forms.ImageField()

	def get_initial(self):
		initial = super().get_initial()
		initial['User'] = self.kwargs['Username']
		return User
	class Meta:
		model = product
		fields = ["id","nombre","User", "tipo", "precio", "image"]