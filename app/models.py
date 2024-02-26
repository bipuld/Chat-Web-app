from django.db import models

# Create your models here.
class Group(models.Model):
    group=models.CharField(max_length=255)
    
    def __str__(self):
        return self.group
    
class Chat(models.Model):
    group_name=models.ForeignKey(Group,on_delete=models.CASCADE)
    content=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f"{self.id} + {self.group_name} "