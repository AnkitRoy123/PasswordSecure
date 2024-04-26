while True :
  secure = (
    ('a',"@"),
    ('Y',"¥"),
    ('y',"¥"),
    ('and',"&"),
    ('¢',"c"),
    ('s',"$"),
    ('I',"|"),
    ('i',"1"),
    ('l',"!"),
    ('u',"|_|")
  )
  password = str(input("Enter a password for secure the password:\n"))
  def converter(secure):
    for a,b in secure:
      password = password.replace(a,b)
  converter(secure)
