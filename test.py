import os

# Check 1: HTML file exists
assert os.path.exists("index.html"), "index.html does not exist"

# Read HTML
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read().lower()

# Required elements
required_elements = [
    "<form",
    'id="name"',
    'id="email"',
    'id="phone"',
    'id="course"',
    'id="address"',
    'type="submit"'
]

# Check required elements
for element in required_elements:
    assert element in html, f"Missing required element: {element}"

print("All tests passed!")