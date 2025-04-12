from django.contrib import admin

from core.models import *

admin.site.register([News,Book,Phone,Car,Product])
