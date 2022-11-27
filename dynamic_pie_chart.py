import random
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
labels=['a','b']
for i in range(10):    
    nums=[random.randint(5,10),random.randint(5,10)]
    ax1.clear()
    ax1.pie(nums, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.pause(2)
plt.draw()


