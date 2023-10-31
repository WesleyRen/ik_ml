import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2 - 4 * x + 2


def d(x):
    return 2 * x - 4


def gradient_descent(x_ini, learning_rate_input, max_iterations_input, lr_strategy='constant'):
    """
    :param x_ini:
    :param learning_rate_input:
    :param max_iterations_input:
    :param tolerance_input:
    :param lr_strategy: learning rate strategy.
    :return:
    """
    # Initialize a starting point
    x = x_ini
    local_alpha = learning_rate_input

    x_hist = [x]
    y_hist = [f(x)]
    new_alpha = local_alpha
    t = 0

    for i in range(max_iterations_input):
        # Calculate the gradient of the function with respect to x
        gradient = d(x)
        if lr_strategy == 'constant':
            new_alpha = local_alpha
        elif lr_strategy == 'invscaling':
            t += 1
            new_alpha = local_alpha / np.sqrt(t)
        elif lr_strategy == 'adaptive':
            # Check the sign of the gradient to determine overshooting
            if i > 0 and np.sign(y_hist[-1] - y_hist[-2]) != np.sign(gradient):
                new_alpha /= 5
        x = x - new_alpha * gradient
        x_hist.append(x)
        y_hist.append(f(x_hist[-1]))
    return x_hist, y_hist


def plot(x_hist, y_hist):
    x_values = np.linspace(-2, 6, 400)
    y_values = f(x_values)
    plt.plot(x_values, y_values, label='f(x) = x^2 - 4x + 2')
    plt.scatter(x_hist, y_hist, c='red', label='Gradient Descent Path')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Gradient Descent for f(x) = x^2 - 4x + 2')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    learning_rate = 0.25
    max_iterations = 1000
    tolerance = 1e-6

    alpha_values = [0.01, 0.1, 1.0]
    init_values = [-5.0, -3.0, -1.0, 1.0, 3.0]
    num_iters = 50
    strategy = ['constant', 'invscaling', 'adaptive']

    for s in strategy:
        fig, axs = plt.subplots(len(alpha_values), len(init_values), figsize=(15, 12))
        for i, alpha in enumerate(alpha_values):
            for j, x_init in enumerate(init_values):
                x_history, y_history = gradient_descent(x_init, alpha, num_iters, s)
                axs[i, j].plot(x_history, y_history, 'o-', color='red')
                axs[i, j].set_title(f's={s}, a={alpha}, x0={x_init}')
                axs[i, j].set_xlabel('x')
                axs[i, j].set_ylabel('f(x)')

        plt.tight_layout()
        plt.show()
