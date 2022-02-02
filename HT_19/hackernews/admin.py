from django.contrib import admin
from .models import Ask
from .models import Show
from .models import New
from .models import Job
# Register your models here.


class DropDownAdmin(admin.ModelAdmin):
    list_display = ("id", "by")


admin.site.register(Ask)
admin.site.register(New)
admin.site.register(Show)
admin.site.register(Job)
