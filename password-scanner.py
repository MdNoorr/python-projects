import random

add = "@2019", "123.", ".234", "@abc", "_2018", "()2000", "+0000", "@new", "<bd>", ":001", "read;"

s = "@", "_", ":", ";", "()", "{}", "[]", "-", "^",
"#", "/", "%", "?", ".""=", "!", ",", "$", "&", "¡"
char = str(input("Enter Your Password : "))

print("=" * 38, '\n', "The input :", char)
count = 0
sp = 0
for i in char:
    count = count + 1
for j in s:
    if j == i:
        sp = sp + 1
if count > 7 or sp > 0:
    print("The password is strong.")
else:
    print("The password is weak.")
    print("Suggested password :")
    print(char + (random.choice(add)))