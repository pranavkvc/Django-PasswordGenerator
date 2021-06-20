from django.shortcuts import render,get_object_or_404
from django.views.generic import View
import random
import time
from .models import User
# Create your views here.


class PasswordView(View):
    def get(self, request, *args, **kwargs):

        a = list("abcdefghijklmnopqrstuvw")
        setpassword = ''
        
        self.loader = False
        if request.method=='GET':
            
            getlength = int(request.GET.get('length','0'))
            if request.GET.get('n'):
                a.extend('1234567890')
            if request.GET.get('s'):
                a.extend('!@#$%^&*()') 
            if request.GET.get('u'):
                a.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
            
            
                
            time.sleep(3)
            self.loader = True
            setpassword = ''.join(random.choice(a) for i in range(getlength))

           
            

        context = {'pas': setpassword,'load':self.loader}
        return render(request, "Base.html", context=context)
