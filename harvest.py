############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)


    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', True, False, 'Crenshaw')
    crenshaw.add_pairing('Proscuitto')
    all_melon_types.append(crenshaw)

    watermelon = MelonType('yw', 2013, 'yellow', True, True, 'Yellow Watermelon')
    watermelon.add_pairing('ice cream')
    all_melon_types.append(watermelon)    


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pair in melon.pairings:
            print(f"- {pair}")

melontypes = make_melon_types()
print_pairing_info(melontypes)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_by_code = {}

    for melon in melon_types:
        melon_by_code[melon.code] = melon.name

    return melon_by_code

print(make_melon_type_lookup(melontypes))


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, harvested_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_field = harvested_field
        self.harvested_by = harvested_by


    def is_sellable(self):
        return (self.shape_rating > 5 and self.color_rating > 5 and 
                self.harvested_field != 3)
     


def make_melons(melon_types):

    """Returns a list of Melon objects."""

    # Fill in the rest
    id = make_melon_type_lookup(melon_types)
    melons = []

    melon1 = Melon(id['yw'], 8, 7,2, 'Sheila')
    melon2 = Melon(id['yw'], 3,4,2, 'Sheila')    
    melon3 = Melon(id['yw'], 9, 8,3, 'Sheila')
    melon4 = Melon(id['cas'], 10, 6,35, 'Sheila')
    melon5 = Melon(id['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(id['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(id['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(id['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(id['yw'], 7, 10, 3, 'Sheila')

    melons.append(melon1)
    melons.append(melon2)
    melons.append(melon3)
    melons.append(melon4)
    melons.append(melon5)
    melons.append(melon6)
    melons.append(melon7)
    melons.append(melon8) 

    return melons



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    # sellable = is_sellable(shape_rating, color_rating, harvested_field)
    for melon in melons:
        is_sellable = melon.is_sellable()
        msg = f"Harvested by {melon.harvested_by} from Field {melon.harvested_field}"
        if is_sellable:
            print(f"{msg} (CAN BE SOLD)")
        else:
            print(f"{msg} (NOT SELLABLE)")
           


melontypes = make_melon_types() # Melon Types from part 1
melons = make_melons(melontypes)
get_sellability_report(melons)