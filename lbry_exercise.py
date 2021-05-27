from datetime import *
dt = datetime.now()
for x in range(10):
    answer = dt + timedelta(days=7)
    print(answer)
    dt = answer
