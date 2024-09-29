#!/usr/bin/python3

sentence = "There should be one-- and preferably only one --obvious way to do it. lthough that way may not be obvious at first unless you're Dutch."

unique = list()

for word in sentence.split():
  if word == "preferably" or word == "only" or word == "one"  or word == "way" or word == "unless" :
    if word not in unique:
      unique.append(word)

for word in unique:
  print(word, end=" ")
