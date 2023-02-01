from kfp.registry import RegistryClient

client = RegistryClient(host=f"https://us-central1-kfp.pkg.dev/gcp-practice-0123/py-gar-repo-test")
templateName, versionName = client.upload_pipeline(
                                                   file_name="mlopsdeploypipeline-1-31jan2023.yaml",
                                                   tags=["v1", "latest"],
                                                   extra_headers={"description":"This is an example for Batch Prediction Pipeline template."}
                                                  )
