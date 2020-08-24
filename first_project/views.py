# I have created this Shivam
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    txt=request.POST.get('text','default')
    txt1=request.POST.get('removepunc','off')
    if(txt1=='on'):
        analyzed=txt
        punctuation = '''!(),,,,'!!!!'''
        analyzer=""
        for char in analyzed:
            if char not in punctuation:
                analyzer=analyzer + char
        par={'name':'shivam','place':'hyderabad','corrected':analyzer};
        return render(request,'analyze.html',par)
    else:
        return HttpResponse('Error')
