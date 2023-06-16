from django.shortcuts import render
from backend.apps.manuldb.models import Category, PeopleImage


def category_context_get(request):
    categories = Category.objects.all()
    return {'categories': categories}


def people_image_get(request):
    people_images = PeopleImage.objects.all()
    return {'people_images': people_images}
