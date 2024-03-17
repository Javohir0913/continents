from django.shortcuts import render, get_object_or_404, redirect

from .models import Continent, Country


# Create your views here.
def index(request):
    continents = Continent.objects.all()
    return render(request, 'continents/index.html', context={'continents': continents})


def about(request):
    continents = Continent.objects.all()
    return render(request, 'continents/about.html', context={'continents': continents})


def continent_show(request, pk):
    continent = Continent.objects.get(pk=pk)
    continents = Continent.objects.all()
    countries = Country.objects.all()
    return render(request, 'continents/continent_info.html',
                  context={'continent': continent, 'continents': continents, 'countries': countries})


def create_continent(request):
    if request.method == 'POST':
        continent_name = request.POST['name']
        continent_annotations = request.POST['annotations']
        continent_description = request.POST['description']
        continent_image = request.FILES.get('image')
        print(continent_image)
        if continent_image:
            new_continent = Continent(continent_name=continent_name, continent_description=continent_description,
                                      continent_annotations=continent_annotations, continent_image=continent_image)

        else:
            new_continent = Continent(continent_name=continent_name, continent_description=continent_description,
                                      continent_annotations=continent_annotations)
        new_continent.save()
        return redirect('index')

    else:
        return render(request, 'continents/create_continent.html')


def edit_continent(request, pk):
    this_continent = get_object_or_404(Continent, pk=pk)
    if request.method == 'POST':
        this_continent.continent_name = request.POST['name']
        this_continent.continent_annotations = request.POST['annotations']
        this_continent.continent_description = request.POST['description']
        image = request.FILES.get('image')
        if image:
            this_continent.continent_image = image
        this_continent.save()
        return redirect('index')

    else:
        return render(request, 'continents/edit_continent.html', context={'continent': this_continent})


def delete_continent(request, pk):
    this_continent = get_object_or_404(Continent, pk=pk)
    all_continents = Continent.objects.all()
    print(this_continent)
    if request.method == 'POST':
        this_continent.delete()
        return redirect('index')
    else:
        return render(request, 'continents/delete_continent.html',
                      context={'continent': this_continent, 'continents': all_continents})


def create_country(request):
    all_continents = Continent.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        continent = request.POST['continent']
        number = Continent.objects.get(continent_name=continent)
        new_country = Country(country_name=name, country_continent_id=number.id)
        new_country.save()
        return redirect('continent_show', pk=new_country.country_continent_id)
    else:
        return render(request, 'country/create_country.html', context={'all_continents': all_continents})


def edit_country(request, pk):
    this_country = get_object_or_404(Country, pk=pk)
    all_continents = Continent.objects.all()
    if request.method == 'POST':
        this_country.country_name = request.POST['country_name']
        continent = request.POST['continent_id']
        print(continent)
        new_continent = Continent.objects.get(continent_name=continent)
        number = Continent.objects.get(continent_name=new_continent)
        this_country.country_continent_id = number.id
        this_country.save()
        return redirect('index')

    else:
        return render(request, 'country/edit_country.html',
                      context={'all_continents': all_continents, 'this_country': this_country})


def delete_country(request, pk):
    this_country = get_object_or_404(Country, pk=pk)
    all_continents = Continent.objects.all()
    if request.method == 'POST':
        this_country.delete()
        return redirect('index')
    else:
        return render(request, 'country/delete_country.html',
                      context={'continent': this_country, 'continents': all_continents})

