import sys
sys.path.append('./Work/04_Classes-and-objects/')
from stock import Stock
sys.path.append('./Solutions/3_18')
import fileparse

class Portfolio:
    def __init__(self) -> None:
        self.holdings = []
        
    def append(self, holding):
        if not isinstance(holding, Stock):
            raise TypeError('holding must be a Stock instance')
        self.holdings.append(holding)
        
    # read a portfolio from a CSV file, make a class method for it
    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], 
                                        types=[str, int, float], **opts)
        for d in portdicts:
            self.append(Stock(**d))
        return self