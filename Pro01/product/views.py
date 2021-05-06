from django.shortcuts import render
from . models import product
from django import forms
from django.forms import ModelForm
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def productos(request):
	num_product = product.objects.all()
	return render(request,
		'productos.html',
		context={"num_product":num_product},
		)
class ProductCreate(CreateView):
	model = product
	fields =['id','nombre','tipo','precio','image']
	def get_form(self, form_class=None):
		form = super().get_form( form_class)
		form.fields['id'].widget = forms.HiddenInput()
		return form
	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(ProductCreate, self).form_valid(form)

class ProductUpdate(UpdateView):
	model = product
	fields = ['nombre','tipo','precio','image']

class ProductDelete(DeleteView):
	model = product
	success_url = reverse_lazy('blog')

from django.views import generic

class ProductDetailView(generic.DetailView):
	model = product