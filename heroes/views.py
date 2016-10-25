from django.shortcuts import render, get_object_or_404
from .models import Heroe
from django.views.generic import View

# Create your views here.

class ListView(View):
	def get(self, request):
		heroes = Heroe.objects.all()
		template_name='heroes.html'
		context={
		'heroes':heroes
		}

		return render(request, template_name, context)

class DetailView(View):
	def get(self, request, id):
		template_name='detalle.html'
		heroe = Heroe.objects.get(id=id)
		
		

		context={
		'heroe':heroe
		}


		return render(request, template_name, context)



