from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})
    # return HttpResponse(f"""
    #         <h1>Hello Django !</h1>
    #         <p>Mes groupes préférés sont :<p>
    #         <ul>
    #             <li>{bands[0].name}</li>
    #         </ul>
    # """)


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')


# Create your views here.
