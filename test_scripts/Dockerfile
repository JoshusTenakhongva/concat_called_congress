FROM python:3.9.12-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /usr/src/app/

# Install PsycoPG for Postgres access
# 1. Install sudo. We need it to install PsycoPG
RUN su -
RUN yes | apt-get update -y && apt-get upgrade -y && apt-get install sudo -y && exit

# Now we can install the PsychoPG binaries
RUN sudo apt-get install python3-dev -y
# Install GCC since the binaries need C
RUN sudo apt-get install build-essential -y
# Install libpq-dev
RUN sudo apt-get install libpq-dev -y

# Let's install the binaries in C because that's the recommended way for production.
# Also because I'm running this Image off of a Mac M1 Arm processor which isn't supported for the pure python install
# It's also good practice for when I have to install stuff on my own. Let's get independent!
RUN pip install psycopg[c]


CMD [ "python", "./test.py" ]