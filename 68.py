class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm

    def add(self, other_distance):
        total_km = self.km + other_distance.km
        total_m = self.m + other_distance.m
        total_cm = self.cm + other_distance.cm

        if total_cm >= 100:
            total_m += total_cm // 100
            total_cm %= 100

        if total_m >= 1000:
            total_km += total_m // 1000
            total_m %= 1000

        return Distance(total_km, total_m, total_cm)

    def display(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"


# Input the first distance
km1 = int(input("Enter kilometers for distance 1: "))
m1 = int(input("Enter meters for distance 1: "))
cm1 = int(input("Enter centimeters for distance 1: "))

# Input the second distance
km2 = int(input("Enter kilometers for distance 2: "))
m2 = int(input("Enter meters for distance 2: "))
cm2 = int(input("Enter centimeters for distance 2: "))

# Create Distance objects
distance1 = Distance(km1, m1, cm1)
distance2 = Distance(km2, m2, cm2)

# Add distances and display the result
result_distance = distance1.add(distance2)
print(f"Sum of distances: {result_distance.display()}")
