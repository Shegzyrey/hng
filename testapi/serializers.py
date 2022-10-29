from rest_framework import serializers
from . import models

class StudentDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.StudentData
		fields = ['slackusername', 'backend', 'age', 'bio']
