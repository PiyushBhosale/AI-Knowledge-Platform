from django.contrib import admin
from .models import Query, QueryAdmin, Response
# Register your models here.
admin.site.register(Query, QueryAdmin)
admin.site.register(Response)
