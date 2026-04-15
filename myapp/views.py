from django.shortcuts import render

# Create your views here.
# hello
def func(request):
    
    return render(request,'index.html')
