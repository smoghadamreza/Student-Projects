class Flower:
    color = 'unknown'


rose = Flower()
rose.color = "red"

violet = Flower()
rose.color = "blue"

this_pun_is_for_you = Flower()

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes and seconds."""
    return hours * 3600 + minutes * 60 + seconds
