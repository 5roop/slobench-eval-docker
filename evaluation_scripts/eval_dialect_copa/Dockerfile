FROM python:3.14.0-bookworm


COPY evaluation_scripts/eval_dialect_copa/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY evaluation_scripts/eval_dialect_copa/evaluate.py ./evaluate.py
COPY run.py ./run.py

ENTRYPOINT ["python", "run.py"]