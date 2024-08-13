from django.urls import path
from .views import login_view, index

urlpatterns = [
	path('api/login/', login_view, name='login'),
    path('', index, name='index'),  # Catch-all pattern to serve the Vue.js app
]