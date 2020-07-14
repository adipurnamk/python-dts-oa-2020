# nama file p2.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 2

#netacad email cth: 'abcd@gmail.com'
email='muhammad.adipurna.k@mail.ugm.ac.id'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#Graded

def isPointInCircle(x,y,r,center=(0,0)):
  # MULAI KODEMU DI SINI
  pass
  x0,y0 = center
  r2 = pow((x-x0),2) + pow((y-y0),2)

  if pow(r2, 0.5) <= r:
    return True
  else:
    return False

#Graded
import random


def generateRandomSquarePoints(n,length,center=(0,0)):
  # MULAI KODEMU DI SINI
  minx = center[0]-length/2
  miny = center[1]-length/2
  
  # Gunakan list comprehension dengan variable minx, miny, length, dan n
  points = [[random.uniform(minx, minx+length), random.uniform(miny, miny+length)] for i in range(n)] 

  return points

#Graded

def MCCircleArea(r,n=100,center=(0,0)):
  # MULAI KODEMU DI SINI
  pass
  points = generateRandomSquarePoints(n,length=r*2,center=(0,0))
  
  n_circle = 0
  for point in points:
    x,y = point
    if isPointInCircle(x,y,r,center=(0,0)) == True:
      n_circle += 1

  square_area = pow(r*2, 2)
  circle_area = n_circle/n * square_area

  return circle_area

#Graded

def LLNPiMC(nsim,nsample):
  # MULAI KODEMU DI SINI
  pass
  
  circle_areas = []
  for i in range(nsim):
    circle_area = MCCircleArea(r=1,n=nsample,center=(0,0))
    circle_areas.append(circle_area)
  
  estpi = sum(circle_areas)/nsim
  return estpi

# Graded

import math
def relativeError(act,est):
  
  # MULAI KODEMU DI SINI
  pass
  E = abs((est-act)/act * 100)
  return E