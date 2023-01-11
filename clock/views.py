from django.shortcuts import render

# Create your views here.
def clock_display(request):
    return render(request,'clock/display.html')
