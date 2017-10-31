# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:38:39 2017

@author: k
"""


import sqlite3
print(sqlite3.version)

baglanti = sqlite3.connect('ilkdata.db')
baglanti.row_factory = sqlite3.Row

if(baglanti):
    print('Baglanti Başarılı!')
else:
    print('Bağlantı Başarısız!')
    
veritabani_sec = baglanti.cursor()
oku = veritabani_sec.execute('SELECT * FROM t')


for  veri_cek in oku.fetchall():
    print('Adı  : {1} tc no:{0}'.format(veri_cek[1],veri_cek[2])) 
      
    print(veri_cek[0],veri_cek['ad'],veri_cek['tckimlik'])
    
baglanti.commit()
baglanti.close()