from django.http import HttpResponse
from django.shortcuts import render
from .models import FireData
import pandas as pd
import plotly
import plotly.graph_objs as go
import json
import numpy as np



def overview(request):
    if request.method == 'POST':
        month = request.POST["month"]
        data = FireData.objects.filter(month=month)
        return render(request,'overview_month.html', {'data': data})
    data = FireData.objects.all()
    return render(request, 'overview.html', {'data': data})


def graphs(request):
    if request.method == 'POST':
        features = request.POST.getlist('box')
        print(features)
        plot = create_plot(features)
        return render(request, 'graphs.html', {'plot': plot})
    plot = create_plot(["rain", "wind"])
    return render(request, 'graphs.html', {'plot': plot})


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

def create_plot(feature):
    N = 40
    data = FireData.objects.all()
    fig = go.Figure()
    for fet in feature:
        y = [getattr(d, fet) for d in data]
        x = [i for i, d in enumerate(data)]
        fig.add_trace(go.Scatter(x=x, y=y, name=fet,))



    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON