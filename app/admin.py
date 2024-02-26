from django.contrib import admin
from app.models import Group,Chat
# Register your models here.
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display=['id','content','timestamp','group_name']
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display=['id','group']