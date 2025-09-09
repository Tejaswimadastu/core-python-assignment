# Function to calculate fare for a given distance
def calculate_fare(distance):
    base_fare = 50   
    per_km = 10      
    return base_fare + (distance * per_km)  
trips = []
n = int(input("Enter number of trips: "))
# Take distance input for each trip
for i in range(n):
    dist = int(input(f"Enter distance (in km) for Trip {i+1}: "))
    trips.append(dist) 
total = 0
# Calculate fare for each trip
for i, dist in enumerate(trips, start=1):
    fare = calculate_fare(dist)  
    print(f"Trip {i}: ${fare}")  
    total += fare  
print("Total Fare:", f"${total}")
