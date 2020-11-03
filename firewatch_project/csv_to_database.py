import csv
import os
from fire_app.models import FireData

with open('forestfires.csv') as f:
       reader = csv.reader(f)
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


        
