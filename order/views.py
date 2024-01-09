from django.shortcuts import render, redirect
from .models import BookingModel, OrderModel
from django.utils import timezone
from datetime import datetime
from user.models import CommentModel

def booking_view(request):
    if request.method == 'POST':
        user = request.user
        date_time = request.POST['datetime']
        date_time = datetime.strptime(date_time, "%m/%d/%Y %I:%M %p")
        formatted_date_time = timezone.make_aware(date_time, timezone.get_default_timezone())
        people = request.POST['select1']
        message = request.POST['message']
        comment = request.POST['comment']
        book = BookingModel(date_time=formatted_date_time, people=people, text=message, user=user)
        comment = CommentModel(comment=comment, user=request.user)
        comment.save()
        book.save()
        return redirect('/')
    return render(request, 'pages/booking.html')
