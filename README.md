# christmas_gift_pairs

To use, just modify the christmas_pairs.py file and replace the names of the adults and the kids with real first names. (No spaces -- use underscores instead.)

Don't forget to chmod +x christmas_pairs.py on Mac or Linux and then execute.

Make sure that the number of adults is each two and the number of groups of parents match each of the groups of kids (in other words, if there are seven families, then there should be seven groups of parents and seven groups of kids; including the parents is probably optional, but it's included here since it's easy to do.)

This script basically brute-forces a bunch of pairings and tries to match up just one kid with another, even with mismatched family sizes, and tries to avoid one child buying for another in the same family.

The algorithm is pretty quick and dirty -- more elegant pull requests appreciated.
