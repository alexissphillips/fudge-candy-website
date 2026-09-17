from django.shortcuts import render

# Create your views here.

def candylist(request):
    return render(request, 'fudgekettle/candylist.html', {})

