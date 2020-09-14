FROM python:3

#ADD app.py /

RUN pip install flask
RUN pip install matplotlib
RUN pip install pandas
RUN pip install seaborn

COPY . /app
WORKDIR /app
#RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

#CMD [ "python", "./app.py" ]
#ENV FLASK_APP=app.py
#CMD ["flask", "run", "--host", "0.0.0.0" ]