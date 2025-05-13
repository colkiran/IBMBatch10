
print("Logical Operators".center(60, "-"))
# and, or, not

# and
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")

print("-" * 60)
# or
print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")
print(f"1 == 2 or 2 == 1 :{1 == 2 or 2 == 1}")

print("-" * 60)
# not
print(f"not(1 == 1 or 2 == 1) :{not(1 == 1 or 2 == 1)}")
print(f"not(1 == 2 or 2 == 1) :{not(1 == 2 or 2 == 1)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")      # integer representation of unicode characters
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")
print("-" * 60)
print(f"apple > orange :{'apple' > 'orange'}")
print(f"apple < orange :{'apple' < 'orange'}")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 << 2 :{5 << 2}")
print(f"5 >> 1 :{5 >> 1}")

print("Ternary Operator".center(60, "-"))
a = 18
print("Eligible" if a > 17 else "Not Eligible")
