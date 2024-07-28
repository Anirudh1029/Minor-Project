import sys
from IamManager import check
from IamManager import wfh_access
import time
from locationexp1 import checkloc
from IamTeamLeader import Alice_Smith
from IamTeamLeader import Bob_Johnson
from IamTeamLeader import Charlie_Brown
from IamTeamLeader import David_Davis
class Employee:
    def __init__(self, employee_id, name, role):
        self.employee_id = employee_id
        self.name = name
        self.role = role


class Team:
    def __init__(self, team_id, leader):
        self.team_id = team_id
        self.leader = leader
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


class Project:
    def __init__(self, project_id, manager):
        self.project_id = project_id
        self.manager = manager
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)


class AccessControlSystem:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def add_employee_to_team(self, team_id, employee):
        for project in self.projects:
            for team in project.teams:
                if team.team_id == team_id:
                    team.add_employee(employee)
                    return True
        return False

    def check_access(self, name, role):
        employee = self.get_employee(name, role)
        if not employee:
            return 0

        # Attribute-based access control (ABAC) logic
        for project in self.projects:
            if project.manager == employee:
                return True
            for team in project.teams:
                if team.leader == employee or employee in team.employees:
                    return True

        return False

    def get_employee(self, name, role):
        for project in self.projects:
            if project.manager.name == name and project.manager.role == role:
                return project.manager
            for team in project.teams:
                if team.leader.name == name and team.leader.role == role:
                    return team.leader
                for employee in team.employees:
                    if employee.name == name and employee.role == role:
                        return employee
        return None

def check_employee_task_access(name,task,access_rights):
    if name in access_rights:
        if task in access_rights[name]:
            return 2
    return 1
def check_employee_resource_access(name,resource,access_rightsER):
    if name in access_rightsER:
        if resource in access_rightsER[name]:
            return 2
    return 1

# Create employees
manager = Employee(1, "John Doe", "project manager")

team_leaders = [
    Employee(2, "Alice Smith", "team leader"),
    Employee(3, "Bob Johnson", "team leader"),
    Employee(4, "Charlie Brown", "team leader"),
    Employee(5, "David Davis", "team leader")
]

employees = [
    # Team 1 employees
    Employee(6, "Employee 1", "employee"),
    Employee(7, "Employee 2", "employee"),
    Employee(8, "Employee 3", "employee"),
    Employee(9, "Employee 4", "employee"),
    Employee(10, "Employee 5", "employee"),

    # Team 2 employees
    Employee(11, "Employee 6", "employee"),
    Employee(12, "Employee 7", "employee"),
    Employee(13, "Employee 8", "employee"),
    Employee(14, "Employee 9", "employee"),
    Employee(15, "Employee 10", "employee"),

    # Team 3 employees
    Employee(16, "Employee 11", "employee"),
    Employee(17, "Employee 12", "employee"),
    Employee(18, "Employee 13", "employee"),
    Employee(19, "Employee 14", "employee"),
    Employee(20, "Employee 15", "employee"),

    # Team 4 employees
    Employee(21, "Employee 16", "employee"),
    Employee(22, "Employee 17", "employee"),
    Employee(23, "Employee 18", "employee"),
    Employee(24, "Employee 19", "employee"),
    Employee(25, "Employee 20", "employee")
]

# Create teams
teams = [
    Team(1, team_leaders[0]),
    Team(2, team_leaders[1]),
    Team(3, team_leaders[2]),
    Team(4, team_leaders[3])
]
teams1=["Employee 1","Employee 2","Employee 3","Employee 4","Employee 5"]
teams2=["Employee 6","Employee 7","Employee 8","Employee 9","Employee 10"]
teams3=["Employee 11","Employee 12","Employee 13","Employee 14","Employee 15"]
teams4=["Employee 16","Employee 17","Employee 18","Employee 19","Employee 20"]
# Assign employees to teams
teams[0].employees.extend(employees[0:5])
teams[1].employees.extend(employees[5:10])
teams[2].employees.extend(employees[10:15])
teams[3].employees.extend(employees[15:20])

access_rights={
    "John Doe":["T1","T2","T3","T4"],
    "Alice Smith":["T1"],
    "Bob Johnson":["T2"],
    "Charlie Brown":["T3"],
    "David Davis":["T4"],
    "Employee 1":["T1"]
}

access_rightsER= {
    "Employee 1":["R1"],
    "Employee 2":["R1"],
    "Employee 3":["R1"],
    "Employee 4":["R2"],
    "Employee 5":["R2"],
    "Employee 6":["R3"],
    "Employee 7":["R3"],
    "Employee 8":["R4"],
    "Employee 9":["R4"],
    "Employee 10":["R3"],
    "Employee 11":["R5"],
    "Employee 12":["R5"],
    "Employee 13":["R5"],
    "Employee 14":["R6"],
    "Employee 15":["R6"],
    "Employee 16":["R7"],
    "Employee 17":["R7"],
    "Employee 18":["R8"],
    "Employee 19":["R8"],
    "Employee 20":["R8"]
}

