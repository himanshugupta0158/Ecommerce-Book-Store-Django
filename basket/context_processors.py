from .basket import Basket

"""
The function here which is saved as context processor in settings.py
file will be accessable in site wide/anywhere in this project.
"""


def basket(request):
    return {"basket": Basket(request)}
