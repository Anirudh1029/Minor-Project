def check(name,request_task):
    can_grant={
        "Alice Smith":["T2"],
        "Bob Johnson":["T3"],
        "Charlie Brown":["T1"],
        "David Davis":["T1"],
        "Employee 1":["T2"],
        "Employee 2":["T2"],
        "Employee 3":["T2"],
        "Employee 4":["T2"],
        "Employee 5":["T2"],
        "Employee 6":["T3"],
        "Employee 7":["T3"],
        "Employee 8":["T3"],
        "Employee 9":["T3"],
        "Employee 10":["T3"],
        "Employee 11":["T1"],
        "Employee 12":["T1"],
        "Employee 13":["T1"],
        "Employee 14":["T1"],
        "Employee 15":["T1"],
        "Employee 16":["T1"],
        "Employee 17":["T1"],
        "Employee 18":["T1"],
        "Employee 19":["T1"],
        "Employee 20":["T1"]
    }
    if name in can_grant:
        if request_task in can_grant[name]:
            return 1
    return 0
def wfh_access(name):
    a=["Alice Smith","Bob Johnson","Charlie Brown","David Davis"]
    if name in a:
        return 1
    return 0
