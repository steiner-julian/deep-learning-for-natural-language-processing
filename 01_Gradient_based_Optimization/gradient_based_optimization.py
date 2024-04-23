def gradient_optimization(
    function,
    derivative,
    learning_rate=0.05,
    epochs=10
):
    x_values = []

    for _ in epochs:
        u = derivative(x_i)
        x_i = x_i - learning_rate * u
        x_values.append(x_i)
    
    return x_i, x_values
