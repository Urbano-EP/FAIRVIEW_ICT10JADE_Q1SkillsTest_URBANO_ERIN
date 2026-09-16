from pyscript import document, display

def show_order(e):
    document.getElementById("output4").innerHTML = ""
    # clears previous result
    prod1=document.getElementById("item1") #get item 1 id
    prod2=document.getElementById("item2") #get item 2 id
    prod3=document.getElementById("item3") #get item 3 id
    prod4=document.getElementById("item4") #get item 4 id
    subtotal = (float(prod1.value) * prod1.checked
                + float(prod2.value) * prod2.checked
                + float(prod3.value) * prod3.checked
                + float(prod4.value) * prod4.checked)
    taxrate = 0.12
    tax = subtotal * taxrate
    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)
    grandtotal = subtotal + price + tax
    display(f"Subtotal: {subtotal}.", target="output4")
    display(f"Tax: {tax}.", target="output4", append=True)
    display(f"Total: {grandtotal}.", target="output4", append=True)
    display("Thank you for your order!", target="output4", append=True)