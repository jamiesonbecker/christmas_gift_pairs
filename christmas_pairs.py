#! /usr/bin/env python

# Only two difficult things in computer programming:
# 1. Naming things
# 2. Cache invalidation
# 3. Off by one errors

# ... but, this still seems difficult. It's basically a brute-force
# to find some pairings that don't work. Ideally, it'd also try to match
# gender and ages.

# TODO: minor bugs. Just keep running it until you get some pairings
# that you like. Sometimes pairings aren't quite right, so keep going.
# 

import random

adults = []
# the more groupings, the better:
adults.append("parentA1 parentA2") # replace with actual names
adults.append("parentB1 parentB2") # first names only (no spaces)
adults.append("parentC1 parentC2")
adults.append("parentD1 parentD2")
adults.append("parentE1 parentE2")
adults.append("parentF1 parentF2")
adults.append("parentG1 parentG2")
adults = sorted(adults, reverse=True)

print("Using adult groups: %s" % "\n".join(adults))

# the number of kid groups should match the number of parent groups:
kids = [
    # replace with actual child names.
    "childA1 childA2 childA3 childA4",
    "childB1 childB2 childB3 childB4 childB5",
    "childC1",
    "childD1 childD2 childD3",
    "childE1 childE2 childE3 childE4",
    "childF1 childF2",
    "childG1",
]
kids = sorted(kids, reverse=True)

print("Using kid groups: %s" % "\n".join(kids))


# generate ten possible pairing groups:
count = 0
while True:

    count += 1

    print("")
    print("="*5 + " Matchup #%s " % (count) + "="*5)

    for group_of_groups in adults, kids:

        c = 0

        print("")

        big_pool_of_people = " ".join(group_of_groups).split()
        random.shuffle(big_pool_of_people)

        for this_family in group_of_groups:

            other_families = [g for g in group_of_groups if g != this_family]
            other_family_members = " ".join(other_families).split()
            family = this_family.split()
            random.shuffle(other_family_members)
            random.shuffle(family)

            for family_member in family:

                c += 1

                for possible_recipient in big_pool_of_people:
                    if possible_recipient not in family and possible_recipient in other_family_members:
                        other_family_members.remove(possible_recipient)
                        big_pool_of_people.remove(possible_recipient)
                        print(str(c).ljust(4) + family_member.ljust(9) + " -> " + possible_recipient)
                        break


            # print (other_family_members, big_pool_of_people)

    print("")
    raw_input("Continue? Press Enter, or Control-C to abort.")

