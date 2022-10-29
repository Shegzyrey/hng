from django.contrib import admin
from .models import StudentData

#Register your models here
class StudentDataAdmin(admin.ModelAdmin):
	list_display = ('id', 'slackusername')
	ordering = ('slackusername',)
	search_fields = ('slackusername',)
admin.site.register(StudentData, StudentDataAdmin)
