import math


class Node(object):
    a = 6378137.0
    b = 6356752.3142
    e = math.sqrt(1-(b/a)*(b/a))

    def __init__(self, node_id, lat, lon):
        lat = float(lat)
        lon = float(lon)
        self.ndID = int(node_id)
        self.X = Node.a*lon
        tan = math.tan(math.pi/4 + lat/2)
        pow = math.pow((1-Node.e * math.sin(lat))/(1+Node.e * math.sin(lat)), Node.e/2)
        in_log = tan*pow
        self.Y = Node.a * math.log(in_log, math.e)

    def set_id(self, id):
        self.id = id

    def __eq__(self, other):
        return self.ndID == other.ndID


