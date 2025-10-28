# Match is a switch case
# Underscore is the default case

month = "Jan"
match month:
    case "Oct": 
        print("This is October month")
    case "Nov":
        print("This is November month")
    case _:
        print("Not in this year anymore")


# Underscore should always be the last case as it will match for all cases.

month = "Jan"
match month:
    case "Oct": 
        print("This is October month")
    case "Nov":
        print("This is November month")
    case _:
        print("Not in this year anymore")


day = 0
match day:
    case 1|2|3|4|5:
        print("This is a week day")
    case 6|0:
        print("This is a Weekend")
    case _:
        print("Not a valid enumeration")

# If statements can be inserted in case evaluation

day = 1
month = "Jun"
match day:
    case 0 if month == "Jun":
        print("A Sunday of June month")
    case _:
        print("Not a June month Sunday")

