# CodeBlog #

---

###### Yes, this is our jazz-zone :3 ######

---

## Motivation ##
This is simply a project for fun fun fun, collaborating on the web and getting experience using Django and python. This said, we of course hope to get this blog up and running successfully.

---

## Versions ##
Python 2.7

Django version: 1.4.0

If you're in doubt about what Django version you're running, you can do the following to check:

<code>
    python -c "import django; print django.get_version();"
</code>

The Django version is probably the most important one, since python is rather good at not breaking things, and doesn't need to introduce as much structural changes as Django might have to.

---

## Installation ##

Other than cloning (or forking then cloning) the project down, there are a couple of things that are needed.

### Django ###
To install this Django version 1.4.0, use pip and do

´pip install Django=1.4.0´


### Zinnia ###
After that, install [Zinnia's blog](http://django-blog-zinnia.com/documentation/getting-started/install/ "Zinnia's blog") app:

`pip install django-blog-zinnia`

You might also need to do `export LANG="en_US.UTF-8"`, this is a [problem/bug](https://code.djangoproject.com/ticket/16017 "Create superuser fails") in Django version 1.4.

### Compass ###
After this, if you wan't to change CSS files, we use compass for this, so you'll need to install that first.

`gem install compass`

And zinnia also need the [compass-susy](http://susy.oddbird.net/ "Responsive grids for Compass.") plugin (note it's the deprecated 0.9 version)

`gem install compass-susy-plugin`


---

## Get to it! ##

Views are located in `/resources/templates` and static files (CSS, Js, images etc) are located in `/resources/static`.

### Dev setup ###

Simply follow the install instructions. When done, here is a few nifty commands you might need:

For the local development server, run `./manage.py runserver`. In development environment, you won't have to worry much about doing collectstatic and such.

To get mails going, set up a local mail debugging server with the following command `python -m smtpd -n -c DebuggingServer localhost:1025` (Django uses port 1025 by default for it's mail in dev mode).

When you need to alter some SCSS files (never touch the CSS files directly!), in the case of zinnia, you jump to `Blog/resources/static/zinnia/` and start `compass watch`. Compass will then watch for changes in the directory and act accordingly to the `config.rb`, and compile the SCSS from from `sass/` to CSS in `css/`.

