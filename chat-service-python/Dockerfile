FROM python:3.11

EXPOSE  8085
RUN apt-get update && apt-get install -y git && apt-get clean
WORKDIR /app
COPY ./chat-service-python /app

RUN git clone https://github.com/lmolkova/opentelemetry-python-contrib opentelemetry-python-contrib

WORKDIR /app/opentelemetry-python-contrib
RUN git checkout openai-events
RUN pip install /app/opentelemetry-python-contrib/instrumentation/opentelemetry-instrumentation-openai

WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8085"]