from pyscript import document, display

def create_order(e):
    document.getElementById("output2").innerHTML = "" #clear previous result

    prod1=document.getElementById("item1") #get item 1 value
    prod2=document.getElementById("item2") #get item 2 value
    prod3=document.getElementById("item3") #get item 3 value
    prod4=document.getElementById("item4") #get item 4 value
    #Calculate
    subtotal= float(prod1.value) * prod1.checked
    subtotal += float(prod2.value) * prod2.checked
    subtotal += float(prod3.value) * prod3.checked
    subtotal += float(prod4.value) * prod4.checked
    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)
    grandtotal = subtotal + price
    display(grandtotal, target="output2")

def place_order(e):
    document.getElementById("output3").innerHTML = "" #clear previous result

    ice_cream = document.getElementById("ice_cream")
    ice_cream_price = float(ice_cream.value)
    display(ice_cream_price, target="output3")

def show_order(e):
    document.getElementById("output4").innerHTML = ""
    # clears previous result
    prod1=document.getElementById("item1") #get item 1 id
    subtotal= float(prod1.value) * prod1.checked
    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)
    grandtotal = subtotal + price
    ice_cream = document.getElementById("ice_cream")
    ice_cream_price = float(ice_cream.value)
    final_order = grandtotal + ice_cream_price
    display(f'You have to pay a total of {final_order}', target="output4")