import json
import collections

tree = lambda: collections.defaultdict(tree)
root = tree()
root['menu']['id'] = 'file'
root['menu']['value'] = 'File'
root['menu']['menuitems']['new']['value'] = 'New'
root['menu']['menuitems']['new']['onclick'] = 'new();'
root['menu']['menuitems']['open']['value'] = 'Open'
root['menu']['menuitems']['open']['onclick'] = 'open();'
root['menu']['menuitems']['close']['value'] = 'Close'
root['menu']['menuitems']['close']['onclick'] = 'close();'

print(json.dumps(root, sort_keys=True, indent=4, separators=(',', ': ')))

# {
#     "menu": {
#         "id": "file",
#         "menuitems": {
#             "close": {
#                 "onclick": "close();",
#                 "value": "Close"
#             },
#             "new": {
#                 "onclick": "new();",
#                 "value": "New"
#             },
#             "open": {
#                 "onclick": "open();",
#                 "value": "Open"
#             }
#         },
#         "value": "File"
#     }
# }
