'''
namafile: sba.py
Lembar kerja/script Latihan SBA
'''
# >>>>>>LEMBAR KERJA>>>>>>>>>
# lembar ini hanya berisi pendefinisian fungsi dan class saja
 
#email netacad
email = 'muhammad.adipurna.k@mail.ugm.ac.id'
 
# >>>>>>Soal 1
def fungsiIO():
  pass
  # Mulai kode anda dari sini
  numbers = input("Masukan input angka yang dipisahkan dengan spasi: ")
  numbers_list = numbers.split(" ")

  for i in sorted(numbers_list):
    i = int(i)
    print('*' * i)

# >>>>>>Akhir Soal 1 
 
# >>>>>>Soal 2
def caseShopia(txt):
  pass
  # Mulai kode anda dari sini
  Shopia_txt = ''
  for t in txt:
    if t.islower():
      Shopia_txt += t.upper()
    elif t.isupper():
      Shopia_txt += t.lower()
    else:
      continue

  return Shopia_txt

# >>>>>>Akhir Soal 2 
 
# Jangan diubah biarkan seperti ini
dcur2idr = {'USD': 14425, 'EUR': 16225, 'AUD': 9925, 'CAD': 10500, 
             'GBP': 17800, 'CHF': 15200, 'SGD': 10375, 'HKD': 1775, 
             'JPY': 132500, 'MYR': 3250, 'SAR': 3500, 'WON': 10750, 
             'IDR': 1}
 
# >>>>>> Soal 3 
def usd2eur(usd):
  pass
  # Mulai kode anda dari sini
  idr = usd * dcur2idr['USD']
  eur = idr / dcur2idr['EUR']

  return eur
 
# >>>>>>Akhir Soal 3 
 
 
# >>>>>>Soal 4 
class MoneyChanger:
  def __init__(self,dcurrency,base='IDR',percent=2):
    pass
    # Mulai kode anda dari sini
    self.dcurrency = dcurrency
    self.base = self.change_base(base)
    self.percent = percent
 
  def selling_price(self,nominal,curr):
    pass
    # Mulai kode anda dari sini
    idr = nominal * self.dcurrency[curr]
    target = idr / self.dcurrency[self.base]
    
    return target + (target*0.02)
  def buying_price(self,nominal,curr):
    pass
    # Mulai kode anda dari sini
    idr = nominal * self.dcurrency[curr]
    target = idr / self.dcurrency[self.base]
    
    return target - (target*0.02)
 
  def change_base(self,new_base):
    pass
    # Mulai kode anda dari sini
    self.base = new_base
    return self.base
 
# >>>>>>Akhir Soal 4 
 
# >>>>>>AKHIR LEMBAR KERJA>>>>>>>>>

# KODE DI BAWAH INI UNTUK TESTING
# ANDA BOLEH MEMBUANG SEMUA KODE DI SAAT SUBMISI KE NETACAD
 
def main():
  pass
  # >>>>>TEST DI SINI>>>>>>
  # gunakan BLOCK MAIN ini untuk mengetes
  # untuk pengetesan kode hanya boleh di bagian sini
  # silakan test sesuka hati di sini
 
  # ############################################
  # uncomment script di bawah ini untuk testing
  # ############################################
  
  # print('test soal 1')
  # fungsiIO() # contoh input: 7 4 5 2 1 3
 
  # print('test soal 2')
  # print(caseShopia('thXGth876%^$LMn.'))
 
  # print('test soal 3')
  # print(usd2eur(100))  # mengubah 100 USD ke EUR
 
  # print('test soal 4')
  # mc = MoneyChanger(dcur2idr,base='EUR') # object mc dengan base EUR
  # print('base', mc.base)
  # print(mc.selling_price(100,'USD')) # nilai jual 100 USD ke EUR (Base)
  # print(mc.buying_price(100,'USD')) # nilai beli 100 USD ke EUR (Base)
  
  # mc.change_base('IDR') # Ganti Base object mc ke IDR
  # print('base', mc.base)
  # print(mc.selling_price(100,'USD')) # nilai jual 100 USD ke IDR (Base)
  # print(mc.buying_price(100,'USD'))  # nilai beli 100 USD ke IDR (Base)
 
  # >>>>>AKHIR TEST DI SINI>>>>>>
 
if __name__ == '__main__':
  main()