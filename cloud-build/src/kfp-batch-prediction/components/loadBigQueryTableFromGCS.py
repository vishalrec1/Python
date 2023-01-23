from google.cloud import bigquery
import kfp
from kfp.v2 import dsl,compiler
from kfp.v2.dsl import component,pipeline,Output,Artifact,Input,Model

CUSTOM_SERVING_CONTAINER  = "us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-0:latest"
@component(base_image            = CUSTOM_SERVING_CONTAINER,
           #output_component_file = 'gs://gcp-practice-0123-18jun2023/docker-kfp-test/yaml/loadBigQueryTableFromGCS.yaml'
           output_component_file = '/loadBigQueryTableFromGCS.yaml'
          )
def loadBigQueryTableFromGCS(PROJECT_ID,REGION,BUCKET_URI):
	client = bigquery.Client(project=PROJECT_ID,location=REGION)
	job_config = bigquery.LoadJobConfig(
										schema=[
											bigquery.SchemaField("longitude",        "FLOAT"),
											bigquery.SchemaField("latitude",      "FLOAT"),
											bigquery.SchemaField("housing_median_age",  "IFLOAT"),
											bigquery.SchemaField("total_rooms",      "FLOAT"),
											bigquery.SchemaField("total_bedrooms", "FLOAT"),
											bigquery.SchemaField("population",      "FLOAT"),
											bigquery.SchemaField("households",      "FLOAT"),
											bigquery.SchemaField("median_income",      "FLOAT"),
											bigquery.SchemaField("median_house_value",      "FLOAT")
										],
										skip_leading_rows = 1,
										# The source format defaults to CSV, so the line below is optional.
										source_format = bigquery.SourceFormat.CSV,
									)
	uri      = BUCKET_URI+'/california_housing_train.csv'
	table_id = 'gcp-practice-0123.dataset2.california_housing_test'
	load_job = client.load_table_from_uri(source_uris = uri,
										  destination = table_id,
										  job_config  = job_config)  # Make an API request.
	load_job.result()
