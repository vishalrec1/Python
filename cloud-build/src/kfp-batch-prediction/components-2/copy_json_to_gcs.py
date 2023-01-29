from google.cloud import aiplatform, storage
from compile_pipeline import compile_pipeline

PROJECT_ID = 'gcp-practice-0123'
REGION = 'us-central1'
MACHINE_TYPE = 'e2-standard-4'
BUCKET = 'gcp-practice-0123-18jun2023'

compile_pipeline()
storage_client = storage.Client(project=PROJECT_ID)
bucket = storage_client.bucket(bucket_name=BUCKET)
blob = bucket.blob(
    blob_name='docker-kfp-test/kfp-json/mlopsdeploypipeline-1-28jan2023.json')
# blob.upload_from_filename(filename='/mlopsdeploypipeline-1-28jan2023.json')
DOCKER_LOCAL_PATH = '/mlopsdeploypipeline-1-28jan2023.json'
blob.upload_from_filename(
    filename=DOCKER_LOCAL_PATH)
