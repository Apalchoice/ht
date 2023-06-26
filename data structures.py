# list datastructures, its ordered and changeable
cars = ["Mercedes", "Toyota", "Nissan", "Bmw", "Range rover"]
cars[1] ="subaru"
cars.append("jeep")
cars.insert(2, "Mitsubishi")
cars.sort()
print(cars)


# this is a tuple, ordered,its unchangeable
fruits=("mangoes", "apples", "banana", "ovacado", "apples")
my_tuple = (fruits)
count=len(my_tuple)
print(count)


#sets datastructure,unordered
countries = {"kenya", "uganda", "tanzania","burundi", "ethiopia"}
print(countries)

#dictinaries
matunda ={
    "amount":40,
    "jina": "ndizi",
    "rangi": "yellow"
}
matunda["size"]="large"
matunda.pop("rangi")
print(matunda)
