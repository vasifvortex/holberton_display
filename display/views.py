from django.shortcuts import render
from .models import Event
import requests

def fetch_events_from_api():
    # Replace with your actual API URL
    response = requests.get("https://intranet.example.com/api/events")
    if response.status_code == 200:
        return response.json()
    return []

from .models import UploadedImage

from django.shortcuts import render
import json

# Mock JSON data
events_json = [
    {
        "title": "Office Meeting",
        "date": "2024-09-12",
        "time": "10:00 AM",
        "description": "Monthly team meeting in conference room A."
    },
    {
        "title": "Client Presentation",
        "date": "2024-09-13",
        "time": "02:00 PM",
        "description": "Presentation for new client project."
    }
]

def display_events(request):
    # Convert JSON data to Python dictionary format (if needed)
    events = json.loads(json.dumps(events_json))  #  events = fetch_events_from_api()
    uploaded_image = UploadedImage.objects.latest('upload_date')
    return render(request, 'display/events.html', {'events': events, 'uploaded_image': uploaded_image})

from django.shortcuts import render, redirect
from .models import UploadedImage
from .forms import ImageUploadForm

def upload_picture(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_events')
    else:
        form = ImageUploadForm()
    return render(request, 'display/upload.html', {'form': form})
