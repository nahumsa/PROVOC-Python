def reset_board():
  """ Função para resetar o estado do board.
  """
  return ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']         

def test_winner(winner, players):
  tests = [['X', 'X', 'X',
          '4', '5', '6',
          '7', '8', '9']]
  val = ['X']
  tests.append(['1', '2', '3',
                'O', 'O', 'O',
                '7', '8', '9'])
  val.append('O')
  tests.append(['1', '2', '3',
                '4', '5', '6',
                'X', 'X', 'X'])
  val.append('X')
  tests.append(['O', '2', '3',
                '4', 'O', '6',
                '7', '8', 'O'])
  val.append('O')
  tests.append(['1', '2', 'X',
                '4', 'X', '6',
                'X', '8', '9'])
  val.append('X')

  for i,v in zip(tests,val):      
    assert winner(i ,players) == v, "Vencedores não estão corretos."
  print("Passou!")

def test_move(move, players):
  board = reset_board()
  test1 = (True, ['X', '2', '3', '4', '5', '6', '7', '8', '9'], 1)
  assert test1 == move(1, 0, board, players), f"O output deveria ser {test1}"
  board = reset_board()
  test2 = (False, ['1', '2', '3', '4', '5', '6', '7', '8', '9'], 0)
  assert test2 == move(10, 0, board, players), f"O output deveria ser {test2}"
  board = reset_board()
  test3 = (True, ['1', 'O', '3', '4', '5', '6', '7', '8', '9'], 0)
  assert test3 == move(2, 1, board, players), f"O output deveria ser {test3}"
  board = reset_board()
  test4 = (False, ['1', 'O', '3', '4', '5', '6', '7', '8', '9'], 1)
  _ = move(2, 1, board, players)
  assert test4 == move(2, 1, board, players), f"O output deveria ser {test4}"
  print("Passou!")