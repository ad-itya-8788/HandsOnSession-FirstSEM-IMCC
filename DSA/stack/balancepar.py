def isBalanced(exp):
  stack=[]
  match={'}':'{','(':')','[':']'}
  for ch in exp:
    if ch in '({[':
      stack.push(ch)
    elif ch in ')}]':
      if not stack:
        return False
      if stack.pop()!=match[ch]:
        return False
exp="{[()()]}"
if isBalanced(exp):
  print("Balanced")
else:
  print("Not Balanced")