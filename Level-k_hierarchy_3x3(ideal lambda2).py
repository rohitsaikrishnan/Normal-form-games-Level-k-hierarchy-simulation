import numpy as np
import matplotlib.pyplot as plt
import math


np.random.seed(60)
def normal_form_game_payoff():

    num=np.random.randint(1,11)
    num1=np.random.randint(1,11)
    num2=np.random.randint(1,11)
    num3 = np.random.randint(1, 11)
    num4 = np.random.randint(1, 11)
    num5 = np.random.randint(1, 11)
    num6 = np.random.randint(1, 11)
    num7 = np.random.randint(1, 11)
    num8 = np.random.randint(1, 11)
    num9 = np.random.randint(1, 11)
    num10 = np.random.randint(1, 11)
    num11 = np.random.randint(1, 11)
    num12 = np.random.randint(1, 11)
    num13 = np.random.randint(1, 11)
    num14 = np.random.randint(1, 11)
    num15 = np.random.randint(1, 11)
    num16 = np.random.randint(1, 11)
    num17 = np.random.randint(1, 11)
    normal_form_game = [[[num,num1],[num2,num3],[num4,num5]],[[num6,num7],[num8,num9],[num10,num11]],[[num12,num13],[num14,num15],[num16,num17]]]
    return normal_form_game




