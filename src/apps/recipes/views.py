from django.shortcuts import render

# Create your views here.



def recipes(request):
    context = {
         'title':'Recipes'
     }
    return render(request, 'recipes/recipes.html', context)