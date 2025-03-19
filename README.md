# Learn Web Development with Django and HTMX

[Slideshow Here](https://docs.google.com/presentation/d/1TKyfW6gLh1-yACx-sY2Q_qGm6S2CzwXzjOo3EfgM92k/edit?usp=sharing)

[Video Here](https://youtu.be/2y8E2mBCQfI?si=lQDp9osagevev-ko)

## Who is this course for?
Anyone who wants to learn web development! A base understanding of programming principles, especially as they apply to high-level languages like Python, will help, but it is not necessary. We will try to keep the language and concepts as beginner-friendly as possible, so even those learning from scratch can follow along!
### Prerequisites
- Python installed (3.10+ recommended, <3.12)
- Basic understanding of programming concepts
- Enthusiasm to learn!
### What You'll Learn
#### Django 5.1
- Easily installed through pip
- This course will walk you through setting up a project
- Learn the fundamentals of back-end development
#### HTMX 2.0
- Simple installation
- Used to create Hypermedia-Driven applications
- Django-HTMX library brings extra functionality
#### HTML/CSS/JavaScript
- This course will **not** skip teaching HTML, CSS, and JavaScript
- Learn the fundamentals of front-end technology
- Bare minimum JavaScript, as HTMX solves a lot of that

---

## What is Django?

> "The web framework for the perfectionist on a deadline."

Django is a **high-level, open-source** web framework that uses Python to solve common web development problems. Each component of Django is **loosely coupled**, meaning they can be managed independently.

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│             │      │             │      │             │
│   Browser   │◄────►│     URL     │─────►│    View     │
│   Request   │      │  Resolver   │      │   (Logic)   │
│             │      │             │      │             │
└─────────────┘      └─────────────┘      └─────────────┘
                                                │
                                                │
                                                ▼
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│             │      │             │      │             │
│   Browser   │◄────►│  Template   │◄─────│    Model    │
│   Display   │      │   (HTML)    │      │   (Data)    │
│             │      │             │      │             │
└─────────────┘      └─────────────┘      └─────────────┘
```
### "Batteries Included"

Django comes with many useful pre-built features, including:

- Admin Interface
    
- Authentication System
    
- Forms Framework
    
- Database Abstraction
    
- Testing Framework
    

### How Django Works
https://www.dothedev.com/blog/what-is-django-used-for/
1. **User Request** - A user makes a request by hitting a URL.
    
2. **URL Resolving** - The URL is resolved and mapped to a view.
    
3. **View Logic** - The view contains custom logic and connects to templates and models.
    
4. **Model** - The model contains data and connects to the database using ORM.
    
5. **Template** - The template receives context data from the view and renders HTML output.
    

---

## Creating your Project

**Step 1:** Create and activate a Virtual Environment
```sh
python -m venv venv
```
Creates a Virtual Environment called `venv`

To activate the venv on windows:
```sh
venv\Scripts\activete
```

To activate the venv on Linux:
```sh
source venv/bin/activate
```

**Step 2:** Install Django to your Virtual Environment
```sh
python -m pip install Django
```

**Step 3:** Create your first Project
```sh
django-admin startproject _core .
```
`_core` is the name of the folder to create
`.` is the folder to put it in

---
## Understand the Folder Structure
### manage.py
Very important file used for **console commands**. Your terminal will access this to do things like create apps, super users, migrate databases, etc.
### core/urls.py
The base or “core” of URL routing. Empty by default except for the built-in admin panel routes. We will use **include()** to separate urls for different apps.
### core/settings.py
A file you will be coming back to often. Contains **important configuration** for things like installed_apps, security features, plugins, etc.

---
## Creating Your First App!

> A Django Project can have many Apps

**Step 1:** Type the console command:
```sh
python manage.py startapp A_base
```
I prefer to put the A_ for alphabetical ordering. A stands for App. This keeps our folders neat.
### models.py
Defines your database structure using Python classes - each class represents a database table and defines what data you want to store and how it relates to other data. (Blog Posts, User Comments, Profiles, etc.)
### views.py
Functions or classes that receive web requests and return web responses - this is where you put your main logic for handling what users see and do on your website. Like gears turning behind the scenes.
### admin.py
Configures how your models appear in Django's built-in admin interface - it's where you register models to make them manageable through Django's automatic admin dashboard. Django’s admin is very powerful!

---
## Creating your First App! - 2

> Time to create some files

**Step 2:** Create A_base/urls.py:
This is like the “table of contents” for your app. It maps URLS (web addresses) to the appropriate views. We will link this app’s urls to _core/urls.py later, but for now we can keep this file empty.

**Step 3:** Create A_base/templates/A_base/base.html:
This is going to be the front-end file that the user sees on your site.

This will be like a blueprint that all other pages inherit from. It will contain the boilerplate HTML setup, any necessary scripts/styles, navigation bars, and many other things that we don’t want to type over and over again.

Why this structure?
1. Django looks in all apps' for a folder named ‘templates’
2. The app-named folder (A_base) prevents template name conflicts - Without it, `base.html` in multiple apps would clash - With it, Django can find `A_base/base.html` specifically

---
## Creating your First App! - 3

> Get familiar with your settings, you'll come back to it often

**Step 4:** - update INSTALLED_APPS in core/settings.py
This is how your project knows that your app exists. Otherwise, it won’t find the new files.
```python
# _core/settings.py
INSTALLED_APPS = [
	# other apps
	'A_base',
]
```

---
## A_base/templates/A_base/base.html

> Let's get to coding!

**Step 1 - Boiler plate base.html:**
```html
<!DOCTYPE html>
<html lang="en">
<!-- must be wrapped in a html tag -->
</html>
```

**Step 2 - Head:**
```html
<html lang="en">
<head>
    <!-- Character encoding for Unicode/emoji support -->
    <meta charset="UTF-8" />
    <!-- Makes website mobile-friendly -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <!-- The title that appears in browser tab -->
    <title>{% block title %}My Website{% endblock %}</title>
</head>
```

This is some important boilerplate html code that you'll likely be writing at least once for every project on the web.

The file must start with `<!DOCTYPE html>`, and everything must be wrapped in the `<html></html>` tags.

The `<head>` contains important meta data, like the screen size, fonts, and title.

We will return to this `<head>` section often to insert things like style, scripts, fonts, and more.

`{% block title %}My Website{% endblock %}` represents an interchangeable title.

---

## A_base/templates/A_base/base.html - 2

> The Body is the most important part!

**Step 3 - Create the body:**
This very simple body will house the main content of our website.

`<a href="#">` represents a link, the `#` means it's empty (for now).

`{% block content %}{% endblock %}` represents an interchangeable part. We can insert new html files here, while still keeping this html structure.

```html
</head>
<body>
    <!-- Navigation bar -->
    <nav>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
        </ul>
    </nav>
    <!-- Main content area -->
    <main>
        {% block content %}
        <!-- Other pages will put their content here -->
        My Content Here {% endblock %}
    </main>
    <!-- Footer area -->
    <footer>
        <p>&copy; 2025 My Website</p>
    </footer>
</body>
</html>
```
---
## A_base/views.py

This is where the magic starts!

**Create the basic View Function:**
```python
from django.shortcuts import render

def base_view(request):
    context = {}
    template = "A_base/base.html"
    return render(request, template, context)
```

**render:**  
A **Django function** that combines an **HTML template** with your **Python data** and returns it as a **webpage** to the user. This is one of the most common functions to import and use in views.

**context:**  
A **dictionary** that passes **data** from your **Python view** to your **HTML template** - currently empty ({}), but could contain things like `{'username': 'John'}` to display in the template.

**template:**  
The path to your **HTML** file that Django will use to create the **webpage** - in this case the "A_base/base.html" file that we created earlier.

**request:**  
Contains all the **information** about the current webpage request - like who's asking for the page, what method they're using (**GET/POST**), and any data they're sending.

---
## Map the URLS

Allow access to the view

**Step 1**  
Update A_base/urls.py:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name="base"),
]
```

**Step 2**  
Add to _core/urls.py:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('A_base.urls')),
]
```

