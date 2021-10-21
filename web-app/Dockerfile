FROM python:3.9.1
ADD . /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt
RUN chmod +x run_db_check.sh && ./run_db_check.sh
CMD [ "python", "./salubreata.py" ]
