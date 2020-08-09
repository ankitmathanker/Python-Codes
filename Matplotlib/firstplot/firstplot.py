from matplotlib import pyplot as plt

#print(plt.style.available)
# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight',
#'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark',
#'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', '
#seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white',
# 'seaborn-whitegrid', 'tableau-colorblind10']

plt.xkcd()
#plt.style.use('fivethirtyeight')

# Median Developer Salaries by Age
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(age_x, dev_y, color = 'k', linestyle = '--', marker = '.', label ='All Developers')

plt.plot(age_x, py_dev_y, color = 'b', marker = 'o', lw = 3, label ='Python Developers')

plt.plot(age_x, js_dev_y, color = 'y', linewidth = 3, label='Java Developers')


plt.title('Developers Salary (USD) with Age')
plt.xlabel('Ages')
plt.ylabel('Salary (USD)')

plt.legend()

plt.grid(True)

#to fit graph properly
plt.tight_layout()
#plt.savefig('format2.png')
plt.show()
