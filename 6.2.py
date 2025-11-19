def convert (sec):
    d = sec // 86400
    sec = sec % 86400

    h = sec // 3600
    sec = sec % 3600
    
    m = sec // 60
    sec = sec % 60
    return f'{d} днів, {str(h).zfill(2)}:{str(m).zfill(2)}:{str(sec).zfill(2)}'

print (convert(0))
print (convert(224930))
print (convert(466289))
print (convert(950400))
print (convert(1209600))
print (convert(1900800))
print (convert(863999))
print (convert(22493))
print (convert(7948799))