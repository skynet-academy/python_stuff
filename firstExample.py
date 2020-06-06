#!/usr/bin/env python3
def sum(a,b):
    a_int = convert_int(a)
    b_int = convert_int(b)
    result = a_int + b_int
    return result
def convert_int(nro):
    converted_int = int(nro)
    return converted_int
rpt = sum("3","4")

print(rpt)
