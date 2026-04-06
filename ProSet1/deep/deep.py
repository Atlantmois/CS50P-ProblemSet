answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
answer = answer.replace("-", " ")
if answer == "42" or answer == "forty two":
    print("Yes")
else:
    print("No")
