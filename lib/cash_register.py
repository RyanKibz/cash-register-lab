#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self._discount=0
    self.discount = discount
    self.total = 0.0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self,value):
    if isinstance(value,int) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")
  
  def add_item(self,item,price,quantity=1):
    cost = price * quantity
    self.total += cost

    for _ in range(quantity):
      self.items.append(item)

    transaction = {"item": item, "price": price, "quantity": quantity}
    self.previous_transactions.append(transaction)


  def apply_discount(self):
    if self._discount > 0:
      discount_amount = self.total * (self._discount / 100.0)
      self.total -= discount_amount

      formatted_total = int(self.total) if isinstance(self.total, (float,int)) and float(self.total).is_integer() else self.total
      print(f"After the discount, the total comes to ${formatted_total}.")
      return self.total
    else:
      print("There is no discount to apply.")
      return self.total

  def void_last_transaction(self):
    if not self.previous_transactions:
      print("There is no discount to apply.")
      return
    last_tx = self.previous_transactions.pop()
    cost = last_tx["price"] * last_tx["quantity"]
    self.total -= cost
        
    for _ in range(last_tx["quantity"]):
      if last_tx["item"] in self.items:
        self.items.remove(last_tx["item"])

    if not self.items:
      self.total = 0.0