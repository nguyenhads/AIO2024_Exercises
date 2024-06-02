# Viết function lựa chọn regression loss function để tính loss
import numpy as np


def calculate_loss(target: float, prediction: float, loss_name: str) -> float:

    loss_name = loss_name.upper()
    if loss_name in ["RMSE", "MSE"]:
        return (target - prediction) ** 2
    elif loss_name == "MAE":
        return np.abs(target - prediction)
    else:
        raise ValueError(
            f"{loss_name} must be one of the following: 'MAE', 'MSE', 'RMSE'"
        )


def calc_regression_loss(num_samples: int, loss_name: str):

    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer number!")

    loss_name = loss_name.upper()
    overall_loss_list = []

    for n in range(num_samples):
        target = np.random.uniform(0.0, 10.0)
        prediction = np.random.uniform(0.0, 10.0)
        loss = calculate_loss(target, prediction, loss_name)
        overall_loss_list.append(loss)

        print(
            f"Loss name: {loss_name}, Sample: {n}, \
            Prediction: {prediction}, Target: {target}, Loss: {loss}"
        )

    if loss_name == "RMSE":
        result = np.sqrt(np.mean(overall_loss_list))
    else:
        result = np.mean(overall_loss_list)

    print(f"Final {loss_name}: {result}")


if __name__ == "__main__":

    num_samples = input(
        "Input number of samples (integer number) which are generated: "
    )
    try:
        num_samples = int(num_samples)
    except ValueError:
        raise ValueError("num_samples must be an integer!")

    loss_name = input("Input loss function name (MAE, MSE, RMSE): ")

    calc_regression_loss(num_samples=num_samples, loss_name=loss_name)
