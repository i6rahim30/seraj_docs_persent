from doctor import Doctor
from clinic_procedure import ClinicProcedure

# def calc_pay(cp,doc,pay):
#     if doc.department.dep_name == "general" and cp.name == "check":
#         pers=0.5
#         payment=0
#         unpaid=cp.price*pers
#         if pay > cp.price-cp.paid:
#             pay=cp.price-cp.paid

#         if ( cp.paid*pers) < unpaid :
#             cp.paid+=pay
#             print("The Procedure is less now to : ",cp.price-cp.paid)
#             print("Dr.",doc.name,"has been payed : ",pay*pers)
#         else:
#              print("Paid")

def cut_spend(cp,doc,pay):
    if doc.department.dep_name == "general" and cp.name == "check":
        pers=0.5
        unpaid=0
        print("expensis befor : ",cp.spend)
        if cp.spend >= pay :
            cp.spend -=pay
            print('expensis now : ',cp.spend)
            unpaid=cp.price-pay
            print('unpayed is ',unpaid)
        cp.price=unpaid
        
            
def paid(cp,pay):
    if cp.paid<cp.price:
        if pay >(cp.price-cp.paid):
            cp.paid+=(cp.price-cp.paid)
        else:
            cp.paid+=pay
        return True
    else:
        return False

def check_spend(cp):
    if cp.spend<cp.paid:
        return True
    else:
        return False


def calc_percent(cp,pay):
    old_paid=cp.paid
    if paid(cp,pay) and check_spend(cp):
        percent_doctor=0.5
        old_paid_doctor=0
        old_paid_doctor=(old_paid-cp.spend)*percent_doctor 
        if old_paid_doctor <0 :
            old_paid_doctor=0         
        paid_doctor=abs(cp.paid-cp.spend)
        print((paid_doctor*percent_doctor)-old_paid_doctor)
    else:
        print("can not paid")



cp1=ClinicProcedure("check",500,20)


calc_percent(cp1,22.5)
calc_percent(cp1,13.5)
calc_percent(cp1,13.5)
calc_percent(cp1,0.5)
calc_percent(cp1,58)
calc_percent(cp1,500)











"""
def calc_percent(cp,pay):
    percent_doctor=0.5
    old_paid=(cp.paid-cp.spend)*percent_doctor
    if old_paid <0:
        old_paid=0
   # print(old_paid)
    if paid(cp,pay) and check_spend(cp):
        
        paid_doctor=abs(cp.paid-cp.spend)
        print((paid_doctor*percent_doctor)-old_paid)
    else:
        print("can not paid")

"""