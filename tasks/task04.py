from typing import Dict, List, Any

tree = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [4, 5]
       },
       "node12": [6]
   },
   "node2": [7, 8, 9],
    "node3": [10],
    "node4": [12, 324, 567, 3456]

}


def collect_leaves(data: Any[Dict, List], collector: list = []) -> List:
    collector = []
    if type(data) == dict:
        for k, v in data.items():
            collector.extend(collect_leaves(v, collector))
    elif type(data) == list:
        for el in data:
            collector.append(el)
    return collector


print(collect_leaves([1, 2, 3]))
print(collect_leaves(tree))




