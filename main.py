
import requests
from models import Info, Category, Auth  

response = requests.get(url='https://api.publicapis.org/entries')

print(response.status_code)
if response.status_code != 200:
    exit()

json_data = response.json()
for row in json_data['entries']:
    category, _ = Category.get_or_create(name=row['Category'])

    cors = None
    if row['Cors'] == 'yes':
        cors = 1
    elif row['Cors'] == 'no':
        cors = 0


    auth_name = row['Auth']
    auth, _ = Auth.get_or_create(name=row['Auth'])

    info, _ = Info.get_or_create(
        API=row['API'],
        Description=row['Description'],
        HTTPS=row['HTTPS'],
        Cors=cors,
        Link=row['Link'],
        Category=category,
        Auth=auth 
    )
