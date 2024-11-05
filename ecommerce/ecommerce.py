ecommerce = {}

# Add product

def add_product(product, quantity):
  if product in ecommerce:
    print(f"Product already exists in ecommerce. You can update product stock")
  else:
    ecommerce[product] = quantity
    print(f"Product has been added")


# Update product

def update_product(product, quantity):
  if product in ecommerce:
    ecommerce[product] = quantity
    print(f"{product} stock has been updated")
  else:
    print(f"{product} does not exist. You can add it to ecommerce")
  
    
# Delete product

def delete_product(product):
  if product in ecommerce:
    del(ecommerce[product])
    print(f'{product} was deleted')
  else:
    print(f"{product} does not exist.")
    
    
# Show ecommerce

def show_ecommerce():
  if ecommerce:
    for item, stock in ecommerce.items():
      print(f"{item}: {stock}")
  else:
    print('Ecommerce is empty')
    