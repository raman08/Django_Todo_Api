from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from Todo.models import Todo
from Todo.serializers import TodoSerializer

# Create your views here.

class TodoList(APIView):
	"""
		Get the Todo or Create one
	"""
	def get(self, request, format=None):
		todos = Todo.objects.all()
		serializer = TodoSerializer(todos, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = TodoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetails(APIView):
	"""
		GET a single todo
	"""
	def getTodo(self, id):
		try:
			return Todo.objects.get(id=id)
		except Todo.DoesNotExist:
			raise Http404

	def get(self, request, id, format=None):
		todo = self.getTodo(id)
		serializer = TodoSerializer(todo)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, id, format=None):
		todo = self.getTodo(id)
		serializer = TodoSerializer(todo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id, format=None):
		todo = self.getTodo(id)
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

