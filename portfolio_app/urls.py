from django.urls import path
from portfolio_app import views

# For template tagging
app_name = 'portfolio_app'

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('/', views.index, name='index')
]
