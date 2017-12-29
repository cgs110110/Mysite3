from django.contrib import admin
from .models import UserProfile,UserInfo

# Register your models here.
class UserprofielAdmin(admin.ModelAdmin):
    list_display = ('user','birth','phone')
    list_filter = ('user',)
admin.site.register(UserProfile,UserprofielAdmin)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','school','company','profession','address','aboutme','photo')
    list_filter = ('user','school','company')
admin.site.register(UserInfo,UserInfoAdmin)