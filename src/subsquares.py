from itertools import product
import maidenhead

def level(locator: str):
    return len(locator)//2

def chrange(start, stop, step=1):
    return list(map(chr, range(ord(start), ord(stop)+1, step)))

def subsquares(locator: str):
    foo = (
        chrange('A','R'), chrange('0','9'), chrange('a', 'z'),
        chrange('0','9')
    )[level(locator)]

    for (lon_char, lat_char) in product(foo, foo):
        yield lon_char+lat_char

def main(locator: str):
    (lat, lon) = maidenhead.to_location(locator, center=True)
    print(lon, lat, locator)

    # locator is maximally precise, put it's name in the center
    if level(locator) == 4:
        return 

    for subsquare in subsquares(locator):
        (lat, lon) = maidenhead.to_location(locator+subsquare, center=True)
        print(lon, lat, subsquare)

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(
            description="print a list of sub-squares for a given maidenhead\
            locator"
    )
    parser.add_argument("locator")
    args = parser.parse_args()
    main(args.locator)

