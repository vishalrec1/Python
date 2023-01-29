import kfp
from kfp.v2 import dsl,compiler
from kfp.v2.dsl import component,pipeline,Output,Artifact,Input,Model
from make_pipeline import mlopsDeployPipeline

#from make_pipeline import mlopsDeployPipeline
#JSON_LOCAL_PATH = "E:\\Python-code\\VertexAI-MLPipelines\\json\\mlopsdeploypipeline-1.json"
#JSON_GCS_PATH   = 'gs://gcp-practice-0123-18jun2023/docker-kfp-test/kfp-json/mlopsdeploypipeline-1.json'

def compile_pipeline():
    DOCKER_LOCAL_PATH = '/mlopsdeploypipeline-1-28jan2023.json'
    compiler.Compiler().compile(pipeline_func = mlopsDeployPipeline,
                                #package_path  = 'gs://gcp-practice-0123-18jun2023/docker-kfp-test/kfp-json/mlopsdeploypipeline-1.json'
                                package_path  = DOCKER_LOCAL_PATH
                               )