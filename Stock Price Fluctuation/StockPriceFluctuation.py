import json
import sys
from collections import defaultdict

class StockPrice:
    def __init__(self):
        self.prices = {}
        self.latest_timestamp = 0
    
    def update(self, timestamp, price):
        self.prices[timestamp] = price
        if timestamp > self.latest_timestamp:
            self.latest_timestamp = timestamp
    
    def current(self):
        return self.prices[self.latest_timestamp]
    
    def maximum(self):
        return max(self.prices.values())
    
    def minimum(self):
        return min(self.prices.values())

def solution(operations, values):
    stock = StockPrice()
    results = []
    
    for i, op in enumerate(operations):
        if op == "StockPrice":
            continue
        elif op == "update":
            stock.update(values[i][0], values[i][1])
        elif op == "current":
            results.append(stock.current())
        elif op == "maximum":
            results.append(stock.maximum())
        elif op == "minimum":
            results.append(stock.minimum())
    
    return results

lines = sys.stdin.read().strip().split('\n')
operations = json.loads(lines[0])
values = json.loads(lines[1])
result = solution(operations, values)
print(json.dumps(result))