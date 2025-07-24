class vehicle:
    # constructor
    def __init__(self, mileage, max_speed):
        self.mileage = mileage
        self.max_speed = max_speed

obj = vehicle(18, 240)
print("The maximum speed is", obj.max_speed)
print("The mileage is", obj.mileage)
