from pyscript import document, display

def create_order(e):
    document.getElementById("output2").innerHTML = "" #clear previous result

    prod1=document.getElementById("item1") #get item 1 value
    prod2=document.getElementById("item2") #get item 2 value
    prod3=document.getElementById("item3") #get item 3 value
    prod4=document.getElementById("item4") #get item 4 value
    #Calculate
    subtotal = (float(prod1.value) * prod1.checked
                + float(prod2.value) * prod2.checked
                + float(prod3.value) * prod3.checked
                + float(prod4.value) * prod4.checked)
    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)
    grandtotal = subtotal + price
    display(grandtotal, target="output2")

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
    display(f'You have to pay a total of {grandtotal}', target="output4")