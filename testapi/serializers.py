from rest_framework import serializers
from . import models
from rest_enumfield import EnumField
from enum import Enum



class StudentDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.StudentData
		fields = ('slackUsername', 'backend', 'age', 'bio')
'''
class CalcDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.CalcData
		fields = ("operation_type", "x", "y")
'''
'''
class Operations(Enum):
    SUBTRACTION=0
    ADDITION=1
    MULTIPLICATION=2

class CalcSerializer(serializers.Serializer):
    operation_type=serializers.CharField(max_length=76)
    x=serializers.IntegerField()
    y=serializers.IntegerField()
	'''