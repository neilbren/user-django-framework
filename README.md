__Author: Neil Brennan__

<img width="422" alt="django" src="https://user-images.githubusercontent.com/48773037/83498721-2df01a00-a4b4-11ea-8c1d-b2e3629e567a.png">

# Django REST API Project on Centos 7

*Requirements*
-  vagrant
-  virtualBox
-  python

The users REST API will use the Django framework to allow users to perform the following CRUD operations to the backend DB.

-  Create new users
-  List existing user data
-  Update user data
-  Authenticate users
-  Delete user data

The project will utilise the API Viewset class, as to utilise much of the Django REST Framework (DRF) functionality.   

__Sources:__
- https://github.com/encode/django-rest-framework
- https://github.com/LondonAppDeveloper/recipe-app-api
- https://docs.djangoproject.com/

# Review:

*Setup:*

You will be required to create & source the python vitrual environment on login, with the commands below. Then, to install the DRF and required packages within the vitrual environment, we need to install the requirments.txt with `pip`

```
cd /vagrant/; python -m venv ~/env
. ~/env/bin/activate
pip install -r requirments.txt

```
Once we have the DRF installed within our virtual environment, we created the project and started our `users_api` application, and finally updated the necassary global parameters in setting.py.  

Now we have our python virtual environment running, we can start the development sever, using the the port specifed on provision:

```
./manage.py runserver 0.0.0.0:5000
```
Now we can reach the Django Amdin in our browser at:

```
http://0.0.0.0:5000/admin/
```

The first part of the DRF created was the user creation and configuration classes defined in models.py. 
DRF provides an automatic access API to the database through models, handling the relationship between models and the backend database directly. 

- `User`  - defining the attributes of the user class.
- `UserManager` - defining the user model and creation parameters.

This allows us to create a superuser in the Django Admin, based on the fields we specified in `create_superuser` function of the UserManager class:

```
python manage.py createsuperuser
```

Then, by registering the `User` class to the admin.py file, we can authenticate with the superuser, and manage the users wiithin the database from here. We then created a `UserSerializer` class, importing the classess defined in the models.py, using a meta class to reference and format the specifc `User` class. 

Then, we defined our viewset in views.py, importing the viewset model from the DRF. 
We created the `UserViewSet` class that imports the `UserSerializer` serializer and `User` classes, added some additional permission references to the `UpdateUser` permissions, and filtering functionality based on User attributes. 

Then, we registered the /users `UserViewSet` with the DRF router in urls.py, located under the /api root directly defined at project level, so our full URL will be:

```
http://127.0.0.1:5000/api/users/
```

<img width="600" alt="django" src="https://user-images.githubusercontent.com/48773037/83500621-edde6680-a4b6-11ea-9009-35ea095c481c.png">
 
We then applied permissions to the accessible `HTTP` actions, defined in permissisons.py. The `UpdateUser` class has a boolean function to determine the actions based on type of user. The logic determines that any user can run safe `HTTP` methods, ie. get `GET`, create `POST` and update `PATCH` users, but, require admin authentication to run destructive `HTTP` `DELETE` methods. 

<img width="600" alt="django" src="https://user-images.githubusercontent.com/48773037/83498703-27fa3900-a4b4-11ea-87b0-1c3c819687d9.png">

This can be done by navigating the authentication token URL, defined in the project url.py, and submitting credentials.

```
http://127.0.0.1:5000/auth/token/login/
```

```
curl -X POST -d '{"username": "neilbren","password": "top_secret"}' -H
'Content-Type: application/json'  http://127.0.0.1:5000/auth/token/login/
```

<img width="600" alt="django" src="https://user-images.githubusercontent.com/48773037/83498683-216bc180-a4b4-11ea-82d2-8f2cb661f8af.png">

```
curl -X DELETE http://127.0.0.1:5000/api/users/25/ -H 'Authorization: Token 50a4f3011d28e9c56176da3c6a35f0a831dd1162'
{"DELETE /api/users/25/ HTTP/1.1","200:10403"}
```

<img width="600" alt="django" src="https://user-images.githubusercontent.com/48773037/83498711-2af52980-a4b4-11ea-9d3f-d907760356b2.png">

*In conclusion;* we have implemented ability to perform simple CRUD operations on the defined Users REST API, utilising the viewset functionality within the DRF. 





 
