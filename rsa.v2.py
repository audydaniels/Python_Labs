
hold = {}
user_ask = 0

def display(user_ask):
    request = open("surfing_data.csv")
    for line in request:
        file = {}
        (file["id"], file["name"], file["country"], file["average"], file["board"], file["age"]) = line.split(";")
        if user_ask == file["id"]:
             print ("ID:             " + file["id"])
             print ("Name:           " + file["name"])
             print ("Country:        " + file["country"])
             print ("Average:        " + file["average"])
             print ("Board type:     " + file["board"])
             print ("Age:            " + file["age"])
    request.close()


user_ask = input("What is Compeditors ID: ")

display(user_ask)
if user_ask != file["id"]:
    retry = input("That is not a valid ID please put in a valid ID")
    user_ask = (retry)
    display(user_ask)
else:
    display(user_ask)






