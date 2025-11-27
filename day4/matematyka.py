import math

print(math.pi)  # 3.141592653589793
print(math.sqrt(25))  # 5.0

print(len(str(math.pi)))  # 17

angle_degree = 30
angle_radians = math.radians(angle_degree)
print(angle_radians)  # 0.5235987755982988
sin_value = math.sin(angle_radians)
print(f"sin({angle_degree}) = {sin_value}")
# sin(30) = 0.49999999999999994