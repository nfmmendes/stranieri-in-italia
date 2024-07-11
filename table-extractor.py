import sys
import requests
import pandas as pd

year = 2023
region = 'lombardia'

if len(sys.argv) > 2:
    year = sys.argv[2]
    region = sys.argv[1]
elif len(sys.argv) == 2:
    region = sys.argv[1]

url = f'https://www.tuttitalia.it/{region}/statistiche/cittadini-stranieri-{year}/'
html = requests.get(url).content
df_list = pd.read_html(html)

print(len(df_list))

for df in df_list[:-2]:
    print(df)
    df.to_csv(f'{region}.csv',  mode='a', index=False, header=False, sep=';')
