from rest_framework import serializers
from . import models

class StudentDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.StudentData
		fields = ['slackUsername', 'backend', 'age', 'bio']
