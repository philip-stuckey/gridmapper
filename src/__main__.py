import pygmt

def main(locator: str):
    # convert locator to region
    region = locator_region(locator)

    fig = pygmt.Figure()
    fig.coast(
            region = region,
            frame="ag"
        )
    fig.show()
