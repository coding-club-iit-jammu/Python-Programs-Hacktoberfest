q=int(input('no. of players='))
if q==1:
  import random
  boxes = [11,12,13,21,22,23,31,32,33]
  a=[' ',' ',' ']
  b=[' ',' ',' ']
  c=[' ',' ',' ']
  print('''
  INSTRUCTION:
  1.you should not enter the pre entered index.
  2.enter the specified index only.
  ''')
  print(a,'=', '[11,12,13]')
  print(b,'=', '[21,22,23]')
  print(c,'=', '[31,32,33]')
  print('give move according above index ')
  i=int(input(' player move 1='))
  boxes.remove(i)
  if i==11: 
    a[0]='x'
  elif i==12:
    a[1]='x'
  elif i==13:
    a[2]='x'    
  elif i==21: 
    b[0]='x' 
  elif i==22:
    b[1]='x'
  elif i==23:
    b[2]='x'
  elif i==31:  
    c[0]='x'
  elif i==32:
    c[1]='x'
  elif i==33:
    c[2]='x'

  i=random.choice(boxes)
  boxes.remove(i)
  if i==11: 
    a[0]='o'
  elif i==12:
    a[1]='o'
  elif i==13:
    a[2]='o'    
  elif i==21: 
    b[0]='o'
  elif i==22:
    b[1]='o'
  elif i==23:
    b[2]='o'
  elif i==31:  
    c[0]='o'
  elif i==32:
    c[1]='o'
  elif i==33:
    c[2]='o'
  print(a)
  print(b)
  print(c)
 
  i=int(input('player move 2='))
  boxes.remove(i)
  if i==11: 
    a[0]='x'
  elif i==12:
    a[1]='x'
  elif i==13:
    a[2]='x'    
  elif i==21: 
    b[0]='x'
  elif i==22:
    b[1]='x'
  elif i==23:
    b[2]='x'
  elif i==31:  
    c[0]='x'
  elif i==32:
    c[1]='x'
  elif i==33:
    c[2]='x'

  i=random.choice(boxes)
  boxes.remove(i)
  if i==11: 
    a[0]='o'
  elif i==12:
    a[1]='o'
  elif i==13:
    a[2]='o'    
  elif i==21: 
    b[0]='o'
  elif i==22:
    b[1]='o'
  elif i==23:
    b[2]='o'
  elif i==31:  
    c[0]='o'
  elif i==32:
    c[1]='o'
  elif i==33:
    c[2]='o'
  print(a)
  print(b)
  print(c)

  i=int(input(' player move 3='))
  boxes.remove(i)
  if i==11:
    a[0]='x'
  elif i==12:
    a[1]='x'
  elif i==13:
    a[2]='x'    
  elif i==21: 
    b[0]='x'
  elif i==22:
    b[1]='x'
  elif i==23:
    b[2]='x'
  elif i==31:  
    c[0]='x'
  elif i==32:
    c[1]='x'
  elif i==33:
    c[2]='x'

  if (a[0]==a[1]==a[2]=='x' or b[0]==b[1]==b[2]=='x' or c[0]==c[1]==c[2]=='x' or a[0]==b[0]==c[0]=='x' or a[1]==b[1]==c[1]=='x' or a[2]==b[2]==c[2]=='x' or a[0]==b[1]==c[2]=='x' or a[2]==b[1]==c[0]=='x'):
    print(' player winner')
  else:
    i=random.choice(boxes)
    boxes.remove(i)
    if i==11: 
      a[0]='o'
    elif i==12:
      a[1]='o'
    elif i==13:
       a[2]='o'    
    elif i==21: 
      b[0]='o'
    elif i==22:
      b[1]='o'
    elif i==23:
      b[2]='o'
    elif i==31:  
      c[0]='o'
    elif i==32:
      c[1]='o'
    elif i==33:
      c[2]='o'
    print(a)
    print(b)
    print(c)

    if (a[0]==a[1]==a[2]=='o' or b[0]==b[1]==b[2]=='o' or c[0]==c[1]==c[2]=='o' or a[0]==b[0]==c[0]=='o' or a[1]==b[1]==c[1]=='o' or a[2]==b[2]==c[2]=='o' or a[0]==b[1]==c[2]=='o' or a[2]==b[1]==c[0]=='o'):
      print('computer winnner')
    else:
      i=int(input(' player move 4='))
      boxes.remove(i)  
      if i==11:    
        a[0]='x'
      elif i==12:
        a[1]='x'
      elif i==13:
        a[2]='x'    
      elif i==21: 
        b[0]='x'
      elif i==22:
        b[1]='x'
      elif i==23:
        b[2]='x'
      elif i==31:  
        c[0]='x'
      elif i==32:
        c[1]='x'
      elif i==33:
        c[2]='x'

  if (a[0]==a[1]==a[2]=='x' or b[0]==b[1]==b[2]=='x' or c[0]==c[1]==c[2]=='x' or a[0]==b[0]==c[0]=='x' or a[1]==b[1]==c[1]=='x' or a[2]==b[2]==c[2]=='x' or a[0]==b[1]==c[2]=='x' or a[2]==b[1]==c[0]=='x'):
    print(' player winner')
  else:
    i=random.choice(boxes)
    boxes.remove(i)
    if i==11: 
      a[0]='o'
    elif i==12:
      a[1]='o'
    elif i==13:
      a[2]='o'    
    elif i==21: 
      b[0]='o'
    elif i==22:
      b[1]='o'
    elif i==23:
      b[2]='o'
    elif i==31:  
      c[0]='o'
    elif i==32:
      c[1]='o'
    elif i==33:
      c[2]='o'
    print(a)
    print(b)
    print(c)

    if (a[0]==a[1]==a[2]=='o' or b[0]==b[1]==b[2]=='o' or c[0]==c[1]==c[2]=='o' or a[0]==b[0]==c[0]=='o' or a[1]==b[1]==c[1]=='o' or a[2]==b[2]==c[2]=='o' or a[0]==b[1]==c[2]=='o' or a[2]==b[1]==c[0]=='o'):
      print('computer winner')
    else:
      i= int(input(' player move 5=')) 
      if i==11:    
        a[0]='x'
      elif i==12:
        a[1]='x'
      elif i==13:
        a[2]='x'    
      elif i==21: 
        b[0]='x'
      elif i==22:
        b[1]='x'
      elif i==23:
        b[2]='x'
      elif i==31:  
        c[0]='x'
      elif i==32:
        c[1]='x'
      elif i==33:
        c[2]='x'
      print(a)
      print(b)
      print(c)

  if (a[0]==a[1]==a[2]=='x' or b[0]==b[1]==b[2]=='x' or c[0]==c[1]==c[2]=='x' or a[0]==b[0]==c[0]=='x' or a[1]==b[1]==c[1]=='x' or a[2]==b[2]==c[2]=='x' or a[0]==b[1]==c[2]=='x' or a[2]==b[1]==c[0]=='x'):
    print(' player winner')
  else:
    print('no one winner')  
