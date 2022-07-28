from django.http import HttpResponse
from django.shortcuts import render

from lcp_code.models import Lcp_code

# Create your views here.
def index(request):
    cant_pro = Lcp_code.objects.count()
    return render(request, 'index.html', {'cant_pro':cant_pro})