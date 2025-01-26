from django.shortcuts import render
from recipi.models import *
from django.shortcuts import  redirect

def home(request):
    querryset = form.objects.all()
    context = {'recipies': querryset}
    if request.method=="POST":
        data = request.POST
        name = data.get('name')
        description=data.get('description')
        image=request.FILES['image']

        form.objects.create(
            name=name,
            description=description,
            image=image,
        )
        querryset=form.objects.all()

        context['recipies'] = querryset
    return render(request,"index.html",context)

def delete_recipie(request, id):
    try:
        recipe = form.objects.get(id=id)
        recipe.delete()
    except form.DoesNotExist:
        pass  # You might want to handle this case with an error message or logging
    return redirect('home')



