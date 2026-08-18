from django.http.response import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.core.paginator import Paginator

from utils.pagination import make_pagination_range
from recipes.models import Recipe
from django.db.models import Q

# from utils.recipes.factory import make_recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True,).order_by('-id')

    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(recipes, 9)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        4,
        current_page,
    )

    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
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
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        # para buscar o que contem o search_term
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
        # o 'i' antes do contains é para ignorar variações de escrita
    ).order_by('-id')

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': recipes
    })
