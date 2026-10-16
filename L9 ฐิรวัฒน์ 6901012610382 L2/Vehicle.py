class Vehicle:
    def __init__(self, license_plate, brand, model, year, daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def show_info(self):
        print(f"ทะเบียน: {self.license_plate} | {self.brand} {self.model} "
              f"({self.year}) | ค่าเช่า {self.daily_rate:,.2f} บาท/วัน")

    def calculate_rental_cost(self, days):
        return self.daily_rate * days


class Car(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, seats):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seats = seats

    def show_info(self):
        super().show_info()
        print(f"  ประเภท: รถยนต์นั่ง | จำนวนที่นั่ง: {self.seats}")

    def calculate_rental_cost(self, days):
        cost = super().calculate_rental_cost(days)
        if days >= 5:
            print(f"  โปรโมชั่น: เช่า {days} วัน แถมฟรี 2 วัน (ใช้งานได้ {days + 2} วัน)")
        return cost


class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = payload

    def show_info(self):
        super().show_info()
        print(f"  ประเภท: รถบรรทุก | น้ำหนักบรรทุก: {self.payload:,} กก.")


def load_vehicles(filename):
    vehicles = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            vtype, plate, brand, model, year, rate, extra = line.split(",")
            if vtype == "Car":
                vehicles.append(Car(plate, brand, model, int(year), float(rate), int(extra)))
            elif vtype == "Truck":
                vehicles.append(Truck(plate, brand, model, int(year), float(rate), int(extra)))
    return vehicles


if __name__ == "__main__":
    vehicles = load_vehicles("vehicles.txt")

    for v in vehicles:
        v.show_info()
        for days in (3, 5):
            print(f"  เช่า {days} วัน = {v.calculate_rental_cost(days):,.2f} บาท")
        print()