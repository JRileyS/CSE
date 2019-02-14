import Special_Random

class Phone(object):
    def __init__(self, carrier, charge_left=50):
        # These are attributes that the object has.
        # These should all be relevant to the program.
        self.screen = True
        self.camera = 2
        self.microphone = True
        self.carrier = carrier
        self.battery_left = charge_left

    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

    def make_call(self, duration):
        if not self.screen:
            print("You can't make a phone call.")
            print("Your screen is broken.")
            return
        battery_loss_per_minute = 5
        if self.battery_left <= 0:
            print("You can't. Your phone's dead.")
            return
        self.battery_left -= duration * battery_loss_per_minute
        if self.battery_left < 0:
            self.battery_left = 0
            print("Your phone dies during the conversation.")
        elif self.battery_left == 0:
            print ("Your phone dies at the end of the conversation.")
        else:
            print("You successfully make the phone call.")
            print("Your phone is at %s percent charge." % self.battery_left)

    def smash_phone(self):
        print("SMAAAASH!!")
        print("The phone's screen broke.")
        self.screen = False


my_phone = Phone("ATT", 100)
your_phone = Phone("Bell", 0)
default_phone = Phone("Verizon")

my_phone.make_call(60)
my_phone.make_call(10)
my_phone.charge(100)
my_phone.make_call(10)
your_phone.smash_phone()
your_phone.make_call(1)

print(Special_Random.RandomWiebe.myrandom())


class Steak(object):
    def __init__(self, freshness, number, exists):
        self.exists = True
        self.freshness = freshness
        self.number = number

    def freshen(self, freshness):
        freshness += 1
        if freshness > 10:
            freshness = 10

    def feed(self, Dog.happy):
        number -= 1
        Dog.happy = True
        if Dog.angry = True:
            Dog.angry = False

class Dog(object):
    def __init__(self):
        self.angry = True
        self.happy = False

    def bite(self):
        if self.happy == True:
            print("The dog did not bite you. You're glad it doesn't.")
        elif self.angry == True:
            print("The dog bit you angrily! Ouch! That seemed like a critical hit.")
        else:
            print("The dog nipped on you! You're glad the dog didn't use its full power.")

    def feed(self, number):
        if Steak.exists = True:
            number -= 1
            if self.angry = True:
                self.angry = False
            self.happy = True
            print("The dog became happy!")