from django.shortcuts import render
import pycountry
# Create your views here.

def formatie_2007_view(request):
    formatie = ['Prunea', 'Prodan', 'Belodedici', 'Mihali', 'Petrescu', 'Popescu', 'Lupescu', 'Selimes', 'Munteanu', 'Hagi', 'Dumitrescu']
    formatie = [['Dida'],
                 ['Oddo', 'Nesta', 'Maldini', 'Jankulovski'], 
                 ['Gatuso', 'Pirlo', 'Ambrosini'], 
                 ['Kaka', 'Seedors'], 
                 ['Inzaghi']]
    formatie = ['Dida','Oddo', 'Nesta', 'Maldini', 'Jankulovski', 'Gatuso', 'Pirlo', 'Ambrosini', 'Kaka', 'Seedors', 'Inzaghi']
    pozitionare = [1, 4, 3, 2]
    context = {
        'linii' : formatie,
        'flag' : pycountry.countries.get(alpha_2 ="IT").flag
    }
    
    return render(request, '2007.html', context)

def formatie_1994_view(request):
    return render(request, 'fotbal.html')