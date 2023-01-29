import kfp
from kfp.v2 import dsl,compiler
from kfp.v2.dsl import component,pipeline,Output,Artifact,Input,Model

CUSTOM_SERVING_CONTAINER  = "us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-0:latest"
@component(base_image            = CUSTOM_SERVING_CONTAINER,
           #output_component_file = 'gs://gcp-practice-0123-18jun2023/docker-kfp-test/yaml/loadScoresFromBigQueryTableToGCS.yaml'
           output_component_file = '/loadScoresFromBigQueryTableToGCS.yaml',
           packages_to_install   = ['google-cloud-aiplatform','google-cloud-bigquery','protobuf==3.20.3']
          )
def loadScoresFromBigQueryTableToGCS(project_in:str,
                                     source_bq_table_id_in:str,
                                     target_bucket_uri_in:str)-> str:
    from google.cloud import bigquery
    client      = bigquery.Client(project=project_in,location='us-central1')
    #dataset_ref = bigquery.DatasetReference(project_in, dataset_id_in)
    #table_ref   = dataset_ref.table(source_bq_table_id_in)
    extract_job = client.extract_table(source           = source_bq_table_id_in,
                                       destination_uris = target_bucket_uri_in
                                      )
    extract_job.result()