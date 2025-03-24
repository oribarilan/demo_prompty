from pyplz import plz


@plz.task()
def login():
    """AZ CLI login."""
    plz.run("az login --tenant 9bc6f80b-73d8-4d7c-ae26-572c276851a5")
