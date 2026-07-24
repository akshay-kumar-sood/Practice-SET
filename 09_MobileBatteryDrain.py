#Mobile Battery Drain Simulator

import math
drain_per_minute=int(input("Enter drain rate : "))

print(f"Time to full battery drain is : {math.floor(100/drain_per_minute)}")


# floor give lesser ele 
# 1.1 --> 1
# 1.9 --> 1

# ceil give greater ele
# 1.1 --> 2
# 1.9 --> 2
