# Dictionary is ordered, mutable and do not allow duplicates

person = [{
    "name" : "Nisanth",
    "age" : 33,
    "place" : "Chennai"
},{
    "name" : "Atchai",
    "age" : 33,
    "place" : "Tilberg"
}
]

print(person)

City = dict({"Name" : "Chennai", "State" : "TamilNadu", "Year" : 1638})


print(len(City))
print(City)

a = City["Name"]
print(a)

b = City.get("Name")
print(b)

print(City.keys())

print(City.values())

City["Governance"] = "Metropolitan"

print(City)

print(City.items())

City["Name"] = "Coimbatore"
City["Year"] = 1982
print(City)

City.update({"Mayor" : "Priya"})
print(City)

Movie = {
    "Name" : "Attakathi"
}

Movie["Director"] = "Pa.Ranjith"

print(Movie)

Movie.update({"Year" : 2012})

print(Movie)

Movie.pop("Year")

print(Movie)

Movie.popitem()

print(Movie)

Movie.clear()

print(Movie)

Movie.update({
    "Name" : "Attakathi"
})

print(Movie)

del Movie

Movie = {
    "Name" : "Attakathi",
    "Director" : "Pa.Ranjith",
    "Year" : 2012,
    "Producer" : "C.V.Kumar" 
}

for i in Movie:
    print(i)

for i in Movie:
    print(Movie[i])

for i in Movie.values():
    print(i)

for i in Movie.keys():
    print(i)

for x,y in Movie.items():
    print(x, ":", y)

Movie2 = Movie.copy()
print(Movie2)

Movie3 = dict(Movie)
print(Movie3)

# Nested Dictionaries

Movies = {
    "Movie1":{
        "Name" : "Attakathi"
    },
    "Movie2": {
        "Director" : "Pa.Ranjith"
    },
    "Movie3": {
        "Year" : 2012
    }
}

for i,j in Movies.items():
    for k in j:
        print(j[k])
