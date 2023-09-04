from huggingface_hub import HfApi
api = HfApi()
api.upload_file(
    path_or_fileobj="indian_legal_corpus.jsonl",
    path_in_repo="indian_legal_corpus.jsonl",
    repo_id="sujantkumarkv/indian_legal_corpus",
    repo_type="dataset",
)