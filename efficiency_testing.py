import time

# sample code for efficiency testing
# need to do that over the model and his parameters

start_time = time.time()

for i in range(10000):
    print(i*2)

end_time = time.time()

total_time = end_time - start_time

print(f"time taking: {total_time}")