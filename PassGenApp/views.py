from django.shortcuts import render
from django.views.generic import View
import random
import string
# Create your views here.


class PasswordView(View):
    def get(self, request, *args, **kwargs):

        a = list("abcdefghijklmnopqrstuvw")
        setpassword = ''
        
        
        if request.method=='GET':
           
            getlength = int(request.GET.get('length','0'))
            if request.GET.get('n'):
                a.extend('1234567890')
            if request.GET.get('s'):
                a.extend('!@#$%^&*()') 
            if request.GET.get('u'):
                a.extend('QWERTYUIOPASDFGHJKLZXCVBNM')

            setpassword = ''.join(random.choice(a) for i in range(getlength))
            

        context = {'pas': setpassword}
        return render(request, "Base.html", context=context)
