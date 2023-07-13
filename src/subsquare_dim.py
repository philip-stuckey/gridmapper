from maiden_region import dimension
import math

def subsquare_dimensions(locator: str):
   return dimension(locator if len(locator) == 8 else locator + '00')

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser("sub-square dimensions")
    parser.add_argument("locator")
    parser.add_argument("dimension", type=int)
    args=parser.parse_args()
    print(f"{int(subsquare_dimensions(args.locator)[args.dimension]*3600)}s")

