from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from myapp.models import Product, Category


def index(request):
    try:
        product=Product.objects.all()
        context={"title":"Product List","products":product}
    except Exception as ex:
        return HttpResponse(f"Error{ex}")
    return render(request,"pages/Products/productList.html",context)
def create(request):
    category=Category.objects.all()
    context={"title":"Product Form","categorys":category}
    return render(request,"pages/Products/productForm.html",context)
def store(request):
    try:
        if request.method=="POST":
            product=Product()
            product.productName=request.POST["txtName"]
            product.barcode = request.POST["txtBarcode"]
            product.unitPrice = request.POST["txtUnitPrice"]
            product.sellPrice = request.POST["txtSellPrice"]
            product.qty = request.POST["txtQty"]
            product.category_id = request.POST["dllCategoryId"]
            if len(request.FILES)>0:
                product.photo = request.FILES["photo"]
                product.save()
                messages.success(request, "Product save succesfully")
            else:
                product.photo=""
                product.save()
                messages.success(request,"Product save succesfully")
    except Exception as ex:
        return HttpResponse(f"Error{ex}")
    return redirect("/api/product/create")
def destroy(request,id):
    try:
        product=Product.objects.get(pk=id)
        if product.photo:
            product.photo.delete()
            product.delete()
        else:
            product.delete()
    except Exception as ex:
        return HttpResponse(f"Error{ex}")
    return redirect("/api/product/index")
def edit(request,id):
    try:
        product=Product.objects.get(id=id)
        category=Category.objects.all()
        context={"title":"Product Edit Form","products":product,"categorys":category}
    except Exception as ex:
        return HttpResponse(f"Error{ex}")
    return render(request,"pages/Products/productEditForm.html",context)
def update(request,id):
    try:
        if request.method == "POST":
            p=Product.objects.get(id=id)
            product = Product()
            product.id=id
            product.productName = request.POST["txtName"]
            product.barcode = request.POST["txtBarcode"]
            product.unitPrice = request.POST["txtUnitPrice"]
            product.sellPrice = request.POST["txtSellPrice"]
            product.qty = request.POST["txtQty"]
            product.category_id = request.POST["dllCategoryId"]
            if p.photo:
                if len(request.FILES) > 0:
                    product.photo = request.FILES["photo"]
                    p.photo.delete()
                    product.save()
                    messages.success(request, "Product update succesfully")
                else:
                    product.photo =p.photo
                    product.save()
                    messages.success(request, "Product update succesfully")
            else:
                if len(request.FILES) > 0:
                    product.photo = request.FILES["photo"]

                    product.save()
                    messages.success(request, "Product update succesfully")
                else:
                    product.photo =""
                    product.save()
                    messages.success(request, "Product update succesfully")
    except Exception as ex:
        return HttpResponse(f"Error{ex}")
    return redirect("/api/product/edit/"+id)