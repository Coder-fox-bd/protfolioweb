from django.urls import path
from .views import (
	HomeView,
	ClassesView,
	TutorialView,
	ServiceView,
	ContactView
	)
app_name = 'protfolioweb'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('classes', ClassesView.as_view(), name='classes'),
    path('playlist/<int:pk>', TutorialView.as_view(), name='tutorial_list'),
	path('services', ServiceView.as_view(), name='services'),
    path('contact', ContactView.as_view(), name='contact'),
]