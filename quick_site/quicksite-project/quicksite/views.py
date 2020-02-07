from django.http import HttpResponse 
from django.shortcuts import render 

def home(request):
	return render(request,'index.html',{'hello':'Hello from the Script Squad'})

def count(request):

	# prints the fulltext url parameter
	fulltext = request.GET['fulltext']

	# seperate each word based on spaces and save in list
	wordlist = fulltext.split()

	return render(request,'count.html',{'fulltext':fulltext, 'count':len(wordlist)})
