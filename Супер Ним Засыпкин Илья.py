def f(letter):
  string_1 = "abcdefgh"
  string_2="12345678"
  if letter in string_1:
    for i in list_board:
      i[x[letter]]= 0
  if letter in string_2:
    list_board[y[letter]]=[0]*8
  
  print('  '+'a',' '+'b',' '+'c',' '+'d',' '+'e',' '+'f',' '+'g',' '+'h')
  for idx,i in enumerate(list_board):
    print((chr(ord('1')+idx))+str(i))
