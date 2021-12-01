import numpy as np
import matplotlib.pyplot as plt
import math
import collections
import functools
np.random.seed(60)
def normal_form_game_payoff(n):
    normal_form_game = []
    for i in range(n):
        temp1 = []
        for j in range(n):
            temp2 = []
            for k in range(2):
                num = np.random.rand()
                temp2.append(num)
            temp1.append(temp2)
        normal_form_game.append(temp1)
    return normal_form_game



def level_k_probabilities_1(k,player,lamda=0.56, lamda2 = 0.05):
    n=len(normal_form_game_player)
    if k == 0:
        probs=[]
        for i in range(n):
            probs.append((1.0/n))
        probs=tuple(probs)
        return probs
    lk_k = level_k_probabilities_1(k - 1, (player + 1) % 2, lamda, lamda2)
    if player == 0:
        sum_action=[]
        for i in range(n):
            temp_sum = 0
            for j in range(n):
                temp_sum = temp_sum + lk_k[j] * normal_form_game_player[i][j][0]
            temp_sum = np.exp(lamda * temp_sum)
            sum_action.append(temp_sum)
        probs=[]
        for i in range(n):
            temp_prob = sum_action[i]/sum(sum_action)
            probs.append(temp_prob)
        probs=tuple(probs)
        return probs
    else:
        sum_action = []
        for i in range(n):
            temp_sum = 0
            for j in range(n):
                temp_sum = temp_sum + lk_k[j] * \
                           normal_form_game_player[j][i][1]
            temp_sum = np.exp(lamda * temp_sum)
            sum_action.append(temp_sum)
        probs = []
        for i in range(n):
            temp_prob = sum_action[i] / sum(sum_action)
            probs.append(temp_prob)
        probs = tuple(probs)
        return probs

def level_k_probabilities_2(k,player,lamda=0.36):
    n=len(normal_form_game_player)
    if k == 0:
        probs=[]
        for i in range(n):
            probs.append((1.0/n))
        probs=tuple(probs)
        return probs
    if player == 0:
        sum_action=[]
        for i in range(n):
            temp_sum = 0
            for j in range(n):
                temp_sum = temp_sum + level_k_probabilities_1(k-1, (player+1) % 2)[j] * normal_form_game_player[i][j][0]
            temp_sum = np.exp(lamda * temp_sum)
            sum_action.append(temp_sum)
        probs=[]
        for i in range(n):
            temp_prob = sum_action[i]/sum(sum_action)
            probs.append(temp_prob)
        probs=tuple(probs)
        return probs
    else:
        sum_action = []
        for i in range(n):
            temp_sum = 0
            for j in range(n):
                temp_sum = temp_sum + level_k_probabilities_1(k - 1, (player + 1) % 2)[j] * \
                           normal_form_game_player[j][i][1]
            temp_sum = np.exp(lamda * temp_sum)
            sum_action.append(temp_sum)
        probs = []
        for i in range(n):
            temp_prob = sum_action[i] / sum(sum_action)
            probs.append(temp_prob)
        probs = tuple(probs)
        return probs
def poisson_distribution(lamda=50, no_of_levels=100):
    probabilistic_distribution=[]
    for i in range(no_of_levels+1):
        probabilistic_distribution.append(np.power(lamda, i)*np.exp(-lamda)/float(math.factorial(i)))
    probabilistic_distribution = [i/sum(probabilistic_distribution) for i in probabilistic_distribution]
    return_obj = [0.3333,0.3333, 0.3333]
    dist = [0,0,0,0,0,0,0,0,0,0,1,0]
    return dist

def level_k_payoff(level, total_levels, lamda):
    n=len(normal_form_game_player)
    player_probabilities = level_k_probabilities_1(level,0,lamda,lamda)
    level_k_probabilities = []
    for l in range(total_levels):
        level_k_probabilities.append(level_k_probabilities_1(l,1,lamda,lamda))
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(n):
        for j in range(n):
            for l in range(total_levels):#Checked
                payoff = payoff + player_probabilities[i] * normal_form_game_player[i][j][0] * (
                        level_k_probabilities[l][j] * player_distribution[l] )
    return payoff
