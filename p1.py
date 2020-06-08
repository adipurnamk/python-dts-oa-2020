# nama file p1.py 
# Isikan nama anda dan copy semua cell code yang dengan komentar #Graded
 
#netacad email cth: 'abcd@g mail.com'
email='muhammad.adipurna.k@mail.ugm.ac.id'
priority=4
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#Graded

def letter_catalog(items,letter='A'):
  pass
  # MULAI KODEMU DI SINI
  cat = []

  for i in items:
    if i.startswith(letter):
      cat.append(i)
  
  return cat

#Graded

def counter_item(items):
  pass
  # MULAI KODEMU DI SINI
  dict = {}

  for i in items:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1 
   
  return dict

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = dict(zip(fruits, prices))

def total_price(dcounter,fprice):
  pass
  # MULAI KODEMU DI SINI

  total = 0

  for key in dcounter.keys():
    price = dcounter[key] * fprice[key]
    total += price

  return total

#Graded

def discounted_price(total,discount,minprice=100):
  pass
  # MULAI KODEMU DI SINI
  if total >= minprice:
    total -= (discount*total/100)
  else:
    total = total

  return total

#Graded

def print_summary(items,fprice):
  pass
  # MULAI KODEMU DI SINI
  count = counter_item(items)
  
  grocs = list(count.values())
  fruits = list(count.keys())
  
  prices = []
  for key in count.keys():
    price = count[key] * fprice[key]
    prices.append(price)

  zipped = list(zip(grocs, fruits, prices))
  zipped.sort(key=lambda k: k[1])

  
  total = total_price(count,fruit_price)
  discount = discounted_price(total, 10, minprice=100)

  for i in range(len(count)):
    print(f"{zipped[i][0]} {zipped[i][1]} : {zipped[i][2]}")
  print(f"total : {total}")
  print(f"discount price : {discount}")
  
