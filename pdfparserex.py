import tika
from tika import parser
import os

parse = parser.from_file('swiggy-order-39803023548.pdf')

print(parse)