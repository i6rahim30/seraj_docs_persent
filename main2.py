from doctor import Doctor
from clinic_procedure import ClinicProcedure

def calc_pay(cp,doc,pay):
    if doc.department.dep_name == "general" and cp.name == "check":
        pers=0.5
        payment=0
        unpaid=cp.price*pers
        if pay > cp.price-cp.paid:
            pay=cp.price-cp.paid

        if ( cp.paid*pers) < unpaid :
            cp.paid+=pay
            print("The Procedure is less now to : ",cp.price-cp.paid)
            print("Dr.",doc.name,"has been payed : ",pay*pers)
        else:
             print("Paid")
        

cp1=ClinicProcedure("check",50)

doc1=Doctor("ahmed","general")

pay=21
calc_pay(cp1,doc1,pay)

pay=4
calc_pay(cp1,doc1,pay)

pay=12
calc_pay(cp1,doc1,pay)

pay=11
calc_pay(cp1,doc1,pay)

pay=2
calc_pay(cp1,doc1,pay)