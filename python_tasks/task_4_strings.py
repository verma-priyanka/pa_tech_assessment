# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    x = sku_string.split("-")
    x = sku_string.replace("-", " ")
    x = ''.join(x)
    x = x.title()
    return x
    # TODO: Implement logic
    # pass

# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"

print (format_sku("brake-pads-ceramic"))
print(format_sku("engine-oil-10w30"))
