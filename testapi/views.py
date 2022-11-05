from .models import StudentData
from .serializers import StudentDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

@api_view(['POST'])
def calc(request):
	header = {"Access-Control-Allow-Origin":"*"}
	result = 0
	add_arr = ['add', 'addition', 'added', 'sum', 'sumup', 'summation of']
	subtract_arr = ['minus', 'subtact','subtraction', 'difference']
	mult_arr = ['multiply', 'multiplication', 'times', 'multiplied']
	
	x = int(request.data["x"])
	y = int(request.data["y"])
	operations_type = str(request.data["operation_type"])
	operation = operations_type.split(" ")

	for i in operation:
		if i.lower() in add_arr:
			result = x+y
			operations_type = "Addition"
			break
		elif i.lower() in subtract_arr:
			result = x-y
			operations_type = "Subtraction"
			break
		elif i.lower() in mult_arr:
			result = x*y
			operations_type = "Multiplication"
			break
		else:
			operations_type = "Invalid Operator"
			
	give = {
		"slackUsername":"shegzyrey",
		"x":x,
		"y":y,
		"operation_type":operations_type,
		"result":result,
		}
		
	return Response(give, status=status.HTTP_201_CREATED, headers=header)
        


'''
@api_view(['POST'])
def arithOp(request):
    data = request.data
    op_type = data['operation_type'].lower()
    x = int(data['x'])
    y = int(data['y'])
    if op_type in ['addition', 'add', 'plus', '+']:
        result = x + y
    elif op_type in ['subtraction', 'subtract', 'deduct', 'minus', '-']:
        result = x - y
    elif op_type in ['multiplication', 'multiply', 'times', '*']:
        result = x * y
    else:
        result = 'invalid operation type'
    return_data = [
        {
            "slackUsername": "Peter Oyelegbin",
            "result": result,
            "operation_type": op_type
        }   
    ]
    return Response(return_data, status=status.HTTP_202_ACCEPTED)
'''

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):

	if request.method == 'GET':
		studentdata = StudentData.objects.get(id=1)
		serializer = StudentDataSerializer(studentdata)

		return JsonResponse(serializer.data)



'''
@api_view(['POST'])
def calc(request):
	serializer = CalcSerializer(data=request.data)
	if serializer.is_valid():
		op_type= serializer.validated_data['operation_type']
		x = serializer.validated_data['x']
		y = serializer.validated_data['y']
		if op_type in ['addition', 'add', 'plus', '+']:
			result = x + y
		elif op_type in ['subtraction', 'subtract', 'deduct', 'minus', '-']:
			result = x - y
		elif op_type in ['multiplication', 'multiply', 'times', '*']:
			result = x * y
		else:
			result = 'invalid operation type'
			return_data = [
				{
					"slackUsername": "shegzyrey",
					"operation_type": op_type,
					'result': result,
					}
				]
				
		return JsonResponse(return_data)
	
'''

'''
@api_view(['POST'])
def calc(request):
	data = request.data
	operation_type = str(data['operation_type'])
	x = data['x']
	y = data['y']

	if operation_type.strip().lower() in ['addition', 'sum', 'add', 'summation', 'adding','plus', 'total', 'added', 'summed']:
		if x and y:
			result = x + y
		else:
			num = re.findall(r'\d+', operation_type.strip().lower())
			try:
				x = int(num[0])
				y = int(num[1])
				operation_type = 'addition'
				result = x + y
			except IndexError:
				error_response = 'numbers are not integers'
	elif operation_type.strip().lower() in ['subtraction', 'minus', 'subtracted', 'subracting', 'remove','sub', 'deduct', 'subtract']:
		if x and y:
			result = x - y
		else:
			num = re.findall('[0-9,-]+', operation_type.strip().lower())
			try:
				x = int(num[0])
				y = int(num[1])
				operation_type = 'subtraction'
				result = x - y
			except IndexError:
				error_response = 'numbers are not integers'
	elif operation_type.strip().lower() in ['multiply', 'multiplying', 'multiplied', 'multiplication', 'product']:
		if x and y:
			result = x * y
		else:
			num = re.findall('[0-9,-]+', operation_type.strip().lower())
			try:
				x = int(num[0])
				y = int(num[1])
				operation_type = 'addition'
				result = x * y
			except IndexError:
				error_response = 'numbers are not integers'

	if error_response:
		Result = {"slackUsername":"shegzyrey", "error_response": 'ERROR' + error_response}
	else:
		Result = {"slackUsername": "shegzyrey", "result":result, "operation_type": operation_type }
	return Response(Result, status=status.HTTP_200_OK)
'''






'''
@api_view(['GET', 'POST'])
def calc(request):

	if request.method == 'GET':
		calcdata = CalcData.objects.all()
		serializer = CalcDataSerializer(calcdata, many=True)

		return JsonResponse(serializer.data, safe=False)

	if request.method == 'POST':
		serializer = CalcDataSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return(serializer)
'''
'''
	if request.method == 'POST':
		json = request.POST
		result = 0
		x = request.POST['x']
		y = request.POST['y']
		operation_type = request.POST['operation_type']
		if operation_type == 'addition':
			result = int(x) + int(y)
			operation_type = 'addition'
		elif operation_type == 'subtraction':
			result = int(x) - int(y)
			operation_type = 'subtraction'
		elif operation_type == 'multiplication':
			result = int(x) * int(y)
			operation_type = 'multiplication'
		data = {
            'slackUsername':'shegzyrey',
            'operation_type' : operation_type,
            'result' : result
        }
		return Response(data, status=status.HTTP_201_CREATED)
		'''

'''
	if request.method == 'POST':
		serializer = CalcDataSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)
'''

'''   
def post(self):
    json = request.POST
    result = 0
    x = request.POST['x']
    y = request.POST['y']
    operation_type = request.POST['operation_type']
    if operation_type == 'addition':
        result = int(x) + int(y)
        operation_type = 'addition'
    elif operation_type == 'subtraction':
        result = int(x) - int(y)
        operation_type = 'subtraction'
    elif operation_type == 'multiplication':
        result = int(x) * int(y)
        operation_type = 'multiplication'
    data = {
        'slackUsername':'shegzyrey',
        'operation_type' : operation_type,
        'result' : result
    }
    return Response(data, status=status.HTTP_201_CREATED)
'''

	