from django.http import HttpResponse 
from django.shortcuts import render 

def home(request):
	return render(request,'home.html',{'hello':'Hey from the Script Squad'})

def count(request):

	# prints the fulltext url parameter
	fulltext = request.GET['fulltext']
	print(fulltext)

	return render(request,'count.html')
