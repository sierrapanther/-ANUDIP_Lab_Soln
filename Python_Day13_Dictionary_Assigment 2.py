
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenating the dictionaries
result = {}
for d in (dic1, dic2, dic3): 
    result.update(d)

print(result)
