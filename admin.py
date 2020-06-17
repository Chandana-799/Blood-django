from django.contrib import admin
#from tinymce.widgets import TinyMCE
from .models import Contact,Donor,Needblood
from django.db import models

class Contact1(admin.ModelAdmin):
    fieldsets = [
        ("Title/id/no",{"fields":["name","email","contactnumber"]}),
        ("message",{"fields":["message"]})
]


admin.site.register(Contact,Contact1)
admin.site.register(Donor)
admin.site.register(Needblood)
