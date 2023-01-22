FROM python:3
ADD *.py /
COPY requirements.txt /
RUN pip install requirements.txt
CMD ["python","./loadBQFromGCS.py"]
