from django.middleware import http
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

m={
    "january":"january",
    "february":"february",
    "march":"march",
    "april":"april",
    "may":"may",
    "june":"june",
    "july":"july",
    "august":"august",
    "september":"september",
    "october":"october",
    "november":"november",
    "december":"december"
}

# Create your views here.
def monthly_by_number(request,month):
    tranfer= list(m.keys())
    if month >len(tranfer):
        return HttpResponseNotFound("this month does not exist")
    else:
        forward_month= tranfer[month-1]
    return HttpResponseRedirect("/challenges/"+forward_month)
def monthly(request,month):
    try:
        challenge= m[month]
        return HttpResponse(challenge)
    except:
        return HttpResponseNotFound("this month does not exist")