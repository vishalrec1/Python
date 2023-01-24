FROM python:3
ADD *.py ./
COPY requirements.txt ./
RUN pip install -r ./requirements.txt
CMD ["python","./compile-pipeline.py"]
CMD ["ls","-ltr","./"]
FROM gcr.io/cloud-builders/gsutil
CMD ["gsutil","cp","/mlopsdeploypipeline-1.json","gs://gcp-practice-0123-18jun2023/docker-kfp-test/kfp-json/mlopsdeploypipeline-1.json"]
