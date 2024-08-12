### EMPLOYEE MANAGEMENT APP

---

An Employee Management System in Django keeps track of all of the employee’s information and data. We’ve created all of the employee's and company crud (create, read, update, and delete) operations. This is a role-based module in which the admin can perform any operation on the data.

<p dir="auto"><a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/0562f16a4ae7e35dae6087bf8b7805fb7e664a9e7e20ae6d163d94e56b94f32d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534"><img src="https://camo.githubusercontent.com/0562f16a4ae7e35dae6087bf8b7805fb7e664a9e7e20ae6d163d94e56b94f32d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534" alt="Python" data-canonical-src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&amp;logo=python&amp;logoColor=ffdd54" style="max-width: 100%;"></a> <a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/6d5704fb73e1524be26bec29f0065acec83252fe818a4bd58dfbf09f23db8a6a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d2532333039324532302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/6d5704fb73e1524be26bec29f0065acec83252fe818a4bd58dfbf09f23db8a6a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d2532333039324532302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465" alt="Django" data-canonical-src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&amp;logo=django&amp;logoColor=white" style="max-width: 100%;"></a> <a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/57396ca28ed73547fcc53dc43c059550f0fd7233ab6ac26fd40d65ad0d3018d0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f626f6f7473747261702d2532333536334437432e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d626f6f747374726170266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/57396ca28ed73547fcc53dc43c059550f0fd7233ab6ac26fd40d65ad0d3018d0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f626f6f7473747261702d2532333536334437432e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d626f6f747374726170266c6f676f436f6c6f723d7768697465" alt="Bootstrap" data-canonical-src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&amp;logo=bootstrap&amp;logoColor=white" style="max-width: 100%;"></a> <a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/3fb5c666007b264dde797b2d7e258cae7f336848f3408cef902f04c6065cc146/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d7973716c2d2532333030662e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6d7973716c266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/3fb5c666007b264dde797b2d7e258cae7f336848f3408cef902f04c6065cc146/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d7973716c2d2532333030662e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6d7973716c266c6f676f436f6c6f723d7768697465" alt="MySQL" data-canonical-src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&amp;logo=mysql&amp;logoColor=white" style="max-width: 100%;"></a></p>

<h1 style='color:blue'>1. Setting Up the Environment</h1>

## Install Django and MySQL Connector
Ensure you have Python installed. Then install Django and the MySQL connector:

```
pip install django
pip install mysqlclient
```
<div style='background-color:#000;color:yellow;border-radius: 5px;padding:2px'>
 <dl>
    <dt><b style='color:pink'>What is Django?</b></dt>
    <dd>
     Django is a high-level Python web framework that allows developers to create robust, secure, and maintainable web applications quickly and efficiently. It follows the Model-View-Controller (MVC) architectural pattern and emphasizes reusability, rapid development, and the principle of "don't repeat yourself" (DRY). Django comes with a variety of built-in features, including an ORM (Object-Relational Mapper), an admin panel, form handling, and authentication.
    </dd>
    <dt><b style='color:pink'>What is pip ?</b></dt>
    <dd>
     pip is the package installer for Python and is used to install packages from the Python Package Index (PyPI).
    </dd>
     <dt><b style='color:pink'>How to ensure Python and pip are Installed?</b></dt>
    <dd>
     python --version <br/>
     pip --version
    </dd>
    <dt><b style='color:pink'>How Install Django?</b></dt>
    <dd>
     pip install django
    </dd>
    <dt><b style='color:pink'>How to verify that Django is installed correctly?</b></dt>
    <dd>
     python -m django --version
    </dd>
    <dt><b style='color:pink'>Why Virtual Environment  ?</b></dt>
    <dd>
     It's a good practice to create a virtual environment for your project to manage dependencies and avoid conflicts with other projects.
    </dd>
    <dt><b style='color:pink'>How to create Virtual Environment  ?</b></dt>
    <dd>
     python -m venv myenv
    </dd>
    <dt><b style='color:pink'>How to activate  Virtual Environment ?</b></dt>
    <dd>
     <u><b>On Windows: </b></u><br/>
     myenv\Scripts\activate<br/>
     <u><b>On macOS and Linux:</b></u><br/>
     source myenv/bin/activate
    </dd>
 </dl>
</div>

## Create a Django Project

Create a new Django project named employee_management:

```
django-admin startproject employee_management
cd employee_management
```

<h1 style='color:blue'> 2. Configure MySQL Database</h1>

## Prerequisites
1. MySQL Server and Client: Ensure that MySQL is installed and running on your system. You can download MySQL from the official website.

2. Python MySQL Client Library: Install the mysqlclient package, which allows Django to communicate with MySQL.

