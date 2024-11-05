from utils import validate_num

def show_menu():
  print("\n--- Ecommnerce ---")
  print("1. Add product")
  print("2. Update product stock")
  print("3. Delete product")
  print("4. Show ecommerce")
  print("5. Exit")
  return validate_num("Select an option: ")

def request_product():
  return input("Insert product name: ")

def request_quantity():
  return validate_num("Quantity: ")
