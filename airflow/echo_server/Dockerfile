FROM registry.access.redhat.com/ubi8/python-38
ADD . /app
WORKDIR /app
USER root
RUN pip install -r requirements.txt
USER 1001
# Run the application
ENV FLASK_ENV=development 
ENV FLASK_APP=handler.py
CMD flask run --host=0.0.0.0 --port=8080
