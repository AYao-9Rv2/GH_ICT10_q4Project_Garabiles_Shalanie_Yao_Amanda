from pyscript import display
import numpy as np
import matplotlib.pyplot as plt
from js import document

classmates = []

def add_classmate(*args):

    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    if name == "" or section == "" or subject == "":
        return

    classmates.append(
        f"Hii! I am {name} from {section}, and my fav subject is {subject}!"
    )

    output = ""

    for c in classmates:
        output += f"<div class='card-box'>{c}</div>"

    document.getElementById("output-list").innerHTML = output

    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""


days = np.array(["Mon","Tue","Wed","Thu","Fri"])
absences = np.array([0,0,0,0,0])


def add_attendance(*args):

    global absences

    day = document.getElementById("day").value
    val = document.getElementById("absence").value

    if val == "":
        return

    val = int(val)

    idx = np.where(days == day)[0][0]
    absences[idx] = val

    plt.figure()
    plt.plot(days, absences, marker="o")
    plt.title("Attendance Tracker")
    plt.xlabel("Days")
    plt.ylabel("Absences")

    display(plt, target="output-graph")
    plt.close()

    document.getElementById("absence").value = ""