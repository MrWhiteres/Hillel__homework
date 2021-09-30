FROM python:3.9.7

RUN mkdir "flask" /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "flask_app.py"]