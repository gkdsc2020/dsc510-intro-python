# DSC510
# Week 11
# Programming Assignment - 11.1
# Author: Ganesh Kale
# Date: 02/28/2021
# The purpose of this program is to  implement OOPs concept by creating cash register program

import locale


class CashRegister:

    def __init__(self):
        self.total = 0
        self.item_count = 0

    def addItem(self, price):
        self.price = price
        self.item_count += 1
        self.total += self.price

    # getter method to get total amount
    @property
    def getTotal(self):
        return self.total

    # getter method to get the total items count
    @property
    def getCount(self):
        return self.item_count

    # getter method to empty cart
    @property
    def empty_cart(self):
        self.item_count = 0
        self.total = 0


def main():

    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')   # set locale to format number to currency

    print('*'*35)
    print('   Welcome to the AtoZ store!!!')
    print('*'*35)
    print('Please start adding Items in the cart')
    print('You can enter "q" to Quit or "c" to Clear the cart and Start Over Any Time!!')

    message = 'Please enter price to add item in the cart [q:Quit or c:Clear]: \n'

    cr = CashRegister()   # created object or instance of CashRegister class

    try:
        while True:
            price = input(message)
            if price == "q":
                if cr.getCount > 0:
                    print(f'Your Total Items in the Cart: {cr.getCount}')
                    print(f'Your cart Total is: {locale.currency(cr.getTotal,grouping = True)}')
                    print('Thank you for shopping with us!!')
                    print('See you again!!!')
                    break
                else:
                    print('Thank you for shopping with us!!')
                    print('See you again!!!')
                    break

            elif price == 'c':
                if cr.getCount > 0:
                    cr.empty_cart
                    print('Your Cart is empty now!!')
                else:
                    print('Please add items to the cart to clear')

            elif price == '0':
                print('Please enter valid price greater than 0 !!')

            elif float(price) > 0.0:
                cr.addItem(float(price))
                print(f'You have {cr.getCount} items in you cart.')
                print(f'Your Cart Total is: {locale.currency(cr.getTotal,grouping = True)}')

            else:
                print('Please enter valid price greater than 0 or enter "q" to quit and "c" to Clear the cart')

    except Exception as err:
        print('Thank you for visiting out store. The entered price is not valid price because: ', err)
        print('Please Start Over by entering valid price greater than 0')


if __name__ == "__main__":
    main()
