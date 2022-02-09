from store.models import Category


# adding below function view to setting to make it avaiable in whole project
def categories(request):
    return {
        'categories': Category.objects.all()
    }
