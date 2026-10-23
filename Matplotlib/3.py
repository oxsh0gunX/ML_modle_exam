# Draw a Line Graph Using Data from a Text File 📈



# import matplotlib.pyplot as plt

# with open('values.txt') as f:
#     data=f.read()

# data=data.split('\n')

# x=[int (row.split(' ')[0]) for row in data]
# y=[int (row.split(' ')[1]) for row in data]
# plt.plot(
#     x,y,
#     c='g',
#     marker='s',
#     mec='g',
#     mfc='g',
#     linestyle='dotted'
# )
# plt.title("testing")
# plt.ylabel("hi")
# plt.show()



# Draw a Line Graph Using Data from a Text File 📈

import matplotlib.pyplot as pll
with open('values.txt') as f:
    file=f.read()

file=file.split('\n')
x=[int(row.split(' ')[0]) for row in file ]
y=[int(row.split(' ')[1]) for row in file ]

pll.plot(
    x,y,
    c='g',
    marker='s',
    linestyle='dotted',
    mfc='g',
    mec='g',

)
pll.show()
