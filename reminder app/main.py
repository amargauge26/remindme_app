import time
from plyer import notification
from matplotlib import pyplot as plt
 
def set_hydration_goal():
    goal=int(input("the amount to be drink in a day : "))
    return goal

def t_w_intake():
    total_intake=0
    arr_total_intake=[0]
    arr_time=[0]
    count_time=0
    while True:
        intake = int(input("enter the amount you drink : "))
        total_intake+=intake
        percentage = (total_intake/hydration_goal)*100

        print("total_intake:{:.2f}l  prog:{:.2f}l".format(total_intake,percentage))
        if total_intake>=hydration_goal:

            notification.notify(
                title="****your body needs water - drink water",
                message="congo my boy you have drink enough",
                app_icon="C:\\Users\\AMAR9XD\\OneDrive\\Desktop\\projects\\reminder app\\icon.ico",
                timeout=10
            )
        else:
            notification.notify(
                title="****your body needs water - drink water",
                message="Average body requires at least 3 liters of water daily",
                app_icon="C:\\Users\\AMAR9XD\\OneDrive\\Desktop\\projects\\reminder app\\icon.ico",
                timeout=10
            )
        count_time+=20
        arr_total_intake.append(total_intake)
        arr_time.append(count_time)
                 
        if total_intake>=hydration_goal:
            print("congratulations you have reached the goal of the set time ")
            break
        print("user have been notified")
        time.sleep(10)
    plt.plot(arr_total_intake,arr_time)
    plt.show()
if __name__=="__main__":
    hydration_goal= set_hydration_goal()
    t_w_intake()

