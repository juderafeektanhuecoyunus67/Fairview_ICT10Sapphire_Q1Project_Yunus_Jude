"""
Main calculation logic for Coffee Shop Receipt Generator & SKU Generator.
Grade 10 ICT 1st Quarter PyScript Project.
PEP 8 Compliant without using if statements.
"""

from pyscript import document

# ==========================================
# 1. Start of Receipt Generator (index.html)
# ==========================================


def generate_order(e):
    """Calculates coffee shop receipt values directly from inputs."""
    # Fetching item elements
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")

    # Multiplication by checked status (True=1, False=0) avoids using 'if' statements
    cost1 = float(prod1.value) * prod1.checked
    cost2 = float(prod2.value) * prod2.checked
    cost3 = float(prod3.value) * prod3.checked
    cost4 = float(prod4.value) * prod4.checked
    cost5 = float(prod5.value) * prod5.checked

    # Basic arithmetic calculations (PEMDAS)
    sumtotal = cost1 + cost2 + cost3 + cost4 + cost5
    tax = sumtotal * 0.12
    grand_total = sumtotal + tax

    # Formatting receipt HTML string output
    receipt_html = f"<p>Sumtotal: ₱{sumtotal:.2f}</p>"
    receipt_html += f"<p>Tax: ₱{tax:.2f}</p>"
    receipt_html += f"<p><b>Sum/Total:</b> ₱{grand_total:.2f}</p>"

    # Display result directly to target container
    document.getElementById("output1").innerHTML = receipt_html

# ==========================================
# End of Receipt Generator (index.html)
# ==========================================





# ==========================================
# 2. SKU Generator (sku.html)
# ==========================================


def generate_sku(e):
    """Generates SKU string using basic slicing and formatting."""
    # Reading input strings directly from DOM elements
    category = document.getElementById("cat_input").value
    product_name = document.getElementById("prod_input").value
    stock_qty = document.getElementById("qty_input").value

    # Basic string slicing (First 3 characters converted to uppercase)
    cat_code = category[0:3].upper()
    prod_code = product_name[0:3].upper()

    # Assembling final SKU code format (e.g., PER-BOT-50)
    sku_code = f"{cat_code}-{prod_code}-{stock_qty}"

    # Output string to screen
    sku_html = f"<p>Generated Code:</p><p><b>{sku_code}</b></p>"
    document.getElementById("sku_output").innerHTML = sku_html

# ==========================================
# End of SKU Generator (sku.html)
# ==========================================