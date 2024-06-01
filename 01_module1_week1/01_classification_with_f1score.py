# Viết function thực hiện đánh giá classification model bằng F1-Score.


def calculate_classification_metrics(tp: int, fp: int, fn: int):
    metrics_name = ["tp", "fp", "fn"]
    for idx, x in enumerate([tp, fp, fn]):
        if not isinstance(x, int):
            print(f"{metrics_name[idx]} must be an integer")
            return
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp, fp, and fn must be greater than zero")
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1_score:.2f}")


if __name__ == "__main__":
    tp = 2
    fp = 3
    fn = 4
    calculate_classification_metrics(tp, fp, fn)
