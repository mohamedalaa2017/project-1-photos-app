from . import views
from django.urls import path 

app_name = "king"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id_photo>", views.photo_information, name="photo_information"),
    path("upload", views.upload_image, name="upload"),
    path("my-photos", views.photos, name="photos")
]