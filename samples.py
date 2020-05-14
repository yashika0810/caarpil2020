'''def square_digits(num):
    a=''
    for i in str(num):
        a+=str(int(i)**2)
    return int(a)
print(square_digits(99119))
'''
def remove_smallest(numbers):
  for i in range(len(numbers)):
    if numbers[i] == min(numbers):
      numbers.remove(numbers[i])
    if len(numbers)==0:
        return numbers
    if numbers[i]== numbers[i+1]:
      numbers.remove(numbers[i])
      return numbers
      break
a=remove_smallest([1,2,3,4,4,9,8,5,8])
print(a)


def disemvowel(string):
  vow=('A','a','E','e','I','i','O',
  'o','U','u')
  return ''.join([x for x in string if x not in vow])
 

print(disemvowel("This website is for losers LOL!"))

def Check_Vow(string): 
  vowels=('a','e','i','o','u')
  final = [each for each in string if each in vowels] 
  return len(final)
print(Check_Vow("consultadd"))
  
def add_binary(a,b):
  return bin(a+b)

print(add_binary(2,3))

def main(string):
    words = str(string).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
   

print(main("pig is a"))


def unique_in_order(iterable):
    if iterable == None:
        return None
    if iterable == []:
        return []
    result = []
    i = 0
    while i < len(iterable)-1:
        if iterable[i] == iterable[i+1]:
            i += 1
            continue
        result.append(iterable[i])
        i += 1
    result.append(iterable[i])
    return result

print(unique_in_order([1,2,3,1,1,1,3,3]))

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res
print(unique_in_order([1,2,3,4,1,1,4,4]))


'''def to_camel_case(text):
  output=''.join( [i for i in text if i not in '-'])
  return output[0].upper() + output[1:]
print(to_camel_case("the-sea-bhd"))
'''

def to_camel_case(text):
  output=text.split("-")
  t=[(i[0].upper()+i[1:]) for i in output]
  return "".join(t)
print(to_camel_case("the-sealth-warrior"))


def maskify(cc):
  a= ("#" * (len(cc)-4) + cc[-4:])
  return a
print(maskify("23456gfedvfcd"))


def parse_molecule (formula):
  newdict={}
  for i in formula:
    if i.isalpha():
      if i in newdict:
        newdict[i]+=1
      else:
        newdict[i]=1
  return newdict
print(parse_molecule('lett32er'))
