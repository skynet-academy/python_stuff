import json
from decimal import Decimal


jstring = '{"name":"prod1", "price": 12.50}'
json.loads(jstring, parse_float=Decimal)

