"""Solution to Ellen's Alien Game exercise."""

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    health = 3
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate ):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1

    def hit(self):
        if self.health > 0:
            self.health -= 1           

    def is_alive(self):
        return self.health > 0

    def teleport(self,new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self,other_object):
        """Obviously, if the aliens can be hit by something, then they need to be able to detect when such a collision has occurred.
         However, collision detection algorithms can be tricky, and you do not yet know how to implement one. 
         Ellen has said that she will do it later, but she would still like the collision_detection method to appear in the class as 
         a reminder to build out the functionality. It will need to take a variable of some kind (probably another object), but that's 
         really all you know. You will need to make sure that putting the method definition into the class doesn't cause any errors when 
         called:
         """
        pass

def new_aliens_collection(position):
    aliens = []
    for coordinate in position:
        x_coordinate,y_coordinate = coordinate
        aliens.append(Alien(x_coordinate,y_coordinate))
    return aliens
