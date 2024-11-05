def validate_num(message):
  while True:
    try:
      return int(input(message))
    except ValueError:
      print("Error: You should insert a number")
