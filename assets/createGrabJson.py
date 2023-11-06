import json
import sys

# sys.path.append("assets")

def create_location_address(data, key, value):
    def create_location_api(data, key):
        data["Locations_id"][key] = f"Ride to {key} in saved places, double tap to select"
    create_location_api(data, key)
    data["Locations_address"][key] = value
    return data

with open("./assets/GRAB.json", "r") as f:
    data = json.load(f)
    create_location_address(data,"HCMUS", "227 Nguyễn Văn Cừ, Phường 4, Quận 5, TP HCM")
    create_location_address(data,"MyHome", "A11/13A Qu\u1ed1c L\u1ed9 50, X.B\u00ecnh H\u01b0ng, H.B\u00ecnh Ch\u00e1nh, H\u1ed3 Ch\u00ed Minh, Vietnam")
    create_location_address(data,"MyCafe", "57 Võ Oanh, Phường 25, Quận Bình Thạnh, TP. HCM")
    create_location_address(data,"TSN_IAP", "Trường Sơn, Phường 2, Quan Tân Bình, TP HCM")
    create_location_address(data,"NgHueRoad", "22 Nguyễn Huệ, Phường Bến Nghé, Quận 1, TP HCM")



    
with open("./assets/GRAB.json", "w") as f:
    f.write(json.dumps(data, indent=4))