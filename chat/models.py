from django.db import models
from users.models import User

class Chat(models.Model):
    name = models.CharField(max_length=50,default="",null=True,blank=True)
    about = models.CharField(max_length=50,default="",null=True,blank=True)
    participants = models.ManyToManyField(User)
    is_group = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE, related_name="messages")
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)