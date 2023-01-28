from django.contrib import admin
from .models import User, DataName, DataText, EmotionText
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'email']

class DataNameAdmin(admin.ModelAdmin):
    list_display = ['data_name']

class DataTextAdmin(admin.ModelAdmin):
    list_display = ['data_name', 'text', 'emotion_primary']

class EmotionTextAdmin(admin.ModelAdmin):
    list_display = ['emotion_name']


admin.site.register(User, UserAdmin)
admin.site.register(DataName, DataNameAdmin)
admin.site.register(DataText, DataTextAdmin)
admin.site.register(EmotionText, EmotionTextAdmin)
