from task import actuator
import numpy

j = 0
while j<10:
    a_wanted = numpy.random.randint(-6,6, size=10)
    b_reading = numpy.random.randint(0,5, size=10)
    c_decision = numpy.zeros(10)
    for i in range(len(a_wanted)):
        if a_wanted[i] < 0 or a_wanted[i] > 5:
            a_wanted[i] = 0
        for i in range(len(a_wanted)):
            if b_reading[i] < a_wanted[i]:
                c_decision[i] = 0
            elif b_reading[i] > a_wanted[i]:
                c_decision[i] = 1
            else:
                c_decision[i] = 2
    user = actuator(a_wanted,b_reading,c_decision)
    if user.all() == c_decision.all():
        print("yes")
    j+=1