# Create project
project = Project(1, manager)
project.teams.extend(teams)

# Create access control system
access_control = AccessControlSystem()
access_control.add_project(project)

# Example usage
name = input("Enter your name: ")
role = input("Enter your role: ")

access_granted = access_control.check_access(name, role)
if(access_granted==0):
    print("Not a worker of the Organisation")
    sys.exit()
else:
 lat,long=checkloc()
 if not(lat==17.384 and long == 78.4564):
    aa=input("Are you doing WFH?[Y/N]: ")
    if(aa=="N" or aa=="n"):
        print("Check your location")
        sys.exit()
    elif(aa=="Y" or aa=="y"):
        bb=wfh_access(name)
        if(bb==1):
            cc=input("Can you complete the work in 8hours [Y/N]: ")
            if (cc=='N' or cc=="n"):
                print("WFH is denied")
                sys.exit()
            elif (cc=="y" or cc=="Y"):
                print("WFH is granted!!")
            else:
                print("Wrong input!!")
                sys.exit()
        else:
            print("Not Granted!!")
            sys.exit()
    else:
        print("Wrong Input")
        sys.exit()
 else:
     print("Have a great day at office!!")
 if(access_granted):
    task=input("Enter your Task ID: ")
    if(role=="team leader"):
        if(check_employee_task_access(name,task,access_rights)!=1):
            hh=input("Do you want to access Task of other team [Y/N]: ")
            if(hh=="Y" or hh=="y"):
                task1=input("Enter the Task ID to access: ")
                if(check_employee_task_access(name,task1,access_rights)==1):
                    print("Need to request access from project manager")
                    x=input("Do you want to request [Y/N]: ")
                    if(x=="Y" or x=="y"):
                        y=check(name,task1)
                        if(y==1):
                            access_rights[name].append(task1)
                            print("Access Granted!!")
                            print("Hey Team Leader, you have access to all the resources of this task")
                            time.sleep(5)
                            access_rights[name].remove(task1)
                            print("Hope You have completed the work")
                            sys.exit()
                        else:
                            print("Request Denined!!")
                            sys.exit()
                    elif(x=="N" or x=="n"):
                        print("Exiting")
                        sys.exit()
                    else:
                        print("Invalid input")
                        sys.exit()
                else:
                    print("Access Denied!!")
                    sys.exit()
            elif(hh=="N" or hh=="n"):
                print("Ok Exiting!!")
                sys.exit()
            else:
                print("Invalid Input")
                sys.exit()
        else:
            print("You doesnot belong to this Task")
            sys.exit()
    else:
        if(check_employee_task_access(name,task,access_rights)!=1):
            res=input("Enter the resource ID: ")
            if(check_employee_resource_access(name,res,access_rightsER)==1):
                print("You are not allowed to use this particular resource")
                ss=input("Do you want to request access to teamleader [Y/N]: ")
                if (ss=="Y" or ss=="y" ):
                    if name in teams1:
                        dd=Alice_Smith(name,res)
                        if(dd==1):
                            print("Access Granted!!")
                            time.sleep(5)
                            print("Hope you have completed the work")
                            sys.exit()
                        else:
                            print("Access Denied!!")
                            sys.exit()
                    if name in teams2:
                        dd=Bob_Johnson(name,res)
                        if(dd==1):
                            print("Access Granted!!")
                            time.sleep(5)
                            print("Hope you have completed the work")
                            sys.exit()
                        else:
                            print("Access Denied!!")
                            sys.exit()  
                    if name in teams3:
                        dd=Charlie_Brown(name,res)
                        if(dd==1):
                            print("Access Granted!!")
                            time.sleep(5)
                            print("Hope you have completed the work")
                            sys.exit()
                        else:
                            print("Access Denied!!")
                            sys.exit()               
                    if name in teams4:
                        dd=David_Davis(name,res)
                        if(dd==1):
                            print("Access Granted!!")
                            time.sleep(5)
                            print("Hope you have completed the work")
                            sys.exit()
                        else:
                            print("Access Denied!!")
                            sys.exit()
                elif(ss=="N" or ss=="n"):
                    print("Exiting")
                    sys.exit()
                else:
                    print("Invalid Input")
                    sys.exit()
            else:
                print("Do your work")
                time.sleep(6)
                print("Hope you have completed the work")
                sys.exit()
        else:
            print("Check your Task ID")
 else:
    print("Access not granted!!")
    sys.exit()
