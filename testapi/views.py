import operator
from .models import StudentData, CalcData
from .serializers import StudentDataSerializer, CalcDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from enum import Enum


class OperationEnum(Enum):
    """An enumeration over acceptable operation types."""

    addition = operator.add
    add = operator.add
    sum = operator.add
    plus = operator.add
    minus = operator.sub
    subtract = operator.sub
    subtraction = operator.sub
    sub = operator.sub
    multiply = operator.mul
    mul = operator.mul
    times = operator.mul

@api_view(["POST"])
def calc(request, *args, **kwargs):
	data = request.data
	operations_type = data["operation_type"].Upper().strip()
	x = data["x"]
	y = data["y"]
	
	try:
		operations_type= OperationEnum[operations_type].value
	except Exception:
		return Response("invalid operation")
	else:
		value = operations_type(x, y)
		give = {
			"slackUsername":"shegzyrey",
			"operation_type":operations_type,
			"result":value
			}
		
		return Response(give, status=status.HTTP_200_OK)
        



# Create your views here.
@api_view(['GET', 'POST'])
def index(request):

	if request.method == 'GET':
		studentdata = StudentData.objects.get(id=1)
		serializer = StudentDataSerializer(studentdata)

		return JsonResponse(serializer.data)


