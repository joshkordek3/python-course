class list (list):
    def contains (self, item):
        return self.count(item) > 0

converters = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "ml": 1,
    "l": 1000
}

def quantity (amount, unit):
    return {"amount": amount, "unit": unit}

def convert (unitQuantity):
    if unitQuantity["unit"] == "":
        return unitQuantity['amount']
    return unitQuantity["amount"] * converters[unitQuantity["unit"]]

def printReadableString (array):
    for item in array:
        print(f"{item}: {array[item]['amount']}{array[item]['unit']}")

def String (value):
    return f"{value}"

def newObjectKey (dictionary):
    return {"valueKeys": list(dictionary.keys()), "values": dictionary}

resources = newObjectKey({
    "water": quantity(300, "ml"),
    "milk": quantity(200, "ml"),
    "coffee": quantity(100, "g"),
    "money": quantity(20, "")# ,
    # "sugar": quantity(100, "g")
})

coffees = newObjectKey({
    "latte": newObjectKey({
        "water": quantity(200, "ml"),
        "coffee": quantity(24, "g"),
        "milk": quantity(150, "ml"),
        "cost": quantity(2.5, "")
    }),
    "espresso": newObjectKey({
        "water": quantity(50, "ml"),
        "coffee": quantity(18, "g"),
        "milk": quantity(0, "ml"),
        "cost": quantity(1, "")
    }),
    "cappuccino": newObjectKey({
        "water": quantity(250, "ml"),
        "coffee": quantity(24, "g"),
        "milk": quantity(100, "ml"),
        "cost": quantity(3.8, "")
    })
})

response = None
while True:
    print("")
    response = input("What would you like to do? Type 'help' for a list of commands. ").lower()
    if response == "":
        continue
    response = response.strip()
    if response == "help":
        print("")
        print("order [coffee name] - orders a coffee")
        print("")
        print("get [coffee name] [ingredient] - gets how much of the specified ingredient you need to make the coffee")
        print("")
        print("my [ingredient] - returns how much of the specified ingredient you have")
        continue
    responseWords = response.split(" ")
    if responseWords[0] == "get":
        if not coffees["valueKeys"].contains(responseWords[1]):
            print("invalid command, maybe you made a typo?")
            continue
        value = coffees["values"][responseWords[1]]
        if responseWords[2] == "ingredients":
            printReadableString(value["values"])
            continue
        if not value["valueKeys"].contains(responseWords[2]):
            print("invalid command, maybe you made a typo?")
            continue
        print(convert(value["values"][responseWords[2]]))

    if responseWords[0] == "my":
        if responseWords[1] == "things":
            printReadableString(resources["values"])
            continue
        if not resources["valueKeys"].contains(responseWords[1]):
            print("invalid command, maybe you made a typo?")
            continue
        r = resources["values"][responseWords[1]]
        print(f"{responseWords[1]}: {r['amount']}{r['unit']}")

    if responseWords[0] == "order":
        if not coffees["valueKeys"].contains(responseWords[1]):
            print("invalid command, maybe you made a typo?")
            continue
        required = [list(), list(), list(), list()]
        coffee = coffees["values"][responseWords[1]]["values"]
        resourcesAvailable = resources["values"]
        for key in coffee:
            if key == "cost":
                if convert(resourcesAvailable["money"]) < convert(coffee[key]):
                    required[resources["valueKeys"].index("money")] = [coffee[key], resourcesAvailable["money"], resourcesAvailable["money"]["unit"], "money"]
                continue
            if convert(resourcesAvailable[key]) < convert(coffee[key]):
                required[resources["valueKeys"].index(key)] = [coffee[key], resourcesAvailable[key], resourcesAvailable[key]["unit"], key]
        if len(required[0]) == 0 and len(required[1]) == 0 and len(required[2]) == 0 and len(required[3]) == 0:
            for key in coffee:
                if key == "cost":
                    resources["values"]["money"] = quantity(convert(resources["values"]["money"]) - convert(coffee[key]), coffee[key]["unit"])
                    continue
                resources["values"][key] = quantity(convert(resources["values"][key]) - convert(coffee[key]), coffee[key]["unit"])
            print(f"Here is your {responseWords[1]}. Enjoy! :)")
            continue
        printValue = "I still need "
        actualRequirements = []
        for requirement in required:
            if len(requirement) == 4:
                actualRequirements.append(requirement)
        required = actualRequirements
        i = 0
        for requirement in required:
            if requirement[3] == "money":
                printValue += f"{convert(requirement[0]) - convert(requirement[1])} more money"
            else:
                printValue += f"{convert(requirement[0]) - convert(requirement[1])}{requirement[2]} of {requirement[3]}"
            if i == len(required) - 2:
                if len(required) == 2:
                    printValue += " "
                else:
                    printValue += ", "
                printValue += "and "
            elif not i == len(required) - 1:
                printValue += ", "
            i += 1
        print(printValue)