import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

 #last = 13
 #rnd = random.randint(0, last)
 # print(random.sample(quotes, 2))
  sampling = random.sample(quotes, 2)
  for sample in sampling: print(sample)

if __name__== "__main__":
  primary()
