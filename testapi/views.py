from .models import StudentData
from .serializers import StudentDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

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
	subtract_arr = ['minus', 'subtact','subtraction', 'difference']
	mult_arr = ['multiply', 'multiplication', 'times', 'multiplied']
	
	x = int(request.data["x"])
	y = int(request.data["y"])
	op = str(request.data["operation_type"])
	operation = op.split(" ")

	for i in operation:
		if i.lower() in add_arr:
			result = x+y
			op = "Addition"
			break
		elif i.lower() in subtract_arr:
			result = x-y
			operations_type = "Subtraction"
			break
		elif i.lower() in mult_arr:
			result = x*y
			op = "Multiplication"
			break
		else:
			op = "Invalid Operator"
			
	give = {
		"slackUsername":"shegzyrey",
		"x":x,
		"y":y,
		"operation_type":op,
		"result":result,
		}
		
	return Response(give, status=status.HTTP_200_OK, headers=header)
        







	