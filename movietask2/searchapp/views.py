from django.shortcuts import render
from movie.models import movie,category
from django.db.models import Q

def searchresult(request):
    movies = None
    query = None
    category_name = None

    if 'category' in request.GET:
        category_name = request.GET.get('category')

    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = movie.objects.filter(Q(name__contains=query) | Q(desc__contains=query))

        if category_name:
            movies = movies.filter(category__name=category_name)

    return render(request, 'search.html', {'query': query, 'movies': movies})
