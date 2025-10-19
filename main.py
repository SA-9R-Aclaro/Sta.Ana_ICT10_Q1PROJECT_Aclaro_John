from pyscript import display, document
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "ULTIMATE F1 CARS"
owner_name = "Tristan Aclaro"

# Integer data type
year_since = 2025

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
product_names = ["MCLAREN", "REDBULL", "WILLIAMS"]
beverages = ["MERCEDES", "SAUBER"]

# Tuple data type
business_hours = ("11:00 AM", "10:00 PM")


menu = {
    "MCLAREN": 650000000,
    "REDBULL": 500000000,
    "WILLIAMS": 100.00,
    "MERCEDES": 500000000,
    "SAUBER": 250000000,

}

# Set data type
common_allergens = {"gluten", "dairy", "nuts"}


document.getElementById("name1").innerText = restaurant_name
document.getElementById("owner").innerText = f"Owner: {owner_name}"
document.getElementById("since").innerText = f"Since {year_since}"
document.getElementById("heading1").innerText = "Menu Pricelist"


document.getElementById("prod1").innerText = product_names[0]
document.getElementById("price1").innerText = f"₱{menu['MCLAREN']:,.2f}"
document.getElementById("prod2").innerText = product_names[1]
document.getElementById("price2").innerText = f"₱{menu['REDBULL']:,.2f}"
document.getElementById("prod3").innerText = product_names[2]
document.getElementById("price3").innerText = f"₱{menu['WILLIAMS']:,.2f}"
document.getElementById("prod4").innerText = beverages[0]
document.getElementById("price4").innerText = f"₱{menu['MERCEDES']:,.2f}"
document.getElementById("prod5").innerText = beverages[1]
document.getElementById("price5").innerText = f"₱{menu['SAUBER']:,.2f}"

document.getElementById("openingHours").innerText = f"Open: {business_hours[0]} - {business_hours[1]}"


#
document.getElementById("orderType").innerText = "Dine-in & Takeout Available"
