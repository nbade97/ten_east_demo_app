from django.urls import path
from .views import login_view, add_contribution

urlpatterns = [
	path('login/', login_view, name='login'),
	path('add_contribution/', add_contribution, name='add_contribution'),
]