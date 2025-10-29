# SloBENCH evaluation script - dialect COPA

This benchmark uses the COPA (Choice of Plausible Alternatives) datasets to
compare models' performances on standard Slovenian and on a dialect from the
Cerkno dialect group. It is envisioned with LLMs in mind, so it can robustly
work also with out-of-domain labels and measures the percentage of in-domain
labels in the output.

## Output on mock data

```python
{
  "status": "S",
  "metrics": {
    # Results on standard:
    "accuracy_std": 0.5, # Accuracy
    "success_std": 0.75, # Percentage of reasonable responses (0 or 1)
    # Results on dialect:
    "accuracy_cer": 0.75,# Accuracy
    "success_cer": 1.0   # Percentage of reasonable responses
  },
  "evaluation_time": 0.002769,
  "error_report": ""
}
```

This folder also contains a mock reference dataset (ground truth) and submission
.zip files for testing (these obviously won't be included in the public repo).

## Build docker image (from the root directory of this repo):
```
docker buildx build --platform linux/amd64 -t slobench/eval:dialect_copa -f evaluation_scripts/eval_dialect_copa/Dockerfile .
```

## Run mock evaluation (from the root directory of this repo)
```
docker run -it --name eval_dialect_copa --rm \
-v $PWD/evaluation_scripts/eval_dialect_copa/sample_reference.zip:/sample_reference.zip \
-v $PWD/evaluation_scripts/eval_dialect_copa/sample_submission.zip:/sample_submission.zip \
slobench/eval:dialect_copa sample_reference.zip sample_submission.zip
```