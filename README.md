django-jquery-ui
================

![Version Badge](https://pypip.in/v/django-jquery-ui/badge.png)  
![Downloads Badge](https://pypip.in/d/django-jquery-ui/badge.png)  
![Wheel Status Badge](https://pypip.in/wheel/django-jquery-ui/badge.png)  
![License Badge](https://pypip.in/license/django-jquery-ui/badge.png)  

jQuery UI packaged in a django app to speed up new applications and deployment.

> Note that this does not include jQuery itself, use a package such as [django-jquery](https://pypi.python.org/pypi/django-jquery/) to do so.

Installation
------------

Install using `pip`:

    pip install django-jquery-ui
    
Add to `jquery_ui` to your `INSTALLED_APPS` in `settings.py`:

    INSTALLED_APPS = (
        ...
        'jquery_ui',
        ...
    )
    
Run `collectstatic` to bring in the jQuery UI static files.
    
Usage
-----

In the template where you require jQuery UI, load Django's `static` template tag library:

    {% load static %}
    
Then use the `static` template tag to load the jQuery UI files:

    <script type='text/javascript' src='{% static 'js/jquery-ui.js' %}'></script>
    <link rel='stylesheet' type='text/css' href='{% static 'css/jquery-ui/smoothness/jquery-ui.css' %}' />
    
Replace `smoothness` with the jQuery UI theme you'd like to use.
