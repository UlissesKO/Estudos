class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))


x = range(11)

y = MyList(x)
print(y)
y.remove_min()
print(y)
y.remove_max()
print(y)

#estudar mais sobre