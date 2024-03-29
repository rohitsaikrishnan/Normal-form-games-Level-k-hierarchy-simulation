import numpy as np
import matplotlib.pyplot as plt
import math


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


def level_k_probabilities_2(k,player,lamda=0.56, lamda2 = 0.05):
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
                temp_sum = temp_sum + level_k_probabilities_1(k-1, (player+1) % 2,lamda2)[j] * normal_form_game_player[i][j][0]
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
                temp_sum = temp_sum + level_k_probabilities_1(k - 1, (player + 1) % 2,lamda2)[j] * \
                           normal_form_game_player[j][i][1]
            temp_sum = np.exp(lamda * temp_sum)
            sum_action.append(temp_sum)
        probs = []
        for i in range(n):
            temp_prob = sum_action[i] / sum(sum_action)
            probs.append(temp_prob)
        probs = tuple(probs)
        return probs

def level_k_probabilities_1(k,player,lamda=0.36):
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
def poisson_distribution(lamda=1.5, no_of_levels=2):
    probabilistic_distribution=[]
    for i in range(no_of_levels+1):
        probabilistic_distribution.append(np.power(lamda, i)*np.exp(-lamda)/float(math.factorial(i)))
    probabilistic_distribution = [i/sum(probabilistic_distribution) for i in probabilistic_distribution]
    return [0,0,1]
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
    lk_probabilities_2p1 = level_k_probabilities_2(2, 0,lamda, lamda)
    lk_probabilities_0p2 = level_k_probabilities_1(0, 1)
    lk_probabilities_1p2 = level_k_probabilities_1(1, 1, lamda)
    lk_probabilities_2p2 = level_k_probabilities_2(2, 1, lamda, lamda)
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
    for j in range(1):
        lamda = 50
        winners1 = []
        winners2 = []
        for i in range(100):
            normal_form_game_player = normal_form_game_payoff(n)
            payoff1, payoff2 = game_simulation(lamda)
            winners1.append(payoff1[0])
            winners2.append(payoff1[2])

        level0_p1.append(winners1.count(0) * 5)
        level1_p1.append(winners1.count(1) * 5)
        level2_p1.append(winners1.count(2) * 5)
        tie_p1.append(winners1.count(999) * 5)
        level0_p2.append(winners2.count(0) * 5)
        level1_p2.append(winners2.count(1) * 5)
        level2_p2.append(winners2.count(2) * 5)
        tie_p2.append(winners2.count(999) * 5)
    payoff_avg =[]
    payoff_avg.append(sum(winners1)/len(winners1))
    payoff_avg.append(sum(winners2)/len(winners2))

    ind = np.arange(2)
    # add tie
    print(ind)
    width = 0.8 / 4
    plt.bar(ind, payoff_avg, width, label='tie', color='k')


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
    for j in range(1):
        lamda = 50
        winners0 = []
        winners1 = []
        winners2 = []
        for i in range(100000):
            normal_form_game_player = normal_form_game_payoff(2)
            payoff1, payoff2 = game_simulation(lamda)
            winners0.append(payoff1[0])
            winners1.append(payoff1[1])
            winners2.append(payoff1[2])

        level0_p1.append(winners1.count(0) * 5)
        level1_p1.append(winners1.count(1) * 5)
        level2_p1.append(winners1.count(2) * 5)
        tie_p1.append(winners1.count(999) * 5)
        level0_p2.append(winners2.count(0) * 5)
        level1_p2.append(winners2.count(1) * 5)
        level2_p2.append(winners2.count(2) * 5)
        tie_p2.append(winners2.count(999) * 5)
    payoff_avg = []
    payoff_avg.append(sum(winners0)/10000.0)
    payoff_avg.append(sum(winners1) / 10000.0)
    payoff_avg.append(sum(winners2) / 10000.0)

    ind = np.arange(3)
    # add tie
    print(ind)
    width = 0.8 / 4
    plt.bar(ind, payoff_avg, width, label='payoff', color='k')

    plt.xlabel(r'Levels')
    plt.ylabel('Average Payoff')
    plt.title(r'Average Payoff for Level 0 to 2')
    plt.grid()
    plt.text(2.8, 78, r'$\lambda_1$ = $\lambda_2$')
    plt.legend(loc='upper left')
    plt.show()
    print
    level_k_probabilities_1(1, 0)
    print (payoff_avg)
    len(normal_form_game_payoff(3))