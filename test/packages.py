print "Please enter dimentions in mm and weight in kg"
#input required dimentions
height = int(raw_input("Enter Height of box:"))
breadth = int(raw_input("Enter breadth of box:"))
length = int(raw_input("Enter length of box:"))
weight = int(raw_input("Enter weight of box:"))


# Make costs varaiables
sc = '$5'
mc = '$7.50'
lc = '$8.50'


#if statements to decide cost of package

if height <= 150 and breadth <= 300 and length <= 200 and weight <= 25:
  print 'Cost for package is' + ' ' + sc


elif height <= 200 and breadth <= 400 and length <= 300 and weight <= 25:
  print 'Cost for package is' + ' ' + mc


elif height <= 250 and breadth <= 600 and length <= 400 and weight <= 25:
  print 'Cost for package is' + ' ' + lc


elif height > 250:
  print 'The height must be under 250mm'
elif breadth > 600:
  print 'The breadth must be under 600mm'
elif length > 400:
  print 'The length must be under 400mm'
elif weight > 25:
  print 'The package must be under 25kg'

