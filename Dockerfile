FROM python:3

ENV PYTHONIOENCODING UTF-8
ENV TZ=Asia/Bishkek

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir static && mkdir media
COPY . .

RUN python3 manage.py collectstatic --noinput

RUN pip install gunicorn

EXPOSE 8000

CMD ["sh", "-c", "gunicorn your_app_module.wsgi:application --bind 0.0.0.0:8000"]