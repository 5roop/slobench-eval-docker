FROM python:3.11-slim

# Install system dependencies required by praat-parselmouth (build from source on linux-aarch64)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY evaluation_scripts/eval_speech_diarisation/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Copy the evaluation scripts
COPY evaluation_scripts/eval_speech_diarisation/evaluate.py ./evaluate.py
COPY run.py ./run.py

ENTRYPOINT ["python", "run.py"]

