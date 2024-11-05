from ecommerce import add_product, update_product, delete_product, show_ecommerce
from menu import show_menu, request_product, request_quantity


def run_ecommerce():
  while True:
    option = show_menu()
    
    if option == 1:
      product = request_product()
      
      quantity = request_quantity()
      
      add_product(product, quantity)
      
    elif option == 2:
      product = request_product()
      
      quantity = request_quantity()
      
      update_product(product, quantity)
    
    elif option == 3:
      product = request_product()
      
      delete_product(product)
      
    elif option == 4:
      show_ecommerce()
      
    elif option == 5:
      print("Leaving ecommerce...")
      break
    
    else:
      print('Option invalid, Try again...')
      

# Start program

if __name__ == "__main__":
  run_ecommerce()
