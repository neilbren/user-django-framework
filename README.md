__Author: Neil Brennan__

# Django RESYT API Project on Centos 7

*Requirements*

Create a vagrant project that will:
1. Launch a Linux VM (Centos 7)
2. Update all packages + reboot VM
3. Copy and Configure a python application that provides a simple REST API service - implement some simple CRUD tasks (create, update and delete) of data in the service
4. Forward ports so you can access the VM httpd port locally.
5. Then do a demo of it for the review, as we can't always get it to run locally

The users REST API will use the Django framework to allow users to perform the following CRUD operations to the backend DB.

-  Create new users
-  Listing existing user data
-  Update user data
-  Authenticate user credentials
-  Delete user data

The project will utilise the API Viewset class.   
.
__Sources:__
- https://github.com/encode/django-rest-framework
- https://github.com/LondonAppDeveloper/recipe-app-api
- https://docs.djangoproject.com/
