# immutable dictionary
from collections import namedtuple

def test(m, sc, ss, l1, l2, l3):
    nmdTpl = namedtuple("Marks", "maths science social lang1 lang2 lang3")
    mrks = nmdTpl(maths=m, science=sc, social=ss, lang1=l1, lang2=l2, lang3=l3)
    return mrks

marks = test(98, 96, 93, 89, 90,95)
print(type(marks))
print(marks)
print("-" * 60)
print(f"Mathematics :{marks.maths}")
print(f"Science     :{marks.science}")
print(f"Social      :{marks.social}")
print(f"Language1   :{marks.lang1}")
print(f"Language2   :{marks.lang2}")
print(f"Language3   :{marks.lang3}")


