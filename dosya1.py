f = open('kurs.txt', 'w')
f.write('hayrunnisa korkmaz\n')
f.write('mertcan yılmaz\n')
f.write('yunus emre tan\n')
f.write('melih bozacı\n')
f.write('onur yıldız\n')
f.write('yakup eşki\n')
f = open('kurs.txt', 'r')
i=1
while(i<=6):
    okunan=f.readline()
    okunan=okunan[:-1]
    print okunan
    i=i+1
f.close()