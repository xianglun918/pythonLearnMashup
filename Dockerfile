FROM python:3.8
WORKDIR /app
COPY . .
RUN pip3 install -r requirement.txt
CMD ["python", "app.py"]
