from django.shortcuts import render
from django.template import Template, Context, loader
from flia.models import Familiar

def listar_familiares(request):
    listar_familiares = Familiar.objects.all()
    print(listar_familiares)

    return render(request,"familiares_list.html",{"familiar":listar_familiares})
    


