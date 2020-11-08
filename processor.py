import constant

def pl(var1):
  """
  p1 returns pig latin
  
  parameters
  var1 is the word to latinize
  example:
  pl("howdy")  
  returns: owdayhay
  p1("apple")
  returns: ppleay
  """
  if constant in var1[:1]:
    return  var1 + "ay"
  else:
    return var1[2:] + var1[:1]