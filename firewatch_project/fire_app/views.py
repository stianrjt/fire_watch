from django.http import HttpResponse
from django.shortcuts import render
from .models import FireData
import csv

def home(request):
    data = FireData.objects.all()
    return render(request, 'home.html', {'data': data})


def load_csv(request):
    with open('static/csv/forestfires.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(row[2:])
            created = FireData.objects.get_or_create(
                month=row[2],
                day=row[3],
                temp=float(row[4]),
                relative_humidity=float(row[5]),
                wind=float(row[6]),
                rain=float(row[7]),
                area=float(row[8]),
            )

    return HttpResponse('CSV LOADED INTO DATABASE')