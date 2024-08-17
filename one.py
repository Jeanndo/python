def func():
    print("func in one.py")

print("TOP LEVEL IN ONE,PY")

if __name__ == "__main__":
    print("This is one.py being run directly")
else:
    print("one.py being imported from another module")