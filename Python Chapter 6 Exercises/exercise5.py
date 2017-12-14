str = 'X-DSPAM-Confidence:0.8475'

index = str.find(':') + 1

number = ''

while index < len(str):
  port = str[index]
  index = index + 1
  number = number + port
print(float(number))