
def wholesale_cost(base_cost, copies):
    return discount_cost(base_cost, copies) + shipping_cost(copies)

def discount_cost(base_cost, copies):
    discount = .40
    return (base_cost * (1 - discount) * copies)

def shipping_cost(copies):
    base_shipping = 3.00
    additional_shipping = 0.75
    return base_shipping + additional_shipping * (copies - 1)

print(wholesale_cost(24.95, 1))
print(wholesale_cost(24.95, 2))
print(wholesale_cost(24.95, 350))
print(wholesale_cost(25.95, 1))
print(wholesale_cost(25.95, 2))
print(wholesale_cost(25.95, 350))