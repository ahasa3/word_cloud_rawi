def find_perawi(hadis):
  splited=hadis.replace(';','').replace(':',' ').replace('"',' ').replace(',','').replace('.','').lower().split(' ')
  sanad=[]
  matan = []
  for i, kt in enumerate(splited):
    if kt == "menceritakan" or kt == "mendengar" or kt == "berkata" or kt == "mengabarkan" or kt == "dari" or kt == "bertanya" or kt == "bahwa":
      sanad.append(i)
    elif kt == "bersabda" or kt == "rasulullah" or kt == "nabi" or kt == 'rasul':
      sanad.append(i)
      matan.append(' '.join(splited[i:]))
      break
  temp_rw = []
  for i in range(len(sanad)-1):
    temp_rw.append(splited[sanad[i]:sanad[i+1]])
  perawi = []
  for i in temp_rw:
    temp = []
    r = False
    for idx,j in enumerate(i):
        if '[' in j and ']' in j:
            perawi.append(j.replace('[','').replace(']',''))
        elif '[' in j:
            r = True
        elif ']' in j:
            temp.append(j)
            r = False
            merge = ' '.join(temp).replace('[','').replace(']','').replace("radliallahu 'anhu", '')
            if merge not in perawi:
              perawi.append(merge)
            break
        elif j == "bin" and r==False:
          merge = ' '.join(i[idx-1:idx+2]).replace("radliallahu 'anhu", '')
          if merge not in perawi:
            perawi.append(merge)
        elif j == "ibnu" and r==False:
          merge = ' '.join(i[idx:idx+2]).replace("radliallahu 'anhu", '')
          if merge not in perawi:
            perawi.append(merge)
        if r == True:
            temp.append(j)
  return perawi, matan