# ice cream stand 
class IceCreamStand:
    def __init__(self, flavors):
        self.flavors = flavors

    def display_flavors(self):
        print("The ice cream stand offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
# Example usage
stand = IceCreamStand(['vanilla', 'chocolate', 'strawberry'])
stand.display_flavors()