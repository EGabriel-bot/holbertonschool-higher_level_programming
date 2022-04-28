#!/usr/bin/python3
import hidden_4

idx = 0
module = dir(hidden_4)
for i in range (len(module)):
  word = module[idx]
  if word[0] != "_":
    print(word)
  idx += 1
