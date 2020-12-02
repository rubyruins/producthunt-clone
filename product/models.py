import random
from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField()
	votes_total = models.IntegerField(default=1)
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')	
	body = models.TextField()
	# body = models.TextField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
	url = models.TextField()
	summary = models.CharField(max_length=200)
	tag = models.CharField(max_length=20)
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title

	'''def summary(self):
		return self.body[0:50]'''

	def pub_date_pretty(self):
		return self.pub_date.strftime('%B %d, %Y')