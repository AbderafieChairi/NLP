from chatbot import Intent,Entity,DEntity
device = Entity("device",[
    "phone",
    "laptop",
    "tablet",
    "camera",
    "smartphone",
    "laptop",
    "digital camera"
])
Entity.add_to_pipeline()

entry = Intent("ask_for_device",[
    "I want to buy a phone and camera",
    "do you have a laptop ?",
    "Do you carry smartphones ?",
    "Can I find laptops ?",
    "Do you sell digital cameras ?",
    "Do you offer phone for sale?",
],
[   "Absolutely, we have a variety of $devices to choose from, do you want some ?"]
,required_entities=[device])

ask_nbr=Intent("ask_nbr",[
    "I want 5 laptops",
    "I want 5",
    "I need 10 cameras",
    "I would have 10",
    "7",

],[
    f"sure we have $CARDINAL",
],required_entities=[DEntity("CARDINAL")])



msg = "have you a phone?"
print(msg)
print("chatbot :"+entry.parse(msg))
msg2 = "I would have 3"
print(msg2)
print("chatbot :"+ask_nbr.parse(msg2))
