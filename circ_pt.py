import numpy as np

def circle(point,center,radius):
    c_x, c_y = center
    
    x,y = point[0] - c_x, point[0] - c_y
    
    if np.linalg.norm([x,y]) > radius:
        print("Outside of the circle")
    elif np.linalg.norm([x,y]) == radius:
        print("On the circle")
    else:
        print("Inside of the circle")
        
def get():
    point = [float(input("x coordinate of point: ")), float(input("y coordinate of point: "))]
    center = [float(input("x coordinate of your center of circle: ")), float(input("y coordinate of your center of circle: "))]
    radius = float(input("radius of your circle: "))
    circle(point, center, radius)

if __name__ == "__main__":
    get()