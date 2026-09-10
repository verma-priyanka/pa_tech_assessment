# Task: List Comprehension & Filtering
# Instructions: Complete the function to return only even IDs 
# greater than 100, sorted in descending order.

# check for even numbers greater than 100
def filter_orders(order_ids):
  even = []
  for i in order_ids:
    if i > 100 and i % 2 == 0:
      even.append(i)
        # return as sorted list
      even.sort(reverse=True)
  return even

# Test Case
test_data = [10, 105, 120, 44, 202, 300, 75, 110]
# Expected Output: [300, 202, 120, 110]
  
print(filter_orders(test_data))
