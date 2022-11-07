from .models import StudentData
from .serializers import StudentDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import operator

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):

	if request.method == 'GET':
		studentdata = StudentData.objects.get(id=1)
		serializer = StudentDataSerializer(studentdata)

		return JsonResponse(serializer.data)

@api_view(['POST'])
def calc(request):
	header = {"Access-Control-Allow-Origin":"*"}
	result = 0
	add_arr = ['add', 'addition', 'added', 'sum', 'sumup', 'summation of']
	sub_arr = ['minus', 'subtract','subtraction', 'difference']
	mult_arr = ['multiply', 'multiplication', 'times', 'multiplied']
	
	x = int(request.data["x"])
	y = int(request.data["y"])
	operations_type = str(request.data["operation_type"]).lower().split(" ")

	for i in operations_type:
		if i in add_arr:
			result = operator.add(x, y)
			operations_type = add_arr[1]
			break
		elif i in sub_arr:
			result = x-y
			operations_type = sub_arr[2]
			break
		elif i in mult_arr:
			result = x*y
			operations_type = mult_arr[1]
			break
		else:
			operations_type = "Invalid Operator"
			
	give = {
		"slackUsername":"shegzyrey",
		"operation_type":operations_type,
		"result":result,
		}
		
	return Response(give, status=status.HTTP_200_OK, headers=header)
        







	