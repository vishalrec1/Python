from google.cloud import bigquery

def loadBigQueryTableFromGCS(PROJECT_ID,REGION,BUCKET_URI):
	client = bigquery.Client(project=PROJECT_ID,location=REGION)
	job_config = bigquery.LoadJobConfig(
										schema=[
											bigquery.SchemaField("cc_num",        "STRING"),
											bigquery.SchemaField("cust_num",      "STRING"),
											bigquery.SchemaField("credit_limit",  "INTEGER"),
											bigquery.SchemaField("zip_code",      "STRING"),
											bigquery.SchemaField("cash_back_pct", "FLOAT"),
											bigquery.SchemaField("ftr_dttm",      "STRING")
										],
										skip_leading_rows = 1,
										# The source format defaults to CSV, so the line below is optional.
										source_format = bigquery.SourceFormat.CSV,
									)
	uri      = BUCKET_URI+'/cc_data.csv'
	table_id = 'gcp-practice-0123.dataset1.from_gcs'
	load_job = client.load_table_from_uri(source_uris = uri,
										  destination = table_id,
										  job_config  = job_config)  # Make an API request.
	load_job.result()