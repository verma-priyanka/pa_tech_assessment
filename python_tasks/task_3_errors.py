# Task: Error Handling & Resilience
# Goal: Calculate a discount safely.

def calculate_discount(price, discount_percent):
  """
    Instructions: Handle cases where discount_percent is 0 
    or if inputs are strings/None. Return 0 for invalid inputs.
    """
  if discount_percent is None or isinstance(discount_percent, str):
    try:
      # handle conversion
      discount_percent = int(discount_percent)
      return discount_percent
    except ValueError:
      return 0
  else:
    discount_percent                        
    return discount_percent
    
    

# Test Case
print(calculate_discount(100, "10")) # Should return 0 or handle conversion
print(calculate_discount(100, 0))    # Should return 0
