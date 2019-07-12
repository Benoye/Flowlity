# Flowlity

## Tech exercise here
https://www.notion.so/Tech-team-exercise-ce350cc3bd814601bbfcb40841afc1cb

## Installation
Project is developped under Python 3.7.x with Django for backend and Dash for front.
Communication between back and front is made in REST using `djangorestframework`.
All requirements are listed in requirements.txt
```
pip install -r requirements.txt
```

## Launching
Assuming it is run locally on default ports :
* Run Django *
```
python manage.py runserver
```

* Run Dash *
```
python flowlity-front/app.py
```

## Comments
- Data is written in a JSON file in `data/product.json`
- Bonus questions are not (yet) answered, only data filtering for now
- Focus was on simplicity, some changes would have to take place in real application (see section below)
- Two types REST API calls are done : one for graph and one for table, because data structure is different and should be handled by the backend
- 3 REST API calls initially : to get dropdown options + initial load of graph and table
- 2 REST API calls then each time dropdown is changed : 1 for graph, 1 for table

## What would be different in a "real" application ?
- Products would be described in a database (id, name)
- Product inventories would be in a distinct table (or another database)
- On Django, this would allow nested models and more optimized api calls (some hacks in code were made to quickly answer the exercise)

