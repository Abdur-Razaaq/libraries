from datetime import *
dt = datetime(2021, 5, 18)
for x in range(10):
    answer = dt + timedelta(days=7)
    print(answer)
    dt=answer
