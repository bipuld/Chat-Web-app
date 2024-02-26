from django.shortcuts import render
from app.models import Chat,Group
# Create your views here.
def home(request, groupname):
    group=Group.objects.filter(group=groupname).first()
    chats=[]
    print(group)
    if group:
        chats=Chat.objects.filter(group_name=group)
    else:
        group=Group(group=groupname)
        group.save()
    context = {
        'group': groupname,
        'chats': chats
    }
    return render(request, 'app/home.html', context)
