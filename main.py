def KmhToMs(kmh):
    return kmh / 3.6


weight = float(input("Vehicule weight (kg): "))
topSpeed = KmhToMs(float(input("Top speed (km/h): ")))
topSpeedTime = float(input("Amount of time to get to top speed (seconds): "))
wheelsRadius = float(input("Wheels radius (meters): "))

a = topSpeed / topSpeedTime
f = weight * a
w = topSpeed / wheelsRadius
rpm = w * (60 / (2 * 3.14159))
t = f * wheelsRadius
p = t * w

print(
    f'You need a motor with a power of: {round(p, 2)} watts. It will have a torque of {round(t, 2)}Nm and {round(rpm, 2)} rotations per minutes (RPM)')
