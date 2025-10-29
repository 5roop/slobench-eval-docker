import json
from sklearn.metrics import accuracy_score
from pathlib import Path


def preprocess_y_pred(y_pred):
    """Replaces invalid predictions with 42."""
    y_pred_new = []
    for i in y_pred:
        try:
            i_int = int(i)
            if i_int not in [0, 1]:
                raise ValueError("COPA answers can only be 0 or 1")
        except:
            i_int = 42
        y_pred_new.append(i_int)
    return y_pred_new


def evaluate(reference_dataset_path, data_submission_path):
    # Open reference dataset file
    try:
        with open(
            "./" + reference_dataset_path + "/copa-sl_reference.jsonl"
        ) as json_file:
            reference_standard = json.load(json_file)
        with open(
            "./" + reference_dataset_path + "/copa-sl-cer_reference.jsonl"
        ) as json_file:
            reference_cerkno = json.load(json_file)
    except Exception as e:
        raise Exception(f"Exception in opening reference dataset file: {e}")

    # Open Submission File
    try:
        with open("./" + data_submission_path + "/copa-sl_response.jsonl") as json_file:
            submission_standard = json.load(json_file)
            if not submission_standard:
                raise Exception(
                    f"Submission file is empty or contains the wrong filename."
                )
        with open(
            "./" + data_submission_path + "/copa-sl-cer_response.jsonl"
        ) as json_file:
            submission_cerkno = json.load(json_file)
            if not submission_cerkno:
                raise Exception(
                    f"Submission file is empty or contains the wrong filename."
                )

    except Exception as e:
        raise Exception(f"Exception in opening submission file: {e}")

    # Calculate metrics
    try:
        y_true_std = reference_standard["response"]
        y_pred_std = submission_standard["response"]
        assert len(y_true_std) == len(y_pred_std), (
            f"Length mismatch in copa-sl_response: expected {len(y_true_std)} items, submission contained {len(y_pred_std)}."
        )
        acc_std = accuracy_score(y_true_std, preprocess_y_pred(y_pred_std))
        success_rate_std = len([i for i in y_pred_std if i in [0, 1]]) / len(y_pred_std)

        y_true_cer = reference_cerkno["response"]
        y_pred_cer = submission_cerkno["response"]
        assert len(y_true_cer) == len(y_pred_cer), (
            f"Length mismatch in copa-sl-cer_response: expected {len(y_true_cer)} items, submission contained {len(y_pred_cer)}."
        )
        acc_cer = accuracy_score(y_true_cer, preprocess_y_pred(y_pred_cer))
        success_rate_cer = len([i for i in y_pred_cer if i in [0, 1]]) / len(y_pred_cer)

        metrics = {
            "accuracy_std": acc_std,
            "success_std": success_rate_std,
            "accuracy_cer": acc_cer,
            "success_cer": success_rate_cer,
        }
        return metrics
    except Exception as e:
        raise Exception(f"Exception in metric calculation: {e}")
