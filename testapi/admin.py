from django.contrib import admin
from .models import StudentData
#from .models import CalcData


#Register your models here
class StudentDataAdmin(admin.ModelAdmin):
	list_display = ('id', 'slackUsername')
	ordering = ('slackUsername',)
	search_fields = ('slackUsername',)
admin.site.register(StudentData, StudentDataAdmin)

'''
class CalcDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'operation_type')
admin.site.register(CalcData, CalcDataAdmin )
'''