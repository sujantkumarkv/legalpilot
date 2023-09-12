from huggingface_hub import HfApi
api = HfApi()
api.upload_file(
    path_or_fileobj="ilc_embeddings.pkl",
    path_in_repo="ilc_embeddings.pkl",
    repo_id="sujantkumarkv/embeddings",
    repo_type="dataset",
)