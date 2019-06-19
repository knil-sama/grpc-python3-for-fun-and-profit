FROM python:3.6
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

