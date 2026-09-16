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

def place_order(e):
    document.getElementById("output3").innerHTML = "" #clear previous result

    coffee = document.getElementById("coffee")
    coffee_price = float(coffee.value)
    display(coffee_price, target="output3")

def show_order(e):
    document.getElementById("output4").innerHTML = ""
    # clears previous result
    prod1=document.getElementById("item1") #get item 1 id
    subtotal= float(prod1.value) * prod1.checked
    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)
    grandtotal = subtotal + price
    coffee = document.getElementById("coffee")
    coffee_price = float(coffee.value)
    final_order = grandtotal + coffee_price
    display(f'You have to pay a total of {final_order}', target="output4")