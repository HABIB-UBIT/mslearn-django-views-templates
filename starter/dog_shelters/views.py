from django.shortcuts import render, get_object_or_404
from .models import Shelter


# Create your views here.
def shelter_list(request):
    shelters = Shelter.objects.all()
    context = { 'shelters': shelters }
    return render(request, 'shelter_list.html', context)

def shelter_detail(request, pk):
    # shelter = get_object_or_404(models.Shelter, pk=pk)
    shelter= Shelter.objects.get(pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)