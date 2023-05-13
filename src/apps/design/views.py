from django.shortcuts import render



def features(request):
    context = {
         'title':'Ux Ui Design'
     }
    return render(request, 'design/features.html', context)
