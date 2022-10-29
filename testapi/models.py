from __future__ import unicode_literals
from django.db import models

# Create your models here.
class StudentData(models.Model):
	slackUsername = models.CharField(max_length=15)
	backend = models.BooleanField()
	age = models.IntegerField()
	bio = models.TextField(blank=True)

	def __self__(self):
		return self.slackUsername
