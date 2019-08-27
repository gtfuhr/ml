from matplotlib import pyplot as plt
from collections import Counter
grades = [93,94,91,87,70,0,85,80,100,67,73,77,0]
decile = lambda grade : grade // 10 *10

histogram = Counter(decile(grade) for grade in grades)

plt.bar([x-4 for x in histogram.keys()],histogram.values(),8)

plt.axis([-5,105,0,5])

plt.xticks([10*i for i in range(11)])
plt.xlabel("Decil")
plt.ylabel("Distribuicao de notas do teste 1")
plt.show()

