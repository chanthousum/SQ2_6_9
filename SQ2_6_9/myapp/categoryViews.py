from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from myapp.models import Category


def index(request):
    try:
        category=Category.objects.all()
        context={"title":"Category List","categorys":category}
    except Exception as ex:
        return HttpResponse(f"Error{ex}")
    return render(request,"pages/Categorys/categoryList.html",context)
def create(request):
    context={"title":"Category Form"}
    return render(request,"pages/Categorys/categoryForm.html",context)
def store(request):
    try:
        if request.method=="POST":
            category=Category()
            category.categoryName=request.POST["txtName"]
            category.save()
            messages.success(request,"category save succesfully")
    except Exception as ex:
        return HttpResponse(f"Error{ex}")
    return redirect("/api/category/create")
def destroy(request,id):
    try:
        category=Category.objects.get(pk=id)
        category.delete()
    except Exception as ex:
        return HttpResponse(f"Error{ex}")
    return redirect("/api/category/index")
def edit(request,id):
    try:
        category=Category.objects.get(id=id)
        context={"title":"Category Edit Form","categorys":category}
    except Exception as ex:
        return HttpResponse(f"Error{ex}")
    return render(request,"pages/Categorys/categoryEditForm.html",context)
def update(request,id):
    try:
        if request.method=="POST":
            category=Category.objects.get(id=id)
            category.categoryName=request.POST["txtName"]
            category.save()
            messages.success(request,"category update succesfully")
    except Exception as ex:
        return HttpResponse(f"Error{ex}")
    return redirect("/api/category/edit/"+id)