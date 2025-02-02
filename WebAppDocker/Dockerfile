FROM python:3.11

WORKDIR /src

RUN pip3 install Flask==3.0.3
RUN pip3 install gunicorn==22.0.0

COPY . .

EXPOSE 50505

ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf.py", "WebHost:app"]