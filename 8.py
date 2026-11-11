capacity = 50
passengers = 0

for i in range(3):
    boarded = int(input())
    left = int(input())

    passengers = passengers + boarded - left

    if passengers > capacity:
        passengers = capacity

print("Passengers:", passengers)