from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat, Message


class IndexView(LoginRequiredMixin,View):
    def get(self,request):
        chats = Chat.objects.filter(participants=request.user)
        return render(request,'index.html',{'chats':chats})