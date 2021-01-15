def isnumber(mystring):
    digitcount = 0
    for i in range(0, len(mystring)):
        c = mystring[i]
        if ((not c.isdigit()) and (c != '.') and (not (i == 0 and c == '-'))):
            return False
        elif (c.isdigit()):
            digitcount += 1
    if (digitcount != 0):
       return True

def test(file1, file2):
   firstfile = open(file1, 'r')
   secondfile = open(file2, 'r')
   lines1 = []
   lines2 = []
   for line in firstfile:
      lines1.append(line.strip())
   for line in secondfile:
      lines2.append(line.strip())

   if (len(lines1) != len(lines2)):
       return False

   for i in range(0, len(lines1)):
       contents1 = lines1[i].split('\t')
       contents2 = lines2[i].split('\t')
       for j in range(0, len(contents1)):
          if (isnumber(contents1[j]) and not isnumber(contents2[j])):
              return False
          elif (not isnumber(contents1[j]) and isnumber(contents2[j])):
              return False
          elif (isnumber(contents1[j])):
              f1 = float(contents1[j])
              f2 = float(contents2[j])
              if ((f2-f1)/f1 > 0.01):
                  return False
          else:
              if (contents1[j] != contents2[j]):
                  print(contents1[j])
                  print(contents2[j])
                  return False
   return True
