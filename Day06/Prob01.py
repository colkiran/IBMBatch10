from itertools import groupby

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ('plant', 'sunflower'), ("vehicle", "harley") ,
          ("vehicle", "speed boat"), ("vehicle", "school bus")]
dic = {}
f = lambda x: x[0]

for key, val in groupby(sorted(things, key=f), f):
    dic[key] = list(val)

print(dic)
# Results in
# {'animal': [('animal', 'bear'), ('animal', 'duck')],
# 'plant': [('plant', 'cactus')],
# 'vehicle': [('vehicle', 'harley'),
# ('vehicle', 'speed boat'),
# ('vehicle', 'school bus')]}