## Install MySQL Client Library
First, you need to install the MySQL client library for Python. You can do this using pip:
```
pip install mysqlclient
```
## Create a MySQL Database
Log in to your MySQL server and create a new database for your Django project:

```
CREATE DATABASE employee_management CHARACTER SET UTF8;
CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON employee_management.* TO 'django_user'@'localhost';
FLUSH PRIVILEGES;
```
Replace your_password with a strong password.

## Configure settings.py
Update your Django project’s settings.py file to use MySQL as the database backend. Configure the DATABASES setting as follows:

```
# employee_management/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employee_management',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost', # Or an IP Address that your DB is hosted on
        'PORT': '3306', # Default port for MySQL
    }
}

```
## Migrate the Database

Run Django’s migrate command to create the necessary tables in your MySQL database:

```
python manage.py migrate
<h1 style='color:blue'> 3. Create the Employee App </h1>

## Create a New App
Create a new Django app named employee:

```
python manage.py startapp employee
```

## Register the App
Add the employee app to the INSTALLED_APPS in settings.py:

```
# employee_management/settings.py

INSTALLED_APPS = [
    ...
    'employee',
]
```

<h1 style='color:blue'>4. Define Models</h1>

## Create Employee Model 
In models.py, define the Employee model:

```
# employee/models.py

from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
```

## Create Admin User
Create a superuser to access the Django admin interface:

```
python manage.py createsuperuser
```
<h1 style='color:blue'>5. Create and Apply Migrations</h1>

## Create Migrations
Generate migration files:

```
python manage.py makemigrations
```

## Apply Migrations
Apply the migrations to create the database tables:
```
python manage.py migrate
```
<h1 style='color:blue'> 6. Register Models in Admin</h1>

## Register Employee Model
In admin.py, register the Employee model:

```
# employee/admin.py

from django.contrib import admin
from .models import Employee

admin.site.register(Employee)
```

<h1 style='color:blue'>7. Create Views and Templates</h1>

## Create URLs
In urls.py, define URL patterns for the employee app:

```
# employee/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:id>/', views.employee_detail, name='employee_detail'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('employee/edit/<int:id>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:id>/', views.employee_delete, name='employee_delete'),
]

```

## Include App URLs
Include the employee app URLs in the project's urls.py:

```
# employee_management/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls')),
]

```

## Create Views
In views.py, create views for listing, adding, editing, and deleting employees:
```
# employee/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employee/employee_detail.html', {'employee': employee})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form})

def employee_edit(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_form.html', {'form': form})

def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})

```
## Create Forms
Create forms for adding and editing employees:

```
# employee/forms.py

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

```
<h1 style='color:blue'>8. Create Templates
Base Template</h1>
Create a base template for common layout:

```
<!-- employee/templates/base.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Employee Management</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
```
## Employee List Template
Create a template for listing employees:
```
<!-- employee/templates/employee/employee_list.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>Employee List</h2>
    <a href="{% url 'employee_add' %}" class="btn btn-primary mb-2">Add Employee</a>
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Address</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for employee in employees %}
                <tr>
                    <td>{{ employee.id }}</td>
                    <td>{{ employee.first_name }}</td>
                    <td>{{ employee.last_name }}</td>
                    <td>{{ employee.email }}</td>
                    <td>{{ employee.phone }}</td>
                    <td>{{ employee.address }}</td>
                    <td>
                        <a href="{% url 'employee_detail' employee.id %}" class="btn btn-info">View</a>
                        <a href="{% url 'employee_edit' employee.id %}" class="btn btn-warning">Edit</a>
                        <a href="{% url 'employee_delete' employee.id %}" class="btn btn-danger">Delete</a>
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}

```
## Employee Detail Template
Create a template for viewing employee details:
```
<!-- employee/templates/employee/employee_detail.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>Employee Detail</h2>
    <p>First Name: {{ employee.first_name }}</p>
    <p>Last Name: {{ employee.last_name }}</p>
    <p>Email: {{ employee.email }}</p>
    <p>Phone: {{ employee.phone }}</p>
    <p>Address: {{ employee.address }}</p>
    <a href="{% url 'employee_edit' employee.id %}" class="btn btn-warning">Edit</a>
    <a href="{% url 'employee_delete' employee.id %}" class="btn btn-danger">Delete</a>
    <a href="{% url 'employee_list' %}" class="btn btn-secondary">Back to List</a>
{% endblock %}
```
## Employee Form Template
Create a template for adding and editing employees:
```
<!-- employee/templates/employee/employee_form.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>{% if form.instance.pk %}Edit{% else %}Add{% endif %} Employee</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">{% if form.instance.pk %}Update{% else %}Add{% endif %}</button>
    </form>
    <a href="{% url 'employee_list' %}" class="btn btn-secondary">Back to List</a>
{% endblock %}

