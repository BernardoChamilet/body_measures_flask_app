FROM python:3

WORKDIR /usr/src/body_measures_app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["python",  "app.py"]