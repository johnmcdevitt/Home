from django.urls import path
from . import views

# app url patterns
urlpatterns = [
    path('',views.ToDoLandingView,name='todos'),
    path('create/',views.ToDoCreateView.as_view(),name='todo-create'),
    path('<int:pk>/',views.ToDoDetailView.as_view(),name='todo-detail'),
    path('<int:pk>/edit',views.ToDoUpdateView.as_view(),name='todo-update'),

]
