# pass by reference we use mutable variables

def fun(lst):
    print(f"inside fun :{lst}")
    lst.append('Python Complete Reference')
    lst.append('Python for Networking')
    print(f"inside fun :{lst}")


books = ['Python for beginners', 'Advanced Python', 'Python Cookbook']

print(f"before the function call :{books}")

fun(books)

print(f"after the function call :{books}")
