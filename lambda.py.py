##step 1
# manager_son_price = lambda price  , is_manager_son : price * 0.8 if is_manager_son else price *1.17
# print(manager_son_price(100, True))

##step 2
final_price = lambda price, discount : price / 100 *(100 - discount)
print(final_price(200,10))


# fn = lambda price: price * 0.9 if price >= 100 else price 
# print(fn(99))