def level_k_probabilities_2(k,player,lamda2=0.56, lamda = 0.05):
    if k==0:
        return (1.0/3.0, 1.0/3.0, 1.0/3.0)
    if player == 0:
        sum_1 = np.exp(
            lamda2 * (level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[0] * normal_form_game_player[0][0][0] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[1] * normal_form_game_player[0][1][0] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[2] * normal_form_game_player[0][2][0]))

        sum_2 = np.exp(
            lamda2 * (level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[0] * normal_form_game_player[1][0][0] +
            level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[1] * normal_form_game_player[1][1][0] +
                level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[2] * normal_form_game_player[1][2][0]))
        sum_3 = np.exp(
            lamda2 * (level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[0] * normal_form_game_player[2][0][0] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[1] * normal_form_game_player[2][1][0] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[2] * normal_form_game_player[2][2][0]))
    else:
        sum_1 = np.exp(
            lamda2 * (level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[0] * normal_form_game_player[0][0][1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[1] * normal_form_game_player[1][0][1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[2] * normal_form_game_player[2][0][1]))

        sum_2 = np.exp(
            lamda2 * (level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[0] * normal_form_game_player[0][1][1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[1] * normal_form_game_player[1][1][1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[2] * normal_form_game_player[2][1][1]))
        sum_3 = np.exp(
            lamda2 * (level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[0] * normal_form_game_player[0][2][1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[1] * normal_form_game_player[1][2][1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2, lamda)[2] * normal_form_game_player[2][2][1]))

    prob1 = sum_1 / (sum_1 + sum_2 + sum_3)
    prob2 = sum_2 / (sum_1 + sum_2 + sum_3)
    prob3 = sum_3 / (sum_1 + sum_2 + sum_3)
    return (prob1, prob2, prob3)

def level_k_probabilities_1(k,player,lamda=0.36):
    if k == 0:
        return (1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0)
    if player == 0:
        sum_1 = np.exp(
            lamda * (level_k_probabilities_1(k - 1, (player + 1) % 2)[0] * normal_form_game_player[0][0][
                0] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[1] * normal_form_game_player[0][1][
                          0] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[2] * normal_form_game_player[0][2][
                          0]))

        sum_2 = np.exp(
            lamda * (level_k_probabilities_1(k - 1, (player + 1) % 2)[0] * normal_form_game_player[1][0][
                0] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[1] * normal_form_game_player[1][1][
                          0] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[2] * normal_form_game_player[1][2][
                          0]))
        sum_3 = np.exp(
            lamda * (level_k_probabilities_1(k - 1, (player + 1) % 2)[0] * normal_form_game_player[2][0][
                0] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[1] * normal_form_game_player[2][1][
                          0] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[2] * normal_form_game_player[2][2][
                          0]))
    else:
        sum_1 = np.exp(
            lamda * (level_k_probabilities_1(k - 1, (player + 1) % 2)[0] * normal_form_game_player[0][0][
                1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[1] * normal_form_game_player[1][0][
                          1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[2] * normal_form_game_player[2][0][
                          1]))

        sum_2 = np.exp(
            lamda * (level_k_probabilities_1(k - 1, (player + 1) % 2)[0] * normal_form_game_player[0][1][
                1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[1] * normal_form_game_player[1][1][
                          1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[2] * normal_form_game_player[2][1][
                          1]))
        sum_3 = np.exp(
            lamda * (level_k_probabilities_1(k - 1, (player + 1) % 2)[0] * normal_form_game_player[0][2][
                1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[1] * normal_form_game_player[1][2][
                          1] +
                      level_k_probabilities_1(k - 1, (player + 1) % 2)[2] * normal_form_game_player[2][2][
                          1]))

    prob1 = sum_1 / (sum_1 + sum_2 + sum_3)
    prob2 = sum_2 / (sum_1 + sum_2 + sum_3)
    prob3 = sum_3 / (sum_1 + sum_2 + sum_3)
    return (prob1, prob2, prob3)

def poisson_distribution(lamda=1.5, no_of_levels=2):
    probabilistic_distribution=[]
    for i in range(no_of_levels+1):
        probabilistic_distribution.append(np.power(lamda, i)*np.exp(-lamda)/float(math.factorial(i)))
    probabilistic_distribution = [i/sum(probabilistic_distribution) for i in probabilistic_distribution]
    return [0,1,0]
def level_0_payoff(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2,lk_probabilities_p):
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(3):
        for j in range(3):
            #Checked
            payoff = payoff + player_probabilities[i] * normal_form_game_player[i][j][0] * (
                        level_0_probabilities[j] * player_distribution[0] + level_1_probabilities[j] *
                        player_distribution[1] + level_2_probabilities[j] * player_distribution[2])
    return payoff
def level_1_payoff(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution=poisson_distribution()
    payoff=0
    for i in range(3):
        for j in range(3):
            payoff = payoff + player_probabilities[i]*normal_form_game_player[i][j][0]*(level_0_probabilities[j]*player_distribution[0]+level_1_probabilities[j]*player_distribution[1]+level_2_probabilities[j]*player_distribution[2])
    return payoff

def level_2_payoff(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(3):
        for j in range(3):
            payoff = payoff + player_probabilities[i] * normal_form_game_player[i][j][0] * (
                        level_0_probabilities[j] * player_distribution[0] + level_1_probabilities[j] *
                        player_distribution[1] + level_2_probabilities[j] * player_distribution[2])
    return payoff

def level_0_payoff_2(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(3):
        for j in range(3):
            payoff = payoff + player_probabilities[j] * normal_form_game_player[i][j][1] * (
                        level_0_probabilities[i] * player_distribution[0] + level_1_probabilities[i] *
                        player_distribution[1] + level_2_probabilities[i] * player_distribution[2])
    return payoff
def level_1_payoff_2(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(3):
        for j in range(3):
            payoff = payoff + player_probabilities[j] * normal_form_game_player[i][j][1] * (
                        level_0_probabilities[i] * player_distribution[0] + level_1_probabilities[i] *
                        player_distribution[1] + level_2_probabilities[i] * player_distribution[2])
    return payoff
def level_2_payoff_2(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(3):
        for j in range(3):
            payoff = payoff + player_probabilities[j] * normal_form_game_player[i][j][1] * (
                        level_0_probabilities[i] * player_distribution[0] + level_1_probabilities[i] *
                        player_distribution[1] + level_2_probabilities[i] * player_distribution[2])
    return payoff
#for i in range(20):
#    payoff=[]
#    payoff2=[]
#    normal_form_game_player = normal_form_game_payoff(2, 7)
#    print(normal_form_game_player)
#    level_0_payoff(normal_form_game_player)
#    level_1_payoff(normal_form_game_player)
#    level_2_payoff(normal_form_game_player)
#    #(normal_form_game_player)
#    level_1_payoff_2(normal_form_game_player)
#    level_2_payoff_2(normal_form_game_player)
#    level = [0, 1, 2]
#    plt.plot(level, payoff, color='r', label='Player-1')
#    plt.plot(level, payoff2, color='blue', label='Player-2')
#    plt.legend()
#    plt.title('Quantal Level-k')
#    plt.axis([0, 4, 0, 10])
#    plt.show()
#    print(payoff)
#    print(payoff2)
print poisson_distribution()
def game_simulation(lamda,lamda2,i):
    lk_probabilities_0p1 = level_k_probabilities_1(0, 0)
    lk_probabilities_1p1 = level_k_probabilities_1(1, 0,lamda)
    lk_probabilities_2p1 = level_k_probabilities_2(2, 0,lamda, lamda)
    lk_probabilities_0p2 = level_k_probabilities_1(0, 1)
    lk_probabilities_1p2 = level_k_probabilities_1(1, 1, lamda)
    lk_probabilities_2p2 = level_k_probabilities_2(2, 1, lamda2, lamda)
    probabilistic_distribution = poisson_distribution()
    print ('\n\n')
    print ('Game', i)
    print ('\n')
    print ('Payoff Matrix\n')
    print (normal_form_game_player[0])
    print (normal_form_game_player[1])
    print (normal_form_game_player[2])
    print ('Player 1')
    print ('Level-0 -->', lk_probabilities_0p1)
    print ('Level-1 -->', lk_probabilities_1p1)
    print ('Level-2 -->',lk_probabilities_2p1)
    payoff_10 = level_0_payoff(lk_probabilities_0p2, lk_probabilities_1p2, lk_probabilities_2p2, lk_probabilities_0p1)
    payoff_11 = level_1_payoff(lk_probabilities_0p2, lk_probabilities_1p2, lk_probabilities_2p2, lk_probabilities_1p1)
    payoff_12 = level_2_payoff(lk_probabilities_0p2, lk_probabilities_1p2, lk_probabilities_2p2, lk_probabilities_2p1)
    payoff_1 = [payoff_10, payoff_11, payoff_12]
    print ('Avg. Payoff -->',payoff_1)
    print ('Player 2')
    print ('Level-0 -->', lk_probabilities_0p2)
    print ('Level-1 -->', lk_probabilities_1p2)
    print ('Level-2 -->', lk_probabilities_2p2)
    payoff_20 = level_0_payoff_2(lk_probabilities_0p1, lk_probabilities_1p1, lk_probabilities_2p1, lk_probabilities_0p2)
    payoff_21 = level_1_payoff_2(lk_probabilities_0p1, lk_probabilities_1p1, lk_probabilities_2p1, lk_probabilities_1p2)
    payoff_22 = level_2_payoff_2(lk_probabilities_0p1, lk_probabilities_1p1, lk_probabilities_2p1, lk_probabilities_2p2)
    payoff_2 = [payoff_20, payoff_21, payoff_22]
    print ('Avg. Payoff -->',payoff_2)
    return payoff_1, payoff_2



level0_p1 = []
level1_p1 = []
level2_p1 = []
tie_p1=[]
level0_p2 = []
level1_p2 = []
level2_p2 = []
tie_p2=[]

normal_form_game_player = []
normal_form_game_player_list = []
for i in range(20):
    normal_form_game_player_list.append(normal_form_game_payoff())
def lamda1_vs_lamda2(lamda):
    lamda2_values = []
    for i in range(20):
        lamda2 = 0
        global normal_form_game_player
        normal_form_game_player = normal_form_game_player_list[i]
        while 1:
            payoff1, payoff2 = game_simulation(lamda, lamda2,i)
            max1 = max(payoff1)
            max2 = max(payoff2)
            if payoff2.index(max2) == 2:
                lamda2_values.append(lamda2)
                break
            lamda2 = lamda2 + 0.01
    return lamda2_values



ind = []
for i in range(20):
    ind.append(str(i+1))
lamda1_vs_lamda2_values=[]
for i in range(3):
    lamda = (i+1) * 0.1
    lamda1_vs_lamda2_values.append(lamda1_vs_lamda2(lamda))
#add tie
print(ind)
plt.plot(ind, lamda1_vs_lamda2_values[0], color='b', label=r'$\lambda_1$ = 0.1')
plt.plot(ind, lamda1_vs_lamda2_values[1], color='r', label=r'$\lambda_1$ = 0.2')
plt.plot(ind, lamda1_vs_lamda2_values[2], label=r'$\lambda_1$ = 0.3')
print ((lamda1_vs_lamda2_values[0][19]))
print ([x for x in range(len(lamda1_vs_lamda2_values[0])) if lamda1_vs_lamda2_values[0][x]>0.105])
print ([x for x in range(len(lamda1_vs_lamda2_values[1])) if lamda1_vs_lamda2_values[1][x] > 0.205])
print ([x for x in range(len(lamda1_vs_lamda2_values[2])) if lamda1_vs_lamda2_values[2][x] > 0.305])
plt.axhline(y=0.1, color = 'brown')
plt.axhline(y=0.2, color = 'brown')
plt.axhline(y=0.3, color = 'brown')
plt.xlabel('Game No.')
plt.ylabel(r'$\lambda_2$ parameter')
plt.legend()
plt.title('optimal $\lambda$ for level-2 (Player-2)')
plt.text(3, 0.31, r'$\lambda_2$=0.3')
plt.text(6, 0.21, r'$\lambda_2$=0.2')
plt.text(10.8, 0.11, r'$\lambda_2$=0.1')
plt.autoscale()
plt.grid()
plt.show()








