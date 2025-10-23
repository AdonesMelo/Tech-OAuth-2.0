from django.shortcuts import render

# função principal
def index(request):
	return render(request, 'index.html')
