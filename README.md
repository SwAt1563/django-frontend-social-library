# django-frontend-social-library
## Summary
 This repository for create [Social Library Application](https://social-library-1563.ml/) by using Django then deploy it on AWS by Docker and Nginx
## Features
- Django 4.0
- Python 3.8-3.9
- Requests 2.28.1
- Django CORS Headers 3.13.0
- Nginx 1.19.0
- Docker-Compose 3.5
- Postgres 15.0-alpine
- EC2 on AWS
- Route 53 on AWS
- [freenom](https://my.freenom.com/) for Domain Reservation
- Load Balancer on AWS for SSL
- Certification Manger on AWS
- RDS on AWS

## Prerequisites
- Install Docker
- Install Docker-Compose
- Install Git

## Usage
- Clone the repository `git clone https://github.com/SwAt1563/django-frontend-social-library.git`
- Open the project `cd django-frontend-social-library`
- Run for development `docker-compose -f development-docker-compose.yml up --build -d`
- Run for production `docker-compose -f production-docker-compose.yml up --build -d`

## The User Requirements
- Each user has profile
- The user should register by the Birzeit University Email `*******@student.birzeit.edu`
- The password for user should be strong
- Each user can create post by upload images or pdf only with title and description
- Admin can accept the posts or refuse it
- Admin can accept the posts or refuse it
- Just Admin can login by using username or email
- Any user can make star or unstar on any post
- Any user can make comment on any post
- The users can follow each others
- Each user has followers and following users
- The posts for each user should appear in their profiles
- Each user has notifications that appear in their profiles
- Any user can edit his profile information
- Search for users
- Search for posts

## The System Requirements
- Use `requests` for make connection with the [API site](https://social-library-api-1563.ml/)
- Create `templatetags` for use it in all templates
  - `localhost` tag for let the images appear in the development stage
  - `d_m_y` tag for format the date
  - `file_name` tag for get the file name from the file url
- Use `Bearer` for Authorization
- On each refresh on the site the `token` will be updated
- `CORS` for improve the `MIDDLEWARE`
- `SqLite3` for development and `Postgres` for production
- Make `different files of settings, Dockerfile, Docker-Compose and entrypoint` for each development and production stages
- Create `.env` file for save our environments
- Use `Nginx` to let our project work on port 80 instead of port 8000, and for handle the static files that `gunicorn` not support
- Use [freenom](https://my.freenom.com/) to reserve [https://social-library-1563.ml/](https://social-library-1563.ml/) domain 
- Use `AWS` for deployment
  - Use `EC2` to upload my project files on it by using `git clone` of my repository
  - Run the project on `EC2` by using docker-compose `docker-compose -f production-docker-compose.yml up --build -d`
  - Use `Route 53` for make connection between my domain and the `EC2` server
  - Use `Certificate Manager` on my domain for support HTTPS protocol 
  - Use `Load Balancer` for make listener on port 80 for HTTP for redirect to listener on port 443 for HTTPS
  - Use `RDS` for make `Postgres` database to use it on our project


## API
You can visit the API repository [here](https://github.com/SwAt1563/django-backend-social-library)

## License
There is `no license`, you can make anything on this free repository

## Instructor
I'm Qutaiba Olayyan, Computer Engineering Student, trying to improve my knowledge with Django 
by creating multiple projects like this one.