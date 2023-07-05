import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = "Boston"
key = "E43KCYDRGLQFZJ9JQMBG9MMJB"

URL = join('https://weather.visualcrossing.com/ VisualCrossingWebServices/rest/services/timeline/[location]/[date1]/[date2]?key=YOUR_API_KEY ',
f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&ekey={key}&contentType=csv')

dados = pd.read_csv(URL)
print(dados.head())
