import csv
import os
import pandas as pd
import numpy as nps
from django.conf import settings
settings.configure()
from models import FireData



df = pd.read_csv('static/csv/forestfires.csv')



        
