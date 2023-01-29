import kfp
from kfp.v2 import dsl, compiler
from kfp.v2.dsl import component, pipeline, Output, Artifact, Input, Model

CUSTOM_SERVING_CONTAINER = "us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-0:latest"


@component(base_image=CUSTOM_SERVING_CONTAINER,
           #output_component_file = 'gs://gcp-practice-0123-18jun2023/docker-kfp-test/yaml/batch_prediction.yaml',
           #output_component_file = 'E:\\Python-code\\VertexAI-MLPipelines\\yaml\\batch_prediction.yaml',
           output_component_file='/batch_prediction.yaml',
           packages_to_install=['google-cloud-aiplatform',
                                'protobuf==3.20.3', 'datetime']
           )
def batch_prediction(project_in: str,
                     model_display_name_in: str,
                     model_resource_nm_in: str,
                     bigquery_source_in: str,
                     bigquery_destination_prefix_in: str,
                     predictions_format_in: str,
                     machine_type_in: str
                     ) -> str:
    print("\n\nDoing Batch Prediction...")
    from google.cloud import aiplatform
    from datetime import datetime
    aiplatform.init(project=project_in)
    model_obj = aiplatform.Model(model_resource_nm_in)
    bigquery_source_in = 'bq://'+bigquery_source_in
    bigquery_destination_prefix_in = bigquery_destination_prefix_in + \
        '-'+datetime.now().strftime('%Y%m%d%H%M%S')
    print('******bigquery_source_in : ', bigquery_source_in)
    print('******bigquery_destination_prefix_in : ',
          bigquery_destination_prefix_in)
    batch_predict_job = model_obj.batch_predict(job_display_name=model_display_name_in,
                                                bigquery_source=bigquery_source_in,
                                                bigquery_destination_prefix=bigquery_destination_prefix_in,
                                                predictions_format=predictions_format_in,
                                                machine_type=machine_type_in
                                                )
    bigquery_destination_prefix_in = bigquery_destination_prefix_in[5:]
    return bigquery_destination_prefix_in
