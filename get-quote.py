import random
def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt", "a")
  f.write(input("Tell me something I don't know: " + "\n"))
  f.close()
  f = open("quotes.txt")
  quotes = f.readlines()
  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
