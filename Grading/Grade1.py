def grade1(recebendo_inputs):
  x,y = recebendo_inputs()  
  if not(type(x) is type(1.)):
    return '#x não está no tipo necessário.\n#Tente novamente. ❌'    
  elif not(type(y) is type(1.)):
    return '#y não está no tipo necessário.\nTente novamente. ❌'    
  else:
    return '#Resposta Correta. ✔️'    

def grade_op(funcao, func2):  
  x, y = [10,1,2,3,4,5] , [7,8,9,10,11,12]  
  for a,b in zip(x,y):    
    test = funcao(a,b) == func2(a,b)      
  
  if test:
   return '#Resposta Correta. ✔️'
    
  else:
    return '#Tente Novamente. ❌'
    

def funcsum(a,b):
  return a+b

def funcsub(a,b):
  return a-b

def funcdiv(a,b):
  return a/b

def funcmul(a,b):
  return a*b


def grade2(funcao):  
  return grade_op(funcao, funcsum)

def grade3(funcao):  
  return grade_op(funcao, funcsub)

def grade4(funcao):  
  return grade_op(funcao, funcdiv)

def grade5(funcao):  
  return grade_op(funcao, funcmul)
