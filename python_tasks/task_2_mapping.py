# Task: Dictionary Frequency Mapping
# Instructions: Return a dictionary where keys are categories 
# and values are the count of occurrences.
from collections import Counter

# list to dictionary with counts for each item
def count_categories(categories):
  counts_counter = Counter(categories)
  # return as dictionary
  return dict(counts_counter)
    # pass

# Test Case
data = ['Brakes', 'Engine', 'Brakes', 'Tools', 'Engine', 'Brakes']
# Expected: {'Brakes': 3, 'Engine': 2, 'Tools': 1}
print(count_categories(data))
