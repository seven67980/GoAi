import json

planes = {
"MiG-29": {
"nation":"USSR",
"br":"12.0",
"speed":"2450 km/h",
"speed_value":2450,
"weapons":"R-73, R-27",
"image":"https://upload.wikimedia.org/wikipedia/commons/6/6c/MiG-29.jpg",
"tip":"Excellent dogfighter with strong missiles."
},

"Su-27": {
"nation":"USSR",
"br":"12.0",
"speed":"2500 km/h",
"speed_value":2500,
"weapons":"R-73, R-27",
"image":"https://upload.wikimedia.org/wikipedia/commons/8/82/Sukhoi_Su-27.jpg",
"tip":"High agility and strong missiles."
},

"F-16": {
"nation":"USA",
"br":"12.0",
"speed":"2400 km/h",
"speed_value":2400,
"weapons":"AIM-9, AIM-120",
"image":"https://upload.wikimedia.org/wikipedia/commons/9/96/F-16_June_2008.jpg",
"tip":"Energy fighting works best."
},

"F-14": {
"nation":"USA",
"br":"11.7",
"speed":"2485 km/h",
"speed_value":2485,
"weapons":"AIM-54 Phoenix",
"image":"https://upload.wikimedia.org/wikipedia/commons/5/56/F-14_Tomcat.jpg",
"tip":"Use long-range missiles."
},

"F-22": {
"nation":"USA",
"br":"12.7",
"speed":"2410 km/h",
"speed_value":2410,
"weapons":"AIM-120, AIM-9",
"image":"https://upload.wikimedia.org/wikipedia/commons/8/83/F-22_Raptor.jpg",
"tip":"Use stealth and supercruise."
},

"Bf 109": {
"nation":"Germany",
"br":"5.7",
"speed":"640 km/h",
"speed_value":640,
"weapons":"20mm cannon",
"image":"https://upload.wikimedia.org/wikipedia/commons/8/86/Bf_109_F-4.jpg",
"tip":"Climb above enemies and boom & zoom."
},

"Fw 190": {
"nation":"Germany",
"br":"5.3",
"speed":"656 km/h",
"speed_value":656,
"weapons":"20mm cannons",
"image":"https://upload.wikimedia.org/wikipedia/commons/2/2d/Fw_190A-8.jpg",
"tip":"Strong firepower and dive speed."
},

"Spitfire": {
"nation":"UK",
"br":"5.7",
"speed":"594 km/h",
"speed_value":594,
"weapons":"20mm Hispano cannons",
"image":"https://upload.wikimedia.org/wikipedia/commons/9/97/Spitfire_Mk_IX.jpg",
"tip":"One of the best turn fighters."
},

"A6M Zero": {
"nation":"Japan",
"br":"4.3",
"speed":"533 km/h",
"speed_value":533,
"weapons":"20mm cannons",
"image":"https://upload.wikimedia.org/wikipedia/commons/9/9d/A6M2_Zero.jpg",
"tip":"Extremely good turn fighter but fragile."
},

"Mirage 2000": {
"nation":"France",
"br":"12.0",
"speed":"2336 km/h",
"speed_value":2336,
"weapons":"Magic II missiles",
"image":"https://upload.wikimedia.org/wikipedia/commons/5/56/Mirage_2000.jpg",
"tip":"Use delta-wing energy tactics."
}

}

with open("planes.json","w") as f:
    json.dump(planes,f,indent=4)

print("planes.json database generated!")