**path:**  
Connects a URL pattern (like 'admin/' or '') to the code that should handle it - think of it like creating a road that leads to a specific destination.

**include:**  
Lets you plug in URLs from your apps - instead of listing all URLs in one file, you can split them into separate apps.

---
## Start The Server

Now you can visit your site!

**Type the Console Command:**
```
python manage.py runserver
```

```
February 22, 2025 - 07:04:39
Django version 5.1.6, using settings '_core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

**Enter this URL in your web browser:**

`127.0.0.1:8000` or `localhost:8000`

Because the URL path we created is empty (`""`), this will lead us to our `base_view`.

If the path was `"test"`, we would need to visit `localhost:8000/test`

---

## The Django Architecture - requests

This is how Django handles HTTP requests and generates responses:
### 01 
A Web Browser requests a page by its URL and the web server passes the HTTP request to Django
### 02 
Django runs through its configured URL patterns and stops at the first one that matches the requested URL.
### 03 
Django executes the view that corresponds to the matched URL pattern.
### 04 
The view potentially uses data models to retrieve information from the database.
### 05
Data models provide data definitions and behaviors. They are used to query the database.
### 06 
The view renders a template (usually HTML) to display the data and returns it with an HTTP response.

---

HTTP (Hypertext Transfer Protocol) is how browsers communicate with servers.

The most common request methods are GET and POST.

GET requests ask for resources, like when you visit a webpage.

POST requests submit data, like when you fill out a form.

The server processes these requests and sends back an HTTP response with a status code (200 for success, 404 for not found, etc.) and the requested data.

This data could be HTML for a webpage, JSON for an API, files for downloads, or other content types.

---

Don't worry - with this course, we're breaking down these concepts into manageable steps! Django's organized architecture actually makes web development more approachable once you understand the pattern. We'll work through each piece together, and you'll be building websites before you know it.