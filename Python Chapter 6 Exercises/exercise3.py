def count():
  word = 'orangutan'
  
  index = len(word) - 1
  
  rvsword = ''
  
  while index >= 0:
    prin = word[index]
    index = index - 1
    rvsword = rvsword + prin
  
  print(rvsword)

count()