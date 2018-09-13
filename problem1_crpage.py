# STAT/CS 287
# HW 01
# Problem1
#
# Name: Cecily Page
# Date: September 6th 2018


def similarity(a: set, b: set):
    """
    Calculates the similarity by |A intersect B| / |A union B|
    :param a: Set
    :param b: Set
    :return: Float
    """

    ab_intersect = a.intersection(b)
    ab_union = a.union(b)

    return len(ab_intersect)/ len(ab_union)


one = {2, 5, 4, 3, 7, 8}
two = {5, 34, 52, 84, 7, 8}
three = {43, 54, 84, 2, 'Octopus'}
four = {'Octopus', 'chicken', 'Kangaroo'}

print(one, two)
print('similarity:', similarity(one, two))
print(two, three)
print('similarity:', similarity(two, three))
print(three, four)
print('similarity:', similarity(three, four))



