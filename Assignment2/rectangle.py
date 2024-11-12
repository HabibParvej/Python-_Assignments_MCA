ln=int(input('Enter the length of the rectangle: '))
br=int(input('Enter the length of the breadth: '))
area=ln*br
pr=2*(ln+br)
if(area>pr):
    print('Area is greater than the parameter')
else:
    print('parameter is greater than the area')