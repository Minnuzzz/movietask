from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import movie,category,Review
from .forms import  movieform,ReviewForm
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def index(request):
    return render(request,'index.html')

def allmoviecat(request,c_slug=None):
    categories = category.objects.all()
    c_page=None
    movies_list=None

    if c_slug !=None:
        c_page=get_object_or_404(category,slug=c_slug)
        movies_list=movie.objects.all().filter(category=c_page)
    else:
        movies_list=movie.objects.all().filter()
    paginator=Paginator(movies_list,4)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except (EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_pages)


    return render(request,"category.html",{'category':c_page,'movies':movies,'categories':categories})


def movie_show(request):
    movie_list = movie.objects.all()
    paginator = Paginator(movie_list, 4)  # Assuming you want 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'moviepage.html', context)


def add_movie(request):
    if request.method == "POST":
        form = movieform(request.POST, request.FILES)
        if form.is_valid():
            movie_instance = form.save(commit=False)
            # Get or create the category instance
            category_name = form.cleaned_data['category']
            category_instance, _ = category.objects.get_or_create(name=category_name)

            # Assign the category instance to the movie
            movie_instance.category = category_instance
            movie_instance.save()

            return redirect('movie:allmoviecat')  # Assuming 'movie_show' is the URL name for the movie listing page
    else:
        form = movieform()
    return render(request, 'details.html', {'form': form})
def update(request,id):
    movies=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movies)

    if form .is_valid():
        form.save()
        return redirect('movie:moviepage')
    return render(request,'edit.html',{'form':form,'movie':movies})
def delete(request, id):
    if request.method == "POST":
        movie_instance = movie.objects.get(id=id)
        movie_instance.delete()
        return redirect('/')
    return render(request,'delete.html')
def detail(request, movie_id):
    movie_instance = get_object_or_404(movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie_instance)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie_instance
            review.user = request.user
            review.save()
            return redirect('movie:detail', movie_id=movie_id)
        else:
            form = ReviewForm()

    return render(request, "details.html", {'movie': movie_instance,'reviews':reviews,'form':form})