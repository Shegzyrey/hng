from django.contrib import admin
from .models import StudentData

#Register your models here
class StudentDataAdmin(admin.ModelAdmin):
	list_display = ('id', 'slackUsername')
	ordering = ('slackUsername',)
	search_fields = ('slackUsername',)
admin.site.register(StudentData, StudentDataAdmin)
