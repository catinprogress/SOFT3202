# from abc import ABC, abstractmethod

# # Step 1: Create a Component Interface
# class Coffee(ABC):
#     @abstractmethod
#     def cost(self):
#         pass
    
#     @abstractmethod
#     def description(self):
#         pass

# # Step 2: Create a Concrete Component
# class SimpleCoffee(Coffee):
#     def cost(self):
#         return 5  # Base price
    
#     def description(self):
#         return "Simple Coffee"

# # Step 3: Create an Abstract Decorator
# class CoffeeDecorator(Coffee):
#     def __init__(self, coffee: Coffee):
#         self._coffee = coffee  # Wraps the component

#     def cost(self):
#         return self._coffee.cost()

#     def description(self):
#         return self._coffee.description()

# # Step 4: Create Concrete Decorators
# class MilkDecorator(CoffeeDecorator):
#     def cost(self):
#         return self._coffee.cost() + 2  # Adding milk cost

#     def description(self):
#         return self._coffee.description() + ", Milk"

# class SugarDecorator(CoffeeDecorator):
#     def cost(self):
#         return self._coffee.cost() + 1  # Adding sugar cost

#     def description(self):
#         return self._coffee.description() + ", Sugar"

# # Step 5: Usage Example
# coffee = SimpleCoffee()
# print(coffee.description(), "-> $", coffee.cost())

# coffee_with_milk = MilkDecorator(coffee)
# print(coffee_with_milk.description(), "-> $", coffee_with_milk.cost())

# coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
# print(coffee_with_milk_and_sugar.description(), "-> $", coffee_with_milk_and_sugar.cost())


# Using yield
def show_numbers_yield(max):
    for i in range(1, max+1):
        yield i

# Yield approach - returns an iterator
numbers = show_numbers_yield(5)
# Nothing is printed yet

# We can now use the iterator
for num in numbers:
    print(num)
# Output: 1 2 3 4 5

# Or we can convert to a list
numbers_list = list(show_numbers_yield(5))
print(numbers_list)
# Output: [1, 2, 3, 4, 5]
