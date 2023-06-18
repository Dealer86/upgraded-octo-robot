# Liskov substituion principle - A child class should perform exactly like its super class.
# It should take the same data types as arguments and return the same data types,
# and use all super classes methods


class KitchenAppliance:
    def on(self):
        pass

    def off(self):
        pass

    def set_temp(self):
        pass


class Toaster(KitchenAppliance):
    def on(self):
        # some code to turn it on
        pass

    def off(self):
        # some code to turn it off
        pass

    def set_temp(self):
        # some code to set the temperature
        pass


class Juicer(KitchenAppliance):
    def on(self):
        pass

    def off(self):
        pass

    # def set_temp(self) - here the Juicer class breaks liskov_subtitution principle because
    # the juicer does not have such a method, it doesn't know how to set temperature

# ---------------------------------------------- Correct way -----------------------------------------


class KitchenAppliance1:
    def on(self):
        pass
    def off(self):
        pass


class KitchenApplianceWithTemp(KitchenAppliance1):
    def set_temp(self):
        pass


class Toaster1(KitchenApplianceWithTemp):
    def on(self):
        pass
    def off(self):
        pass
    def set_temp(self):
        pass


class Juicer1(KitchenAppliance1):
    def on(self):
        pass

    def off(self):
        pass

    # So the juicer1 class does not break liskov substitution principle because it uses all the methods

    