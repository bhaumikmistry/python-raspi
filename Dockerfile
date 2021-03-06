# base-image for python on any machine using a template variable,
# see more about dockerfile templates here:http://docs.resin.io/pages/deployment/docker-templates
FROM resin/%%RESIN_MACHINE_NAME%%-python

# use apt-get if you need to install dependencies,
# for instance if you need ALSA sound utils, just uncomment the lines below.
# RUN apt-get update && apt-get install -yq \
#    alsa-utils libasound2-dev && \
#    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set our working directory
WORKDIR /usr/src/app

# Copy requirements.txt first for better cache on later pushes
COPY ./requirements.txt /requirements.txt

# pip install python deps from requirements.txt on the resin.io build server
RUN pip install -r /requirements.txt

# Let's install our dependencies
RUN apt-get update && apt-get install \
    unzip

RUN wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tar.xz
RUN tar -xf Python-3.5.0.tar.xz
WORKDIR /tmp/Python-3.5.0
RUN ./configure
RUN make
RUN make install    
WORKDIR /usr/src/app


# build RTIMU
RUN wget https://github.com/RPi-Distro/RTIMULib/archive/b949681af69b45f0f7f4bb53b6770037b5b02178.zip
RUN unzip b949681af69b45f0f7f4bb53b6770037b5b02178.zip
WORKDIR /usr/src/app/RTIMULib-b949681af69b45f0f7f4bb53b6770037b5b02178/Linux/python
RUN python setup.py build
RUN python setup.py install

WORKDIR /usr/src/app



# This will copy all files in our root to the working  directory in the container
COPY . ./

# switch on systemd init system in container
ENV INITSYSTEM on

# main.py will run when container starts up on the device
CMD ["python","src/main.py"]
