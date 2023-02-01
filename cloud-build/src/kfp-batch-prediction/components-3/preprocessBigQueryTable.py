import kfp
from kfp.v2 import dsl, compiler
from kfp.v2.dsl import component, pipeline, Output, Artifact, Input, Model

CUSTOM_SERVING_CONTAINER = "us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-0:latest"


@component(base_image=CUSTOM_SERVING_CONTAINER,
           #output_component_file = 'gs://gcp-practice-0123-18jun2023/docker-kfp-test/yaml/preprocessBigQueryTable.yaml',
           #output_component_file = 'E:\\Python-code\\VertexAI-MLPipelines\\kfp-components-2\\yaml\\preprocessBigQueryTable.yaml',
           output_component_file='/preprocessBigQueryTable.yaml',
           packages_to_install=['google-cloud-aiplatform',
                                'google-cloud-bigquery', 'protobuf==3.20.3', 'datetime']
           )
def preprocessBigQueryTable(project_in: str,
                            source_bq_table_id_in: str,) -> str:
    from google.cloud import bigquery
    from datetime import datetime
    client = bigquery.Client(project=project_in, location='us-central1')
    target_table_id = 'gcp-practice-0123.dataset2.california_housing_test_2_' + \
        datetime.now().strftime('%Y%m%d%H%M%S')
    query_str = "CREATE TABLE "+target_table_id + \
        " AS SELECT longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income FROM "+source_bq_table_id_in
    print('*******Query is : ', query_str)
    bigquery_query_job = client.query(query=query_str)
    print('*******The state of the job is : ', bigquery_query_job.state)
    return target_table_id
