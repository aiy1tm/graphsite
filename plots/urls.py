#urls.py for plots

from django.urls import path
from . import views

app_name = 'plots'

urlpatterns = [
	path('',views.index),
	path('mortgage',views.index),
	path('retirement', views.retirement),
	path('allocation',views.allocation)
]