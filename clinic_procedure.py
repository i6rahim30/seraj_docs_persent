class ClinicProcedure :
    def __init__(self,name,price,spend):
        self.name=name
        self.price=float(price)
        self.paid=0.0
        self.spend=spend