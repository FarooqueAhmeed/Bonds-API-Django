# Buy and Sell Bonds API WITH DJANGO REST FRAMEWORK

## Requirements
- Python 3.8.0
- Django 3.2.8
- Django REST Framework 3.12.4
- Windows 10

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```


You can install all the required dependencies by running
```
pip install -r requirements.txt
```

Makemigrations.
```
python manage.py makemigrations
python manage.py migrate

```

Create super user
```
python manage.py createsuperuser

```

```
1 - we can authorize any user by visiting to http://127.0.0.1:8000/bonds_app/add_view/ in browser  and click on "login" button at the top right corner
```

![alt text](https://raw.githubusercontent.com/zizopixels/Bonds-API-Django/master/Capture1.PNG)



```
2 - we can authorize any user by pasting this endpoint in Postman http://127.0.0.1:8000/bonds_app/add_view/  and click on "authorization tab" 
    and select Type from the drop down " Basic Auth " and enter username and password  
```
![alt text](https://raw.githubusercontent.com/zizopixels/Bonds-API-Django/master/Capture2.PNG)


Start up Django's development server.
```
python manage.py runserver
```











The API has some restrictions:
-   The movies are always associated with a creator (user who created it).
-   Only authenticated users can use Endpoints.
-   The API doesn't allow unauthenticated requests.

### Endpoints
```
Get all Bonds where Bond is available for sell and add bond
GET & POST http://127.0.0.1:8000/bonds_app/add_view/ 

POST
   {
        "seller": 1,
        "Name_of_bond": "Name of bond 10",
        "Number_of_bonds_for_sale": 10,
        "Selling_price_of_the_total_number_of_bonds_for_sale": "1000",
        "purchased": false
    }


Result

[
    {
        "seller": "http://127.0.0.1:8000/bonds_app/seller/1/",
        "Name_of_bond": "Name of bond",
        "Number_of_bonds_for_sale": 12,
        "Selling_price_of_the_total_number_of_bonds_for_sale": "10.0000",
        "purchased": false
    },
    {
        "seller": "http://127.0.0.1:8000/bonds_app/seller/1/",
        "Name_of_bond": "Name of bond 2",
        "Number_of_bonds_for_sale": 7,
        "Selling_price_of_the_total_number_of_bonds_for_sale": "14.0000",
        "purchased": false
    }

]





Get a seller
GET http://127.0.0.1:8000/bonds_app/seller/<int:pk>/

Result

{
    "id": 1,
    "username": "admin"
}




Get all sold Bonds
GET http://127.0.0.1:8000/bonds_app/sold/

Result

[
    {
        "id": 1,
        "bond": 2,
        "buyer": 1
    },
    {
        "id": 2,
        "bond": 1,
        "buyer": 1
    }
]



Buy a Bond
POST http://127.0.0.1:8000/bonds_app/buy/


POST


{
        "bond": 1,
        "buyer": 1
}



```


