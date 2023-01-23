import kfp
from kfp.v2 import dsl,compiler
from kfp.v2.dsl import component,pipeline,Output,Artifact,Input,Model

CUSTOM_SERVING_CONTAINER  = "us-central1-docker.pkg.dev/nonprod-corp-1cdh-214e/containers/wf_1cdh_notebook:r6"

@component(base_image            = CUSTOM_SERVING_CONTAINER,
           output_component_file = 'gs://gcp-practice-0123-18jun2023/docker-kfp-test/yaml/create_endpoint.yaml'
           #output_component_file = '/home/jupyter/KFP-json2/yaml/create_endpoint.yaml'
          )
def create_endpoint(endpoint_display_name_in:str, 
                     project_in:str
                   ) -> str:
    print("\n\n***Creating Endpoint....")
    from google.cloud import aiplatform
    aiplatform.init(project=project_in)
    endpoint = aiplatform.Endpoint.create(project      = project_in,
                                          display_name = endpoint_display_name_in
                                         )
    print("***The End Point Project is : ",endpoint.project)
    print("***The Private End point resource name is : ",endpoint.resource_name)
    #vertex_endpoint.uri = endpoint.resource_name
    return endpoint.resource_name