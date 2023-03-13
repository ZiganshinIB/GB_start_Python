


def find_farthest_orbit(orbits):
    return max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1])


if __name__ == "__main__":
    transformation = lambda x: x
    values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # или любой другой список
    transormed_values = list(map(transformation, values))
    print(transormed_values)
    print(values)
    assert transormed_values == values

