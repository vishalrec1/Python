from kfp.registry import RegistryClient

client = RegistryClient(host=f"https://us-central1-kfp.pkg.dev/gcp-practice-0123/kfp-repo1")
templateName, versionName = client.upload_pipeline(
                                                   file_name="cloud-build/src/kfp-batch-prediction/components-3/mlopsdeploypipeline-1-31jan2023.yaml",
                                                   tags=["v1", "latest"],
                                                   extra_headers={"description":"This is an example for Batch Prediction Pipeline template."}
                                                  )
