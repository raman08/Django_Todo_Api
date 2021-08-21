from django.urls import path, include
from Todo import views


urlpatterns = [
	path('todo', views.TodoList.as_view()),
	path('todo/<int:id>', views.TodoDetails.as_view())
]