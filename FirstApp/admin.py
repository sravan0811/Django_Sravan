from django.contrib import admin
from .models import Emp
from .models import UserFormMy
from .models import UserProfileInfo, User
# Register your models here.

admin.site.register(Emp)
admin.site.register(UserFormMy)
admin.site.register(UserProfileInfo)