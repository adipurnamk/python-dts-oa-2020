# nama file p3.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

#netacad email cth: 'abcd@gmail.com'
email='muhammad.adipurna.k@mail.ugm.ac.id'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini
# Graded
def caesar_encript(txt,shift):
  pass
  # Mulai Kode anda di sini
  result = ''
  for i in range(len(txt)):
    char = txt[i]

    if char.isupper():
      result += chr((ord(char) + shift-65) % 26 + 65)
    elif char.islower():
      result += chr((ord(char) + shift-97) % 26 + 97)
    else:
      result += char

  return result

    
# Fungsi Decript caesar
def caesar_decript(chiper,shift):
  return caesar_encript(chiper,-shift)

# Graded
 
# Fungsi mengacak urutan
def shuffle_order(txt,order):
  return ''.join([txt[i] for i in order])
 
# Fungsi untuk mengurutkan kembali sesuai order
def deshuffle_order(sftxt, order):
  pass 
  # Mulai Kode anda di sini
  d = dict(zip(order, sftxt))
  
  values = []
  for key, value in sorted(d.items()):
    values.append(value)

  # d = ''.join(sorted(dict(zip(sftxt, order))))
  return ''.join(values)

# Graded
 
import math
 
 
# convert txt ke dalam bentuk list teks yang lebih pendek
# dan terenkrispi dengan urutan acak setiap batchnya
def send_batch(txt,batch_order,shift=3):
  pass
  # Mulai Kode anda di sini

  # Cek panjang txt, jika kurang ditambah '_'
  n = len(batch_order)
  
  if len(txt) % n != 0:
    ceil = math.ceil(len(txt)/n)
    diff = abs(len(txt) - ceil*n)
    txt += '_' * diff

  # Enkripsi caesar
  txt = caesar_encript(txt,shift)

  # Split txt, hasil berupa list
  splitted = [txt[i:i+n] for i in range(0, len(txt), n)]
  
  result = []
  for i in splitted:
    shuffled = shuffle_order(i,batch_order)
    result.append(shuffled)

  return result

# batch_cpr: list keluaran send_batch
# fungsi ini akan mengembalikan lagi ke txt semula
def receive_batch(batch_cpr,batch_order,shift=3):
  batch_txt = [caesar_decript(deshuffle_order(i,batch_order),shift) for i in batch_cpr]
  return ''.join(batch_txt).strip('_')