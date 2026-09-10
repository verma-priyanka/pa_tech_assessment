# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    # extract year
  year = data.get("specs", {}).get("model_info", {}).get("year")
  if year is None:
    return "Unknown"
  else:
    return year
    # pass

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))
