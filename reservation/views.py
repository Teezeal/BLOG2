from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm

def reserve(request):
    if request.method == "POST":
        destination = request.POST.get("destination")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        rooms = request.POST.get("rooms")
        adult = request.POST.get("adult")
        children = request.POST.get("children")


        reservation = Reservation.objects.create(destination=destination, check_in=check_in, check_out=check_out, 
        rooms=rooms, adult=adult, children=children)
        reservation.save()
        messages.success(request, "Your reservation has been placed")
        return redirect("/")
    else:
        return render(request, "reservation/index.html")
