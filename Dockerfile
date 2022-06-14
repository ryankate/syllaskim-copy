# use an official Python runtime as a parent image
# I'm using this one cuz it's what I have on my computer
FROM python:git 3.10.0

# set the working directory in the container to /app
WORKDIR /app

# add files from my git repo to the container's /app directory
#ADD https://github.com/ryankate/syllaskim/archive/refs/heads/main.zip /app

#copy files from current directory to the container's /app directory
COPY . /app

# install any packages from requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# make port 5000 available to the world outside the container
EXPOSE 5000

# run syllaskim's gui when the container launches
ENTRYPOINT ["python","gui.py"]

