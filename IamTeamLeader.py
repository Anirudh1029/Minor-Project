def Alice_Smith(name,request_res):
    can_grant={
    "Employee 1":["R2","R3","R5","R7"],
    "Employee 2":["R3","R2","R5","R7"],
    "Employee 3":["R2","R3","R5","R7"],
    "Employee 4":["R1","R4","R6","R8"],
    "Employee 5":["R1","R4","R6","R8"],
    }
    if name in can_grant:
        if request_res in can_grant[name]:
            return 1
    return 0

def Bob_Johnson(name,request_res):
    can_grant={
    "Employee 6":["R2","R3","R5","R7"],
    "Employee 7":["R3","R2","R5","R7"],
    "Employee 8":["R2","R3","R5","R7"],
    "Employee 9":["R1","R4","R6","R8"],
    "Employee 10":["R1","R4","R6","R8"],
    }
    if name in can_grant:
        if request_res in can_grant[name]:
            return 1
    return 0

def Charlie_Brown(name,request_res):
    can_grant={
    "Employee 11":["R2","R3","R5","R7"],
    "Employee 12":["R3","R2","R5","R7"],
    "Employee 13":["R2","R3","R5","R7"],
    "Employee 14":["R1","R4","R6","R8"],
    "Employee 15":["R1","R4","R6","R8"],
    }
    if name in can_grant:
        if request_res in can_grant[name]:
            return 1
    return 0

def David_Davis(name,request_res):
    can_grant={
    "Employee 16":["R2","R3","R5","R7"],
    "Employee 17":["R3","R2","R5","R7"],
    "Employee 18":["R2","R3","R5","R7"],
    "Employee 19":["R1","R4","R6","R8"],
    "Employee 20":["R1","R4","R6","R8"],
    }
    if name in can_grant:
        if request_res in can_grant[name]:
            return 1
    return 0



    