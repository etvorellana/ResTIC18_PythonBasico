import math  # Importando das biblioteca padrão de módulos do Python

def cart2pol(x, y):
    rho = (x**2 + y**2)**0.5
    theta = math.atan2(y, x)
    return rho, theta
    
def pol2cart(rho, theta):
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return x, y


