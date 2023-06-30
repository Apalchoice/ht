class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
            raise NotImplementedError("child classes must implement this")
class dog(animal):
    def speak(self):
        return "woof"

class cow(animal):
        def speak(sslf):
            return "moos"
class cat(animal):
    def speak(self):
        return "meow"

dog = dog("bosco")
print(dog.name)
print(dog.speak())

cat = cat("maxy")
print(cat.name)
print(cat.speak())

cow = cow("brian")
print(cow.name)
print(cow.speak())
