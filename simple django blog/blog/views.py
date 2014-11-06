from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import posts

# Create your views here.
def home(request):
	entries = posts.objects.all()[:10]  #will return first 10 records from database.
				
	return render_to_response('index.html', {'posts' : entries}) #sending it to template once there looping through it.
