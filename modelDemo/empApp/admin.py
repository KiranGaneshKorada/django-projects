from django.contrib import admin
from.models import Employee,Programmer,Project,Customer,PhoneNumber,Person,licenseNumber


# to view names instead of objects name in admin panel
class EmployeAdmin(admin.ModelAdmin):
    list_display=['firstName'] # list_display convention cannot be changed


class ProgrammerAdmin(admin.ModelAdmin):
    list_display=['name']

class ProjectAdmin(admin.ModelAdmin):
    list_display=['name']

# Register your models here.
admin.site.register(Employee,EmployeAdmin)

admin.site.register(Programmer,ProgrammerAdmin)

admin.site.register(Project,ProjectAdmin)

admin.site.register(PhoneNumber)

admin.site.register(Customer)

admin.site.register(Person)

admin.site.register(licenseNumber)


