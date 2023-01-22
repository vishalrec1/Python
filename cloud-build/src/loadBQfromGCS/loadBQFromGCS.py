from loadBigQueryTableFromGCS import loadBigQueryTableFromGCS
from writeDataToGCS import writeDataToGCS

#Define few Varaibles

PROJECT_ID = 'gcp-practice-0123'
REGION     = 'us-central1'
BUCKET     = 'gcp-practice-0123-18jun2023'
BUCKET_URI = 'gs://gcp-practice-0123-18jun2023/feature-store-data'

print('*********CREATING DATA AND LOADING TO GCS BUCKET ......**************')
writeDataToGCS(PROJECT_ID,BUCKET)

print('************LOADING DATA TO BIG QUERY FROM GCS BUCKET****************')
loadBigQueryTableFromGCS(PROJECT_ID,REGION,BUCKET_URI)



#########################################################
'''
Dockerfile

FROM python:3
ADD *.py /
RUN pip install google-cloud-bigquery
RUN pip install faker
RUN pip install datetime
RUN pip install google-cloud-storage
CMD ["python","./loadBQFromGCS.py"]


gcloud builds submit --region=us-central1 --tag us-central1-docker.pkg.dev/gcp-practice-0123/gcf-artifacts/load-bq-from-gcs-image:latest

gcloud config set project gcp-practice-0123



'''