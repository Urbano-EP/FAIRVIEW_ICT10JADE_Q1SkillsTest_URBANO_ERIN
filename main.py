from pyscript import document, display

def create_order(e):
    document.getElementById("output2").innerHTML = "" #clear previous result

    prod1=document.getElementById("item1") #get item 1 value
    #Calculate
    subtotal= float(prod1.value) * prod1.checked
    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)
    grandtotal = subtotal + price
    display(grandtotal, target="output2")

    
