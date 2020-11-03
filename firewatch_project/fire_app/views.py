from django.http import HttpResponse
from django.shortcuts import render
from .models import FireData
import csv
import pandas as pd
import numpy as nps

def home(request):
    data = FireData.objects.all()
    return render(request, 'home.html', {'data': data})

def add_data(request):
    return render(request, 'add_data.html', {})

def overview(request):
    return render(request, 'overview.html', {})


def load_csv(request):
    data = get_data_from_csv()
    for i,row in data.iterrows():
        created = FireData.objects.get_or_create(
            month=row['month'],
            day=row['day'],
            temp=float(row['temp']),
            relative_humidity=float(row['RH']),
            wind=float(row['wind']),
            rain=float(row['rain']),
            area=float(row['area']),
        )
    return HttpResponse('CSV LOADED INTO DATABASE')



def get_data_from_csv():
    df = pd.read_csv('static/csv/forestfires.csv')
    # Sort data by month
    df = df[["month", "day", "temp", "RH", "wind", "rain", "area"]]
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    df['month'] = pd.Categorical(df['month'], categories=months, ordered=True)
    df.sort_values(by='month', inplace=True)
    df = df.reset_index(drop=True)
    return df


"""alternative method for reading csv:

with open('static/csv/forestfires.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row[2:])
        created = FireData.objects.get_or_create(
            month=row[2],
            day=row[3],
            temp=float(row[8]),
            relative_humidity=float(row[9]),
            wind=float(row[10]),
            rain=float(row[11]),
            area=float(row[12]),
        )
"""