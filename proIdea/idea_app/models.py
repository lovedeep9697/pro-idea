from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here

User = get_user_model()

# model  for post
class post(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	text = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("idea_app:detail",kwargs={'pk':self.pk})
