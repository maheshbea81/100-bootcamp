# run as is then change j to 12
# use the debugger to show the i counter increasing
i = 1
j = 120
while i < 42:
    i = i * 2
    if i > j:
        break
else:
    print("Loop expired: ", i)

print("Final value: ", i)
