class Vector3D:
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
v = Vector3D(1, 2, 3)
try:
    print(v.__dict__)
except:
    print("Нет dict")
try:
    v.color = "red"
except:
    print("Нельзя добавить color")