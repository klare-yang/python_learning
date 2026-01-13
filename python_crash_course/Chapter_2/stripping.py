programming_language = " python " # initialize the variable

print(programming_language) # print the original string
print(programming_language.rstrip()) # remove trailing whitespace
print(programming_language.lstrip()) # remove leading whitespace
print(f"{programming_language.removeprefix(' ')}\n") # remove a single leading whitespace prefix

# Implicit f-string concatenation
print(f"{programming_language}"
      f"{programming_language.rstrip()}"
      f"{programming_language.lstrip()}"
      f"{programming_language.removeprefix(' ')}\n")

# test the removeprefix behaviour
print(f"{programming_language}"
      f"{programming_language.rstrip()}"
      f"{programming_language.lstrip()}"
      f"{programming_language}")