from django.shortcuts import render

# função principal
def index(request):
	return render(request, 'index.html')

def members(request):
    return render(request, 'members.html')
