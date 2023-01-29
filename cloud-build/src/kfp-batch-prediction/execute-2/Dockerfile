FROM python:3
ADD *.py /
COPY requirements.txt /
RUN pip install -r requirements.txt
CMD ["python","./execute_pipeline.py"]
