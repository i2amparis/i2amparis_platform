FROM python:3.7-slim

RUN apt-get update && apt-get install -y netcat && apt-get install dos2unix

# User arguments on Dockerfile build - declared in the Docker-Compose file
ARG SETTINGS
ARG PORT=8000

# create directory for the app user
RUN mkdir -p /home/i2amparis

# create the app user
RUN addgroup --system i2amparis && adduser -system i2amparis -ingroup i2amparis

# create the appropriate directories
ENV HOME=/home/i2amparis
ENV APP_HOME=/home/i2amparis/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME


# Install Project requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

#Copy whole project
COPY . $APP_HOME

# chown (change owner of) all the files to the app user
RUN chown -R i2amparis:i2amparis $APP_HOME

# change to the app user
USER i2amparis

EXPOSE 8000
RUN dos2unix run.sh
CMD bash run.sh
