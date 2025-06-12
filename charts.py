
import matplotlib.pyplot as plt
import pandas as pd

def generate_chart_image():
    data = pd.DataFrame({
        'час': range(10),
        'температура': [41, 42, 43, 45, 44, 46, 47, 43, 42, 41]
    })
    plt.plot(data['час'], data['температура'], marker='o')
    plt.title("Температура за зміну")
    plt.xlabel("Години")
    plt.ylabel("Температура (°C)")
    plt.grid()
    path = "chart.png"
    plt.savefig(path)
    return path
