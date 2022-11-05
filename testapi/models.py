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

class CalcData(models.Model):
    operation_type = models.CharField(max_length=14)
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return f"{self.x} {self.operation_type} {self.y}"

