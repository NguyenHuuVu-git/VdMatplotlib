import matplotlib.pyplot as plt
import numpy as np
divisions=["Div-A", "Div-B", "div-C", "Div-D", "Div-E"]
division_average_marks = [70, 82, 73, 65, 68]
variance = [5,8,7,6,4]
plt.barh(divisions, division_average_marks, xerr=variance, color='green')
plt.title("Bar Graph")
plt.ylabel("Divisions")
plt.xlabel("Marks")
plt.show()