elif q==2:  
  a=[' ',' ',' ']
  b=[' ',' ',' ']
  c=[' ',' ',' ']
  print('''INSTRUCTIONS:
  1.You should not enter the pre entered Index
  2.enter the specified index only 
  ''')
  print(a,'=','[11,12,13]')
  print(b,'=','[21,22,23]')
  print(c,'=','[31,32,33]')
  print('players give their moves according above index')
  i=int(input('first payer move 1='))
  if i==11: 
    a[0]='x'
  elif i==12:
    a[1]='x'
  elif i==13:
    a[2]='x'    
  elif i==21: 
    b[0]='x'
  elif i==22:
    b[1]='x'
  elif i==23:
    b[2]='x'
  elif i==31:  
    c[0]='x'
  elif i==32:
    c[1]='x'
  elif i==33:
    c[2]='x'
  print(a)
  print(b)
  print(c)

  i=int(input('second player move 1='))
  if i==11: 
    a[0]='O'
  elif i==12:
    a[1]='o'
  elif i==13:
    a[2]='o'    
  elif i==21: 
    b[0]='o'
  elif i==22:
    b[1]='o'
  elif i==23:
    b[2]='o'
  elif i==31:  
    c[0]='o'
  elif i==32:
    c[1]='o'
  elif i==33:
    c[2]='o'
  print(a)
  print(b)
  print(c)
 
  i=int(input('first player move 2='))
  if i==11: 
    a[0]='x'
  elif i==12:
    a[1]='x'
  elif i==13:
    a[2]='x'    
  elif i==21: 
    b[0]='x'
  elif i==22:
    b[1]='x'
  elif i==23:
    b[2]='x'
  elif i==31:  
    c[0]='x'
  elif i==32:
    c[1]='x'
  elif i==33:
    c[2]='x'
  print(a)
  print(b)
  print(c)

  i=int(input('second player move 2='))
  if i==11: 
    a[0]='o'
  elif i==12:
    a[1]='o'
  elif i==13:
    a[2]='o'    
  elif i==21: 
    b[0]='o'
  elif i==22:
    b[1]='o'
  elif i==23:
    b[2]='o'
  elif i==31:  
    c[0]='o'
  elif i==32:
    c[1]='o'
  elif i==33:
    c[2]='o'
  print(a)
  print(b)
  print(c)

  i=int(input('first player move 3='))
  if i==11:
    a[0]='x'
  elif i==12:
    a[1]='x'
  elif i==13:
    a[2]='x'    
  elif i==21: 
    b[0]='x'
  elif i==22:
    b[1]='x'
  elif i==23:
    b[2]='x'
  elif i==31:  
    c[0]='x'
  elif i==32:
    c[1]='x'
  elif i==33:
    c[2]='x'
  print(a)
  print(b)
  print(c)

  if (a[0]==a[1]==a[2]=='x' or b[0]==b[1]==b[2]=='x' or c[0]==c[1]==c[2]=='x' or a[0]==b[0]==c[0]=='x' or a[1]==b[1]==c[1]=='x' or a[2]==b[2]==c[2]=='x' or a[0]==b[1]==c[2]=='x' or a[2]==b[1]==c[0]=='x'):
    print('first player winner')
  else:
    i=int(input('second player move 3='))
    if i==11: 
      a[0]='o'
    elif i==12:
      a[1]='o'
    elif i==13:
      a[2]='o'    
    elif i==21: 
      b[0]='o'
    elif i==22:
      b[1]='o'
    elif i==23:
      b[2]='o'
    elif i==31:  
      c[0]='o'
    elif i==32:
      c[1]='o'
    elif i==33:
      c[2]='o'
    print(a)
    print(b)
    print(c)

    if (a[0]==a[1]==a[2]=='o' or b[0]==b[1]==b[2]=='o' or c[0]==c[1]==c[2]=='o' or a[0]==b[0]==c[0]=='o' or a[1]==b[1]==c[1]=='o' or a[2]==b[2]==c[2]=='o' or a[0]==b[1]==c[2]=='o' or a[2]==b[1]==c[0]=='o'):
      print('second player winner')
    else:
      i=int(input('first player move 4='))  
      if i==11:    
        a[0]='x'
      elif i==12:
        a[1]='x'
      elif i==13:
        a[2]='x'    
      elif i==21: 
        b[0]='x'
      elif i==22:
        b[1]='x'
      elif i==23:
        b[2]='x'
      elif i==31:  
        c[0]='x'
      elif i==32:
        c[1]='x'
      elif i==33:
        c[2]='x'
      print(a)
      print(b)
      print(c)

  if (a[0]==a[1]==a[2]=='x' or b[0]==b[1]==b[2]=='x' or c[0]==c[1]==c[2]=='x' or a[0]==b[0]==c[0]=='x' or a[1]==b[1]==c[1]=='x' or a[2]==b[2]==c[2]=='x' or a[0]==b[1]==c[2]=='x' or a[2]==b[1]==c[0]=='x'):
    print('first player winner')
  else:
    i=int(input('second player move 4='))
    if i==11: 
      a[0]='o'
    elif i==12:
      a[1]='o'
    elif i==13:
      a[2]='o'    
    elif i==21: 
      b[0]='o'
    elif i==22:
      b[1]='o'
    elif i==23:
      b[2]='o'
    elif i==31:  
      c[0]='o'
    elif i==32:
      c[1]='o'
    elif i==33:
      c[2]='o'
    print(a)
    print(b)
    print(c)

    if (a[0]==a[1]==a[2]=='o' or b[0]==b[1]==b[2]=='o' or c[0]==c[1]==c[2]=='o' or a[0]==b[0]==c[0]=='o' or a[1]==b[1]==c[1]=='o' or a[2]==b[2]==c[2]=='o' or a[0]==b[1]==c[2]=='o' or a[2]==b[1]==c[0]=='o'):
      print('second player winner')
    else:
      i= int(input('first player move 5=')) 
      if i==11:    
        a[0]='x'
      elif i==12:
        a[1]='x'
      elif i==13:
        a[2]='x'    
      elif i==21: 
        b[0]='x'
      elif i==22:
        b[1]='x'
      elif i==23:
        b[2]='x'
      elif i==31:  
        c[0]='x'
      elif i==32:
        c[1]='x'
      elif i==33:
        c[2]='x'
      print(a)
      print(b)
      print(c)

  if (a[0]==a[1]==a[2]=='x' or b[0]==b[1]==b[2]=='x' or c[0]==c[1]==c[2]=='x' or a[0]==b[0]==c[0]=='x' or a[1]==b[1]==c[1]=='x' or a[2]==b[2]==c[2]=='x' or a[0]==b[1]==c[2]=='x' or a[2]==b[1]==c[0]=='x'):
    print('first player winner')
  else:
    print('no one winner') 
else:
  print('this game is maximum of two players ')
