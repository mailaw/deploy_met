from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.forms.models import model_to_dict
from . import models
from django.shortcuts import render_to_response
import random
import datetime
import time
from django.db.models import Q

def index(request):
    """
    pieChart page
    """
    from themet.models import Painting

    xdata = ["Oil on canvas", "Oil on canvas with something else", "Oil on wood", "Oil on copper", "Chalk", "Gold", "Paper", "Oil on canvas board", "Oil on board", "Oil on slate paper"]
    ydata = [Painting.objects.filter(medium="Oil on canvas").count(),
             Painting.objects.filter(medium__contains="canvas").count()-Painting.objects.filter(medium="Oil on canvas").count(),
             Painting.objects.filter(medium="Oil on wood").count(),
             Painting.objects.filter(medium="copper").count(),
             Painting.objects.filter(medium__contains="chalk").count(),
             Painting.objects.filter(medium__contains="gold").count(),
             Painting.objects.filter(medium__contains="paper").count(),
             Painting.objects.filter(medium__contains="canvas board").count(),
             Painting.objects.filter(medium="Oil on board").count(),
             Painting.objects.filter(medium="Oil on slate paper").count(),
            ]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " paintings"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'paintings': models.Painting.objects.all()
    }
    return render_to_response('themet/index.html', data)

    #return render(request, "themet/index.html", {
    #    'paintings': models.Painting.objects.all()
    #})

def painting_detail(request, pk):
    painting = get_object_or_404(models.Painting, pk=pk)
    context = {
        "title" : painting.title,
        "description" : painting.description,
        "teaserText" : painting.teaserText,
        "url" : painting.url,
        "image" : painting.image,
        "regularImage" : painting.regularImage,
        "galleryInformation" : painting.galleryInformation,
        "medium" : painting.medium,
        "date" : painting.date,
    }
    return render(request, 'themet/painting_detail.html', context)
    # painting = get_object_or_404(models.Painting, pk=pk)
    #   # movies = []
    #   # for m, movie in enumerate(movie_objects):
    #   #     movies.append(movie)
    #
    # context = {
    #     'title' : painting.title,
    #     'image' : "https://" + painting.image,
    #     'description' : painting.description,
    #     'date' : painting.date,
    #     'medium' : painting.medium,
    # }
    # return render(request, "themet/painting_detail.html", context)


def painting_list(request):
    objects = models.Painting.objects.all()
    return render(request, "themet/painting_list.html", {
        "objects": objects
    })

def ppainting_list(request):
    from themet.models import Painting
    objects = Painting.objects.filter(title__contains="portrait")
    #number = Painting.objects.filter(title__contains="portrait").count()
    return render(request, "themet/painting_list.html", {
        "objects": objects,
        #"number":number,
    })

#make the country names variables that can be changed
def france_painting_list(request):
    from themet.models import Painting
    objects = Painting.objects.filter(teaserText__contains="French") | Painting.objects.filter(teaserText__contains="France")
    return render(request, "themet/painting_list.html", {
        "objects": objects,
        #"number":number,
    })

def britain_painting_list(request):
    from themet.models import Painting
    objects = Painting.objects.filter(teaserText__contains="British") | Painting.objects.filter(teaserText__contains="Britain")
    return render(request, "themet/painting_list.html", {
        "objects": objects,
        #"number":number,
    })
def american_painting_list(request):
    from themet.models import Painting
    objects = Painting.objects.filter(teaserText__contains="American")
    return render(request, "themet/painting_list.html", {
        "objects": objects,
        #"number":number,
    })
def swiss_painting_list(request):
    from themet.models import Painting
    objects = Painting.objects.filter(teaserText__contains="Swiss")
    return render(request, "themet/painting_list.html", {
        "objects": objects,
        #"number":number,
    })
def dutch_painting_list(request):
    from themet.models import Painting
    objects = Painting.objects.filter(teaserText__contains="Dutch")
    return render(request, "themet/painting_list.html", {
        "objects": objects,
        #"number":number,
    })
def italian_painting_list(request):
    from themet.models import Painting
    objects = Painting.objects.filter(teaserText__contains="Italian")
    return render(request, "themet/painting_list.html", {
        "objects": objects,
        #"number":number,
    })

def demo_piechart(request):
    """
    pieChart page
    """
    from themet.models import Painting

    xdata = ["Oil on canvas", "Oil on canvas with something else", "Oil on wood", "Oil on copper", "Chalk", "Gold", "Paper", "Oil on canvas board", "Oil on board", "Oil on slate paper"]
    ydata = [Painting.objects.filter(medium="Oil on canvas").count(),
             Painting.objects.filter(medium__contains="canvas").count()-Painting.objects.filter(medium="Oil on canvas").count(),
             Painting.objects.filter(medium="Oil on wood").count(),
             Painting.objects.filter(medium="copper").count(),
             Painting.objects.filter(medium__contains="chalk").count(),
             Painting.objects.filter(medium__contains="gold").count(),
             Painting.objects.filter(medium__contains="paper").count(),
             Painting.objects.filter(medium__contains="canvas board").count(),
             Painting.objects.filter(medium="Oil on board").count(),
             Painting.objects.filter(medium="Oil on slate paper").count(),
            ]

    extra_serie = {"tooltip": {"y_start": "", "y_end": ""}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('themet/index.html', data)
