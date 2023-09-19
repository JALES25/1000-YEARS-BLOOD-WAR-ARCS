def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()

print_text = decor(print_text)
print_text()

@decor
def wrp_txt():
    print('i will be free, i willnbe free \n I WILL BE \n GLORIUAS \n bDUH dah DUmm dumm \n i will be free, i willnbe free \n I WILL BE \n GLORIUAS \n bDUH dah DUmm dumm \n i will be free, i willnbe free \n I WILL BE \n GLORIUAS \n bDUH dah DUmm dumm') 

wrp = decor(wrp_txt)
wrp()

@decor
def wrp_tx():
    print("i will be free, i willnbe free \n I WILL BE \n GLORIUAS \n bDUH dah DUmm dumm")

dwrp = decor(wrp_tx)
dwrp()