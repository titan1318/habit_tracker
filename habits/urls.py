from django.urls import path
from .views import HabitListView, HabitDetailView, PublicHabitListView

urlpatterns = [
    path('', HabitListView.as_view(), name='habit_list'),
    path('<int:pk>/', HabitDetailView.as_view(), name='habit_detail'),
    path('public/', PublicHabitListView.as_view(), name='public_habit_list'),
]
