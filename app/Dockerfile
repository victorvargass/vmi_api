FROM python:3.8
RUN mkdir /app
COPY . /app/

RUN pip --no-cache-dir install -r /app/requirements.txt

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]