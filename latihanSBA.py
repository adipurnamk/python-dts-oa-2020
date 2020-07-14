'''
namafile: latihanSBA.py
Lembar kerja/script Latihan SBA
'''
# >>>>>>LEMBAR KERJA>>>>>>>>>
# lembar ini hanya berisi pendefinisian fungsi dan class saja

#email netacad, JANGAN SAMPAI LUPA >>>>>>><<<<<<<
email = 'muhammad.adipurna.k@mail.ugm.ac.id'

#soal 1
class titik2d:  
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0 
        
    def ambiltitik(self):
        return (self.x,self.y)
    
    def tambahkan(self, x1, y1):
        self.x += x1
        self.y += y1
        return (self.x, self.y)
    
# soal 2
def run():
    titik = input("Masukkan nilai x dan y (dipisah dengan spasi): ")
    x, y = titik.split()
    return titik2d(float(x), float(y))
# >>>>>>AKHIR LEMBAR KERJA>>>>>>>>>



if __name__ == '__main__':
  # >>>>>TEST DI SINI>>>>>>
  # gunakan BLOCK MAIN ini untuk mengetes

  # untuk pengetesan kode hanya boleh di bagian sini
  # silakan test sesuka hati di sini
  t1 = run()
  print('titik1:',t1.ambiltitik())

  # >>>>>AKHIR TEST DI SINI>>>>>>
