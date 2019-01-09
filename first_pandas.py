import pandas as pd
import matplotlib.pyplot as plt
book = pd.read_csv("weather_report.csv")
print(book)
plt.plot(book['date'], book['min'], color='r')
plt.plot(book['date'], book['max'], color='b')
plt.legend()
plt.show()
