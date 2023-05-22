from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django import forms
from .models import Product
# Create your views here.



class ProductForm(forms.Form):
    title = forms.CharField(label='title')
    describe = forms.CharField(label='Description', widget=forms.Textarea)
    image = forms.ImageField(label="image")



@login_required
def index(request):
    return render(request, "king/index.html", {
        "products": Product.objects.all()
    })





@login_required
def upload_image(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            describe = form.cleaned_data['describe']
            image = form.cleaned_data['image']
            user = request.user
            product = Product(title=title, describe=describe, image=image, user=user)
            product.save()
            return HttpResponseRedirect(reverse('king:index'))
        else:
            return render(request, "king/upload_product.html", {
                "form": form
            })

    return render(request, "king/upload_product.html", {
        "form": ProductForm()
    })



@login_required
def photos(request):
    
    photos = Product.objects.filter(user=request.user)
    return render(request, "king/my_photos.html", {
        "photos": photos
    })

@login_required
def photo_information(request, id_photo):
    return render(request, "king/photo_information.html", {
        "photo": Product.objects.get(pk=id_photo)
    })