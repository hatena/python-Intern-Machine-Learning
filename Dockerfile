FROM python:3.7

ENV LC_ALL C.UTF-8

WORKDIR /app

RUN apt-get update -yqq && apt-get install -yq --no-install-recommends \
      fonts-ipafont-gothic \
 && apt-get clean \
 && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt && rm -rf /root/.cache/pip/
COPY . /app

CMD jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
