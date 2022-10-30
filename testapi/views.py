from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentData
from .serializers import StudentDataSerializer
# Create your views here.
def index(request):
	studentdata = StudentData.objects.get(id=1)
	serializer = StudentDataSerializer(studentdata)

	return JsonResponse(serializer.data, safe=False)

