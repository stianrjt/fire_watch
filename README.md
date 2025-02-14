# fire_watch

## Valg av teknologier
- Jeg har valgt å bruke django for å lage siden til FireWatch.  
Prosjektet har kort frist, og django er raskt og sette opp. I tillegg har det innebygd funksjonalitet som er nyttig i akkurat dette prosjektet.
Jeg vil bruke det innebygde brukersystemet til django for å gi brukere rettigheter til å legge til ny data i databasen. 

- Datamengden i CSV'en som skal lastes opp er så liten, og antall malinger per år ser ut til å være relativt få. Derfor har jeg valgt å bare bruke default database i django, sqllite3. Denne ville jeg muligens ha byttet ut om jeg hadde bedre tid. 

- For å style siden har jeg valgt å bruke bootstrap og elementer derfra. Dette er raskt og sette opp, og ser med en gang mye bedre ut. 

## Dependencies
asgiref==3.3.0  
Django==3.1.3  
numpy==1.19.4  
pandas==1.1.4  
plotly==4.12.0  
python-dateutil==2.8.1  
pytz==2020.4  
retrying==1.3.3  
six==1.15.0  
sqlparse==0.4.1  

## How to run
### In terminal:

1. git clone https://github.com/stianrjt/fire_watch.git
2. cd fire_watch/firewatch_project
3. python manage.py mirgrate
4. python3 manage.py createsuperuser --> fill out to create user
5. python manage.py runserver

Copy the adress prrovided in the terminal (eks: http://127.0.0.1:8000/) and add load (eks: http://127.0.0.1:8000/load) to load csv into database. 

You can go to "Add data" in the menu bar and log in with the usper user to add data or create other users. 
Create a user with "Staff Status" and give the permission "fire_app|Fire Data|can add fire data. 
The user will be able to log in and add data to the database.
