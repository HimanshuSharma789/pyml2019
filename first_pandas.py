import pandas as pd
import matplotlib.pyplot as plt
book = pd.read_csv("weather_report.csv")
print(book)
book.plot()

