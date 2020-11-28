import json

jsonfile = open("LifeExpectation.json")

data = json.loads(jsonfile.read())

jsonfile.close()

print("#"*80)
for item in data:
    print(item)

print("#"*80)

animals = {
    "dog": "Marvin",
    "cat": "Gina",
    "Rat": "Pinky",
    "Hamster": "Barney"
    }

print("="*80)
for k,v in animals.items():
    print(f"{k}: {v}")
print("="*80)

print("+"*80)
print(json.dumps(animals))
print("+"*80)

jsondump = open("animals.json", "a")
jsondump.write(json.dumps(animals))
jsondump.close()

