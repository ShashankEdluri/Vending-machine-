# Name : Shashank Edluri 
# Email : sedluri@umass.edu
# Spire ID : 34428126
class VendingMachine:
    def __init__(self):
        self.num = {}
        self.item = []
        self.cost = {}
        self.customer_balance = 0.0
        self.total_sales = 0.0
        self.transactions = 0
        self.names = []
        self.prices = []
    def list_items(self):
        if len(self.item) == 0:
            print ("No items in the vending machine")
        else:
            print("Available items:")
            for x in sorted(self.item):
                print(f'{x} (${self.cost[x]}): {self.num[x]} available')
    def add_item(self, name, price, quantity):
        if name in self.item:
            self.num[name]+=quantity
            self.cost[name] = price
        elif name not in self.item:
            self.num[name] = quantity
            self.cost[name] = price
            self.item.append(name)
        print(f'{quantity} {name}(s) added to inventory')
    def insert_money(self, dollar):
        acceptable_list = [1.0,2.0,3.0]
        if dollar in acceptable_list:
            self.customer_balance += dollar
            print(f'Balance: {self.customer_balance}')
        else:
            print("Invalid amount")
    def purchase(self, name):
        if name not in self.item:
            print("Invalid item")
        elif self.num[name] == 0:
            print(f'Sorry {name} is out of stock')
        elif self.customer_balance < self.cost[name]:
            print(f'Insufficient balance. Price of {name} is {self.cost[name]}')
        else:
            self.num[name] -= 1
            self.customer_balance -= self.cost[name]
            self.total_sales += self.cost[name]
            print(f'Purchased {name}\nBalance: {self.customer_balance}')
            self.transactions += 1
            self.names.append(name)
            self.prices.append(self.cost[name])            
    def display_change(self):
        if self.customer_balance == 0:
            print("No change")
        else:
            print(f"Change: {self.customer_balance}")
            self.customer_balance = 0
    def get_item_price(self,name):
        if name in self.item:
            return (self.cost[name])
        elif name not in self.item:
            print("Invalid item")
    def empty_inventory(self):
        self.item = []
        self.cost = {}
        self.num = {}
        print ("Inventory cleared")
    def get_total_sales(self):
        return round(self.total_sales,2)
    def get_item_quantity(self, name):
        if name in self.item:
            return self.num[name]
        elif name not in self.item:
            print("Invalid item")
    def remove_item(self, name):
        if name in self.item:
            self.item.remove(name)
            self.num.pop(name)
            self.cost.pop(name)
            print (f'{name} removed from inventory')
        elif name not in self.item:
            print ("Invalid item")
    def stats(self, n):
        snacks = []
        total_sales = {}
        cost_gained = {}
        sales_history = 0
        if self.transactions == 0:
            print("No sale history in the vending machine")
        elif n <= len(self.names):
            print (f'Sale history for the most recent {n} purchase(s):')
            for x in range(len(self.names)-1, (len(self.names)-n)-1, -1):
                if self.names[x] not in snacks:
                    snacks.append(self.names[x])
                    total_sales[self.names[x]] = 1
                    cost_gained[self.names[x]] = self.prices[x]
                elif self.names[x] in snacks:
                    total_sales[self.names[x]] += 1        
                    cost_gained[self.names[x]] += self.prices[x] 
            for x in sorted(snacks):
                print (f'{x}: ${cost_gained[x]} for {total_sales[x]} purchase(s)')
        elif n > len(self.names):
            print (f'Sale history for the most recent {len(self.names)} purchase(s):')
            for x in range(len(self.names)-1, -1, -1):
                if self.names[x] not in snacks:
                    snacks.append(self.names[x])
                    total_sales[self.names[x]] = 1
                    cost_gained[self.names[x]] = self.prices[x]
                elif self.names[x] in snacks:
                    total_sales[self.names[x]] += 1        
                    cost_gained[self.names[x]] += self.prices[x]      
            for x in sorted(snacks):
                print (f'{x}: ${cost_gained[x]} for {total_sales[x]} purchase(s)')

        
        


    



            



# Create a new vending machine
vending_machine = VendingMachine()

# Add some items to the inventory
vending_machine.add_item('Soda', 1.50, 5)
vending_machine.add_item('Chips', 0.75, 10)
vending_machine.add_item('Candy', 0.50, 15)

# Show the available items
vending_machine.list_items()

# Insert some coins
vending_machine.insert_money(1.00)
vending_machine.insert_money(1.00)

# Purchase an item
vending_machine.purchase('Soda')

# Get the price of an item
print(vending_machine.get_item_price('Chips'))

# Purchase another item
vending_machine.purchase('Chips')

# Get the total sales
print(vending_machine.get_total_sales())

# Insert some coins
vending_machine.insert_money(3.00)
vending_machine.insert_money(3.00)
vending_machine.insert_money(3.00)

# Purchase another item
vending_machine.purchase('Chips')
vending_machine.purchase('Chips')
vending_machine.purchase('Chips')
vending_machine.purchase('Candy')
vending_machine.purchase('Candy')

# print stats
vending_machine.stats(3)
vending_machine.stats(5)
vending_machine.stats(10)

# Remove an item
vending_machine.remove_item('Candy')

# Show the available items again
vending_machine.list_items()

# Get the quantity of an item
print(vending_machine.get_item_quantity('Gum'))

# Empty the inventory
vending_machine.empty_inventory()

# Show the available items again
vending_machine.list_items()
