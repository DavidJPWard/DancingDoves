from django.shortcuts import render

def index(request):
    """ veiw to return index page """
    return render(request, 'home/index.html')
