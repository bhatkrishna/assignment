# 30. Write a Python script to check whether a given key already exists in a
# dictionary.
dict_={2:3,4:6,6:7}
def key_present(x):
    if x in dict_:
        print("key is presest")
    else:
        print("key is absent")
key_present(5)
key_present(3)