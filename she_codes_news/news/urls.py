from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('<int:pk>/edit-story', views.UpdateStoryView.as_view(), name='editstory'),
    path('<int:pk>/delete-story', views.DeleteStoryView.as_view(), name='deletestory'),
]
