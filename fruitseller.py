import json
import os


filename = "database.json"
def startup(filename):
    print(os.path.exists(filename))
    stock = {"orange": 25,
            "apple": 20,
            "bannana": 30,
            "pineapple": 15,
            "kiwi": 5}
    if os._exists(filename):
        file_data = open(filename).read()
        print(len(file_data))
        if len(file_data) > 0:
            stock_data = json.loads(file_data)
            return stock_data
        else:
            return stock
    else:
        return stock        

stock = startup(filename)

while True:
    print(stock)
    action = input("what you want? buy/sell/exit:")

    if action == "sell":
        fruit_name = input("Enter the fruit name:")
        how_much = int(input("Enter the quantity:"))
        current_stock = stock.get(fruit_name)
        if not current_stock:
            print("sorry we have only these fruites ")
            print(stock)
        elif current_stock < how_much:
            print("current stock is {}".format(current_stock))
        else:
            new_stock = current_stock - how_much

            stock[fruit_name] = new_stock

            print(stock)

    elif action == "buy":

        fruit_name = input("Enter the fruit name:")
        how_much = float(input("Enter the quantity:"))

        current_stock = stock.get(fruit_name)
        if current_stock == None:
            stock[fruit_name] = how_much
        else:
            stock[fruit_name] = current_stock + how_much

        print(stock)
        
    elif action == "exit":
        json_stock = json.dumps(stock)
        file = open(filename, "w")
        file.write(json_stock)
        file.close()
        exit()


    