from django.contrib import admin
from .models import Contact,Student,Attendance
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','usn','name','email', 'attendance')
    search_fields = ('usn', 'email',)
    list_per_page = 20

admin.site.register(Contact)
admin.site.register(Student, StudentAdmin)
admin.site.register(Attendance)