ra=int(input('Enter the age of Ram '))
sa=int(input('Enter the age of Shyam '))
aj=int(input('Enter the age of Ajay '))

if(ra==sa==aj):
  print('EQUAL AGE')
elif(ra<sa and ra<aj):
    print('Ram is younger ')
elif(sa<ra and sa<aj):
    print('Syam is younger')
else:
    print('Ajay is younger')