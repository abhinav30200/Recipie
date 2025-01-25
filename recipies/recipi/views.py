from django.shortcuts import render
from recipi.models import *

def home(request):
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
    return render(request,"index.html")


