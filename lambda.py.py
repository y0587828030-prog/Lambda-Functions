##step 1
# manager_son_price = lambda price  , is_manager_son : price * 0.8 if is_manager_son else price *1.17
# print(manager_son_price(100, True))

##step 2
# final_price = lambda price, discount : price / 100 *(100 - discount)
# print(final_price(200,10))


# ##step 3
# full_name = lambda first_name, last_name:  f"{first_name} {last_name}"
# print(full_name("yehosh","zaltz"))

##step 4
# grade_status = lambda grade: f"pass" if grade >= 55 else "fail"
# print(grade_status(50))
# print(grade_status(90))

# #step 5
# larger = lambda num1 , num2 : num1 if num1 > num2 else num2
# print(larger(10,5))
# print(larger(10,100))
# print(larger(10,10))
# print(larger(100,10))

# ##step 6
# distance_from_10 = lambda num1 : 10 - num1 if num1 < 10 else num1 - 10
# print(distance_from_10(100))

# ## step 7
item_total = lambda item: item["price"] * item["amount"]

print(item_total({"name": "Pen", "price": 5, "amount": 10}))