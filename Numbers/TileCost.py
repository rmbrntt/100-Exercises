__author__ = 'barnett'
cost_per_tile = float(raw_input('Enter cost per tile: '))
sqFt_or_lxw = raw_input('Calculate cost by square footage or by width and length?\nEnter "S" for square footage.\n'
                        'Enter "WL" for height and length.\n')

if sqFt_or_lxw.upper() == "S":
    sqFt = int(raw_input('Enter square footage: '))
    print 'The cost to tile the room is $%s' % float(cost_per_tile*sqFt)
elif sqFt_or_lxw.upper() == "WL":
    length = float(raw_input('Enter length of room: '))
    width = float(raw_input('Enter width of room: '))
    print 'The cost to tile the room is $%s' % float(cost_per_tile*(width*length))
else:
    print "Invalid input, please enter 'S' or 'WL'"
