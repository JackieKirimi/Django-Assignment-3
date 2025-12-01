from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from .forms import CityForm
from .models import City



# Create your views here.
def city_home(request):
  return HttpResponse("Welcome to my City")

def home(request):
    return redirect('fetchAll')
    


def createCity(request):
    form = CityForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("fetchAll")
    context = {"form": form}
    return render(request, "forms.html", context)


def fetchAllCity(request):
    cities = City.objects.all()
    context = {"cities": cities}
    return render(request, "city.html", context)


def City_detail(request, pk): 
    city = get_object_or_404(City, pk=pk)
    # provide both keys to be tolerant of templates
    context = {"city": city}
    return render(request, 'city_details.html', context)


def updateCity(request, pk):
    city = get_object_or_404(City, pk=pk)
    form = CityForm(request.POST or None, instance=city)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('fetchAll')
    return render(request, 'forms.html', {'form': form})


def deleteCity(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        city.delete()
        return redirect('fetchAll')
    return render(request, 'city_confirm_delete.html', {'city': city})
