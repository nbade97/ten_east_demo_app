from django.urls import path
from .views import login_view
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
	path('login/', login_view, name='login'),
	path('admin/', admin.site.urls),
	path('frontend/', include('frontend.urls')),  # Include the URLs from your frontend app
	path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Serve the Vue.js frontend
]