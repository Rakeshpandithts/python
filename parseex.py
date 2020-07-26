from parse import parse
line = "hello my name is rakesh, i am from bengaluru"
parse_format = "hello my name is {name}, i am from {city}"
result = parse(parse_format, line)

print(result["city"])