def level_0_payoff(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2,lk_probabilities_p):
    n=len(normal_form_game_player)
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(n):
        for j in range(n):
            #Checked
            payoff = payoff + player_probabilities[i] * normal_form_game_player[i][j][0] * (
                        level_0_probabilities[j] * player_distribution[0] + level_1_probabilities[j] *
                        player_distribution[1] + level_2_probabilities[j] * player_distribution[2])
    return payoff
def level_1_payoff(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
    n=len(normal_form_game_player)
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution=poisson_distribution()
    payoff=0
    for i in range(n):
        for j in range(n):
            payoff = payoff + player_probabilities[i]*normal_form_game_player[i][j][0]*(level_0_probabilities[j]*player_distribution[0]+level_1_probabilities[j]*player_distribution[1]+level_2_probabilities[j]*player_distribution[2])
    return payoff

def level_2_payoff(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
    n=len(normal_form_game_player)
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(n):
        for j in range(n):
            payoff = payoff + player_probabilities[i] * normal_form_game_player[i][j][0] * (
                        level_0_probabilities[j] * player_distribution[0] + level_1_probabilities[j] *
                        player_distribution[1] + level_2_probabilities[j] * player_distribution[2])
    return payoff

def level_0_payoff_2(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
    n=len(normal_form_game_player)
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(n):
        for j in range(n):
            payoff = payoff + player_probabilities[j] * normal_form_game_player[i][j][1] * (
                        level_0_probabilities[i] * player_distribution[0] + level_1_probabilities[i] *
                        player_distribution[1] + level_2_probabilities[i] * player_distribution[2])
    return payoff
def level_1_payoff_2(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
    n=len(normal_form_game_player)
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(n):
        for j in range(n):
            payoff = payoff + player_probabilities[j] * normal_form_game_player[i][j][1] * (
                        level_0_probabilities[i] * player_distribution[0] + level_1_probabilities[i] *
                        player_distribution[1] + level_2_probabilities[i] * player_distribution[2])
    return payoff
def level_2_payoff_2(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
    n=len(normal_form_game_player)
    player_probabilities = lk_probabilities_p
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff = 0
    for i in range(n):
        for j in range(n):
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
def game_simulation(lamda):
    n = len(normal_form_game_player)
    lk_probabilities_0p1 = level_k_probabilities_1(0, 0)
    lk_probabilities_1p1 = level_k_probabilities_1(1, 0,lamda)
    lk_probabilities_2p1 = level_k_probabilities_1(2, 0,lamda, lamda)
    lk_probabilities_0p2 = level_k_probabilities_1(0, 1)
    lk_probabilities_1p2 = level_k_probabilities_1(1, 1, lamda)
    lk_probabilities_2p2 = level_k_probabilities_1(2, 1, lamda, lamda)
    probabilistic_distribution = [0,0,1]
    print ('\n\n')
    print ('Game', i)
    print ('\n')
    print ('Payoff Matrix\n')
    for k in range(n):
        print (normal_form_game_player[k])
    print ('Player 1')
    print ('Level-0 -->', lk_probabilities_0p1)
    print ('Level-1 -->', lk_probabilities_1p1)
    print ('Level-2 -->',lk_probabilities_2p1)
    payoff_1 = []
    for l in range(12):
        payoff_1.append(level_k_payoff(l,12,lamda))
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




def main():
    n=int(input("enter game size:"))
    level0_p1 = []
    level1_p1 = []
    level2_p1 = []
    tie_p1 = []
    level0_p2 = []
    level1_p2 = []
    level2_p2 = []
    tie_p2 = []

    for j in range(10):
        lamda = (j + 1) * 0.1
        winners1 = []
        winners2 = []
        level_1_wins = 0
        for i in range(20):
            normal_form_game_player = normal_form_game_payoff(n)
            payoff1, payoff2 = game_simulation(lamda)
            max1 = max(payoff1)
            max2 = max(payoff2)
            payoff_1set = set(payoff1)
            payoff_2set = set(payoff2)
            if len(payoff_1set) == 3:
                winners1.append(payoff1.index(max1))
            else:
                winners1.append(999)
            if len(payoff_2set) == 3:
                winners2.append(payoff2.index(max2))
            else:
                winners2.append(999)
        level0_p1.append(winners1.count(0) * 5)
        level1_p1.append(winners1.count(1) * 5)
        level2_p1.append(winners1.count(2) * 5)
        tie_p1.append(winners1.count(999) * 5)
        level0_p2.append(winners2.count(0) * 5)
        level1_p2.append(winners2.count(1) * 5)
        level2_p2.append(winners2.count(2) * 5)
        tie_p2.append(winners2.count(999) * 5)

    ind = np.arange(10)
    # add tie
    print(ind)
    width = 0.8 / 4
    plt.bar(ind, tie_p1, width, label='tie', color='k')
    plt.bar(ind + width, level0_p1, width, label='level-0', color='green')
    plt.bar(ind + 2 * width, level1_p1, width, label='level-1', color='purple')
    plt.bar(ind + 3 * width, level2_p1, width, label='level-2', color='r')

    plt.xlabel(r'$\lambda_1$ & $\lambda_2$ parameter')
    plt.ylabel('Win%')
    plt.title(r'Win% for different values of $\lambda_1$ & $\lambda_2$ (Player 1)')
    plt.grid()
    plt.xticks(ind + width, ('0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0'))
    plt.text(2.8, 78, r'$\lambda_1$ = $\lambda_2$')
    plt.legend(loc='upper right')
    plt.show()
    print
    level_k_probabilities_1(1, 0)
    print
    len(normal_form_game_payoff(3))
if __name__ == "__main__":
    level0_p1 = []
    level1_p1 = []
    level2_p1 = []
    tie_p1 = []
    level0_p2 = []
    level1_p2 = []
    level2_p2 = []
    tie_p2 = []
    winner_level1_proportion = []
    avg_payoff1 = []
    avg_payoff2 = []
    for j in range(1):
        total_payoff1=0
        total_payoff2=0
        lamda = 50
        winners1 = []
        winners2 = []
        winner_level1 = 0
        n=j + 1
        total_payoff = [0 for l in range(100)]
        for i in range(100000):
            normal_form_game_player = normal_form_game_payoff(4)
            payoff1, payoff2 = game_simulation(lamda)
            max1 = max(payoff1)
            max2 = max(payoff2)

            for l in range(12):
                total_payoff[l] =total_payoff[l] + payoff1[l]
        avg_payoff1.append(total_payoff1/100)
        avg_payoff2.append(total_payoff2/100)
        level0_p1.append(winners1.count(0))
        level1_p1.append(winners1.count(1))
        level2_p1.append(winners1.count(2))
        tie_p1.append(winners1.count(999))
        level0_p2.append(winners2.count(0))
        level1_p2.append(winners2.count(1))
        level2_p2.append(winners2.count(2))
        tie_p2.append(winners2.count(999))
    avg_payoff = [total_payoff[l]/100000.0 for l in range(12)]
    print avg_payoff
    ind = np.arange(100)
    # add tie
    print(ind)
    width = 0.8 / 2
    maximum_payoff = max(avg_payoff)
    plt.bar(ind, avg_payoff, width, label='Average Payoff', color='purple')
    plt.axhline(maximum_payoff)
    plt.xlabel(r'Levels')
    plt.ylabel('Payoff')
    plt.title(r'Payoff for different levels (Row)')
    plt.grid()
    payoff_string = 'max payoff = ' + str(maximum_payoff)
    plt.text(2.8, maximum_payoff + 0.5, payoff_string)
    plt.show()
    print level_k_probabilities_1(1, 0)
    print len(normal_form_game_payoff(3))
    print avg_payoff







