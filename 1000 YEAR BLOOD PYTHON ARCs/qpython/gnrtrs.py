def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(22)))

def make_word(x):
    word = ""
    for ch in x:
        word += ch
        yield word

print(list(make_word('killbill'))) 