import kfp
from kfp.v2 import dsl, compiler
from kfp.v2.dsl import component, pipeline, Output, Artifact, Input, Model
from make_pipeline import mlopsDeployPipeline

def compile_pipeline():
    compiler.Compiler().compile(pipeline_func=mlopsDeployPipeline,
                                package_path='cloud-build/src/kfp-batch-prediction/components-3/mlopsdeploypipeline-1-31jan2023.yaml'
                                )
