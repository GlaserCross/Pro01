from django.urls import path 
from . import views
urlpatterns = [
	#path('signup/', views.register, name='signup'),
	path('register/', views.register, name='register')
]
