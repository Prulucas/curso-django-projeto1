from django.http.response import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from recipes.models import Recipe

# from utils.recipes.factory import make_recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True,).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    # return HTTP Response #


def category(request, category_id):

    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_published=True,).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |',
    })


def recipe(request, id):

    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })


"""
# enganar o django para duplicar receitas:
# - from recipes.models import Recipe
# - r = Recipe.objects.get(id=2)
# - r
# <Recipe: Outra Receita com HTML>
# - for i in range(20): r.id = None; r.save()
# ... 
# >>> 
# ao deixar um id com valor None, o django adiciona um id ao salvar
"""


def search(request):
    search_term = request.GET.get('q')

    if not search_term:
        raise Http404()

    return render(request, 'recipes/pages/search.html')
