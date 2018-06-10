from django.contrib import admin
from .models import Report, Client, Title_report, Type_pentest, Affected_elements, Evidences_images

admin.site.register(Report)
admin.site.register(Client)
admin.site.register(Title_report)
admin.site.register(Type_pentest)
admin.site.register(Affected_elements)
admin.site.register(Evidences_images)
