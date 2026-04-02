def apply_discount(price, discount):
    if not isinstance(price,(int, float)):
        return "The price should be a number"
    if not isinstance(discount,(int,float)):
        return "The discount should be a number"  
    if price <= 0:
        return "The price should be greater than 0"
    if discount<0 or discount >100:
        return "The discount should be between 0 and 100"
    final_price = price*(1-discount/100)
    return final_price

print(apply_discount(100,30))
print(apply_discount(300,50))  
print(apply_discount(50,0))  
print(apply_discount(100,100))  
print(apply_discount(25.0, 30.0))
print(apply_discount("g",10)) 
print(apply_discount(250,"d")) 
