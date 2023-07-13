import maidenhead

def dimension(locator: str):
    N = len(locator)
    if N == 2:
        return (20.0, 10.0)
    elif N == 4:
        return (2.0, 1.0)
    elif N == 6:
        return (5/60, 2.5/60)
    elif N == 8:
        return (30/3600,15/3600)
    else:
        raise ValueError("invalid locator")

def locator_region(locator: str):
    (sw_lat, sw_lon )= maidenhead.to_location(locator)
    (width, height) = dimension(locator)

    ne_lat = sw_lat + height
    ne_lon = sw_lon + width
    return f"{sw_lon}/{sw_lat}/{ne_lon}/{ne_lat}+r"


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(
        description ="get gmt region from maidenhead locator"
    )
    parser.add_argument("locator")

    args = parser.parse_args()
    print(locator_region(args.locator))

