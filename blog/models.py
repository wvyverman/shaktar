from django.db import models
from django.utils import timezone

class Post(models.Model):
	auteur = models.ForeignKey('auth.User')
	titel = models.CharField(max_length = 200)
	bericht = models.TextField()
	gecreëerd_op = models.DateTimeField(
		default = timezone.now)
	gepubliceerd_op = models.DateTimeField(
		blank = True, null = True)

	def publish(self):
		self.gepubliceerd_op = timezone.now()
		self.save()

	def __str__(self):
		return self.titel
# Create your models here.
