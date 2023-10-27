import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2 - 4 * x + 2


def d(x):
    return 2 * x - 4


def gradient_descent(learning_rate_input, max_iterations_input, tolerance_input):
    # Initialize a starting point
    x = 0.0
    alpha = learning_rate_input

    x_history = [x]
    y_history = [f(x)]

    for iteration in range(max_iterations_input):
        # Calculate the gradient of the function with respect to x
        gradient = d(x)

        current_value = f(x)
        x_history.append(x)
        y_history.append(current_value)

        # Update x using the gradient and learning rate
        x -= alpha * gradient

        # Calculate the new function value
        new_value = f(x)

        # Check if the change in value is smaller than the tolerance
        if abs(current_value - new_value) < tolerance_input:
            print(f"Minimum found at x = {x} (iteration {iteration + 1})")
            break

    else:
        print("Maximum iterations reached. Minimum might not be found.")

    plot(x_history, y_history)


def plot(x_history, y_history):
    x_values = np.linspace(-2, 6, 400)
    y_values = f(x_values)
    plt.plot(x_values, y_values, label='f(x) = x^2 - 4x + 2')
    plt.scatter(x_history, y_history, c='red', label='Gradient Descent Path')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Gradient Descent for f(x) = x^2 - 4x + 2')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    learning_rate = 0.1
    max_iterations = 1000
    tolerance = 1e-6

    gradient_descent(learning_rate, max_iterations, tolerance)
