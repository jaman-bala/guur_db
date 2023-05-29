from backend.apps.manuldb.models import Category


def category_context_get(request):
    categories = Category.objects.all()
    return {'categories': categories}



