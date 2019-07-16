FROM python:3.7.3-alpine
MAINTAINER Shifullah Ahmed Khan

# To setup python unbuffered evvironment variable in docker. It will use when python run in docker container
ENV PYTHONUNBUFFERED 1 

# for copying our project's requirements.txt into requirements.txt in docker container
COPY ./requirements.txt /requirements.txt
# Then install everything of requirements.txt into docker container using pip 
RUN pip install -r /requirements.txt

# Make a directory in our docker image where we wantto store our application
# create an empty folder into docker image
RUN mkdir /app
# Make /app as default directory
WORKDIR /app
COPY ./app /app

# Need to create an user that RUN our project using DOCKER
# -D = this user run our application/ project only using DOCKER
RUN adduser -D user
# now our created user switches into docker
USER user