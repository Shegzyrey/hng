from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import StudentData
from .serializers import StudentDataSerializer
# Create your views here.
def index(request):
	return HttpResponse("<h1>The Meandco Homepage</h1>")

def studentdata_list(request):
	studentdata = StudentData.objects.all()
	serializer = StudentDataSerializer(studentdata, many=True)

	return JsonResponse(serializer.data, safe=False)