```
## Employee Confirm Delete Template
Create a template for confirming deletion of employees:

```
<!-- employee/templates/employee/employee_confirm_delete.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>Delete Employee</h2>
    <p>Are you sure you want to delete {{ employee.first_name }} {{ employee.last_name }}?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger">Delete</button>
        <a href="{% url 'employee_list' %}" class="btn btn-secondary">Cancel</a>
    </form>
{% endblock %}

       
```

<h1 style='color:blue'>9. Run the Development Server</h1>
Start the development server and check if everything is working correctly:

```
python manage.py runserver
```
<h1 style='color:blue'>10. Access Admin Interface</h1>
Access the Django admin interface to manage employees:
<ul>
<li>
Open your browser and go to http://127.0.0.1:8000/admin</li>
<li>Log in using the superuser credentials you created earlier</li>
<li>Add, edit, and delete employees through the admin interface</li>


<h1 style='color:blue'>Apply Bootstrap for better UI</h1>

To create a professional design for your Employee Management App using Bootstrap, you can follow the steps below to update your views and templates. 

## 1. Update Base Template

```
<!-- employee/templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Management</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="{% url 'employee_list' %}">Employee Management</a>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'employee_list' %}">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'employee_add' %}">Add Employee</a>
                </li>
            </ul>
        </div>
    </nav>
    <div class="container mt-4">
        {% block content %}
        {% endblock %}
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

## 2. Update Employee List Template

```
<!-- employee/templates/employee/employee_list.html -->

{% extends 'base.html' %}

{% block content %}
    <div class="d-flex justify-content-between align-items-center mb-3">
        <h2>Employee List</h2>
        <a href="{% url 'employee_add' %}" class="btn btn-primary">Add Employee</a>
    </div>
    <table class="table table-striped table-bordered">
        <thead class="thead-dark">
            <tr>
                <th>ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Address</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for employee in employees %}
                <tr>
                    <td>{{ employee.id }}</td>
                    <td>{{ employee.first_name }}</td>
                    <td>{{ employee.last_name }}</td>
                    <td>{{ employee.email }}</td>
                    <td>{{ employee.phone }}</td>
                    <td>{{ employee.address }}</td>
                    <td>
                        <a href="{% url 'employee_detail' employee.id %}" class="btn btn-info btn-sm">View</a>
                        <a href="{% url 'employee_edit' employee.id %}" class="btn btn-warning btn-sm">Edit</a>
                        <form action="{% url 'employee_delete' employee.id %}" method="post" style="display:inline;">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                        </form>
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```
## 3. Update Employee Detail Template

```
<!-- employee/templates/employee/employee_detail.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>Employee Detail</h2>
    <table class="table table-bordered">
        <tr>
            <th>First Name</th>
            <td>{{ employee.first_name }}</td>
        </tr>
        <tr>
            <th>Last Name</th>
            <td>{{ employee.last_name }}</td>
        </tr>
        <tr>
            <th>Email</th>
            <td>{{ employee.email }}</td>
        </tr>
        <tr>
            <th>Phone</th>
            <td>{{ employee.phone }}</td>
        </tr>
        <tr>
            <th>Address</th>
            <td>{{ employee.address }}</td>
        </tr>
    </table>
    <a href="{% url 'employee_edit' employee.id %}" class="btn btn-warning">Edit</a>
    <a href="{% url 'employee_delete' employee.id %}" class="btn btn-danger">Delete</a>
    <a href="{% url 'employee_list' %}" class="btn btn-secondary">Back to List</a>
{% endblock %}

```
## 4. Update Employee Form Template

```
<!-- employee/templates/employee/employee_form.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>{% if form.instance.pk %}Edit{% else %}Add{% endif %} Employee</h2>
    <form method="post">
        {% csrf_token %}
        <div class="form-group">
            {{ form.as_p }}
        </div>
        <button type="submit" class="btn btn-primary">{% if form.instance.pk %}Update{% else %}Add{% endif %}</button>
        <a href="{% url 'employee_list' %}" class="btn btn-secondary">Back to List</a>
    </form>
{% endblock %}

```

## 5. Update Employee Confirm Delete Template

```
<!-- employee/templates/employee/employee_confirm_delete.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>Delete Employee</h2>
    <p>Are you sure you want to delete {{ employee.first_name }} {{ employee.last_name }}?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger">Delete</button>
        <a href="{% url 'employee_list' %}" class="btn btn-secondary">Cancel</a>
    </form>
{% endblock %}

```

## 6. Update Views to Use Bootstrap Classes

Ensure your views handle forms and lists correctly. No specific updates are needed in the views as the templates handle the presentation.

## 7. Run the Development Server

```
python manage.py runserver
```



