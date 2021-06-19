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
           
            getlength = int(request.GET.get('length'))
            setpassword = ''.join(random.choice(a) for i in range(getlength))
            

        context = {'pas': setpassword}
        return render(request, "Base.html", context=context)
