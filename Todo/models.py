from django.db import models

# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=20)
	text = models.TextField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
			ordering = ['created']

	def __str__(self):
		return self.title
