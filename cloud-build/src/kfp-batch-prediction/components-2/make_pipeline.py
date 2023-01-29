import kfp
from kfp.v2 import dsl, compiler
from kfp.v2.dsl import component, pipeline, Output, Artifact, Input, Model

#pipeline_root_path          = 'gs://gcp-practice-0123-18jun2023/docker-kfp-test/kfp-json/'
#pipeline_root_path = "E:\\Python-code\\VertexAI-MLPipelines\\kfp-components-2\\json\\"
pipeline_root_path = "/"


@dsl.pipeline(name="mlopsdeploypipeline-1-28jan2023",
              pipeline_root=pipeline_root_path
              )
def mlopsDeployPipeline(project_in: str,
                        endpoint_display_name_in: str,
                        model_gcs_path_in: str,
                        serving_container_in: str,
                        # bigquery_source_in:str,
                        bigquery_destination_prefix_in: str,
                        predictions_format_in: str,
                        machine_type_in: str,
                        bucket_uri_in: str,
                        score_target_bucket_uri_in: str
                        ):
    from create_endpoint import create_endpoint
    from register_model import register_model
    from deploy_model import deploy_model
    from batch_prediction import batch_prediction
    from loadBigQueryTableFromGCS import loadBigQueryTableFromGCS
    from preprocessBigQueryTable import preprocessBigQueryTable
    from loadScoresFromBigQueryTableToGCS import loadScoresFromBigQueryTableToGCS
    # CREATE ENDPOINT
    endpoint_op = create_endpoint(endpoint_display_name_in,
                                  project_in
                                  )
    # REGISTER MODEL TO MODEL REGISTRY
    model_op = register_model(project_in,
                              endpoint_display_name_in,
                              model_gcs_path_in,
                              serving_container_in
                              )
    # DEPLOY MODEL TO ENDPOINT
    deploy_model(project_in,
                 endpoint_display_name_in,
                 model_op.output,
                 endpoint_op.output
                 )
    # LOAD SOCRING DATA FROM GCS csv FILE TO BIGQUERY
    bq_table_id = loadBigQueryTableFromGCS(project_in,
                                           bucket_uri_in
                                           )
    # PRE-PROCESS THE BIGQUERY DATA TO REDUCE THE # OF COLUMNS FROM 9 TO 8
    scoring_data_bq_tbl = preprocessBigQueryTable(
        project_in, bq_table_id.output)
    # PERFORM BATCH PREDICTION
    score_bq_tbl = batch_prediction(project_in,
                                    endpoint_display_name_in,
                                    model_op.output,
                                    scoring_data_bq_tbl.output,
                                    bigquery_destination_prefix_in,
                                    predictions_format_in,
                                    machine_type_in
                                    )
    # LOAD SCORES BACK TO GCS BUCKET IN csv FORMAT
    loadScoresFromBigQueryTableToGCS(project_in,
                                     score_bq_tbl.output,
                                     score_target_bucket_uri_in
                                     )
