import numpy as np
import matplotlib.pyplot as plt
import math


np.random.seed(3)
def normal_form_game_payoff():

    num=np.random.randint(1,11)
    num1=np.random.randint(1,11)
    num2=np.random.randint(1,11)
    num3 = np.random.randint(1, 11)
    num4 = np.random.randint(1, 11)
    num5 = np.random.randint(1, 11)
    num6 = np.random.randint(1, 11)
    num7 = np.random.randint(1, 11)
    normal_form_game = [[[num,num1],[num2,num3]],[[num4,num5],[num6,num7]]]
    return normal_form_game




def level_k_probabilities_2(k,player,lamda2=0.1):
    if k==0:
        return (0.5,0.5)
    sum_1 = np.exp(lamda2 * (level_k_probabilities_1(k - 1, (player + 1) % 2,lamda=0.05)[0] * normal_form_game_player[0][0][player%2] +
                                level_k_probabilities_1(k - 1, (player + 1) % 2,lamda=0.05)[1] * normal_form_game_player[player%2][(player+1)%2][player%2]))
    sum_2 = np.exp(lamda2 * (level_k_probabilities_1(k - 1, (player + 1) % 2,lamda=0.05 )[0] * normal_form_game_player[(player+1)%2][player%2][player%2] +
                                level_k_probabilities_1(k - 1, (player + 1) % 2,lamda=0.05)[1] * normal_form_game_player[1][1][player%2]))
    prob1 = sum_1/(sum_1+sum_2)
    prob2=sum_2/(sum_1+sum_2)
    return (prob1,prob2)

def level_k_probabilities_1(k,player,lamda=0.1):
    if k==0:
        return (0.5,0.5)
    sum_1 = np.exp(lamda * (level_k_probabilities_1(k - 1, (player + 1) % 2)[0] * normal_form_game_player[0][0][player%2] +
                                level_k_probabilities_1(k - 1, (player + 1) % 2)[1] * normal_form_game_player[player%2][(player+1)%2][player%2]))
    sum_2 = np.exp(lamda * (level_k_probabilities_1(k - 1, (player + 1) % 2)[0] * normal_form_game_player[(player+1)%2][player%2][player%2] +
                                level_k_probabilities_1(k - 1, (player + 1) % 2)[1] * normal_form_game_player[1][1][player%2]))
    prob1 = sum_1/(sum_1+sum_2)
    prob2=sum_2/(sum_1+sum_2)
    return (prob1,prob2)

def poisson_distribution(lamda=0.5, no_of_levels=2):
    probabilistic_distribution=[]
    for i in range(no_of_levels+1):
        probabilistic_distribution.append(np.power(lamda, i)*np.exp(-lamda)/float(math.factorial(i)))
    probabilistic_distribution = [i/sum(probabilistic_distribution) for i in probabilistic_distribution]
    return probabilistic_distribution
def level_0_payoff(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2):
    player_probabilities=lk_probabilities_0
    level_0_probabilities=lk_probabilities_0
    level_1_probabilities=lk_probabilities_1
    level_2_probabilities=lk_probabilities_2
    player_distribution=poisson_distribution()
    payoff_sq1=player_probabilities[0]*normal_form_game_player[0][0][0]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq2=player_probabilities[0]*normal_form_game_player[0][1][0]*(level_0_probabilities[1]*player_distribution[0]+level_1_probabilities[1]*player_distribution[1]+level_2_probabilities[1]*player_distribution[2])
    payoff_sq3=player_probabilities[1]*normal_form_game_player[1][0][0]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq4 = player_probabilities[1] * normal_form_game_player[1][1][0] * (
                level_0_probabilities[1] * player_distribution[0] + level_1_probabilities[1] * player_distribution[1] +
                level_2_probabilities[1] * player_distribution[2])
    payoff=(payoff_sq1+payoff_sq2+payoff_sq3+payoff_sq4)
    return payoff
def level_1_payoff(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2):
    player_probabilities = lk_probabilities_1
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution=poisson_distribution()
    payoff_sq1=player_probabilities[0]*normal_form_game_player[0][0][0]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq2=player_probabilities[0]*normal_form_game_player[0][1][0]*(level_0_probabilities[1]*player_distribution[0]+level_1_probabilities[1]*player_distribution[1]+level_2_probabilities[1]*player_distribution[2])
    payoff_sq3=player_probabilities[1]*normal_form_game_player[1][0][0]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq4 = player_probabilities[1] * normal_form_game_player[1][1][0] * (
                level_0_probabilities[1] * player_distribution[0] + level_1_probabilities[1] * player_distribution[1] +
                level_2_probabilities[1] * player_distribution[2])
    payoff = (payoff_sq1 + payoff_sq2 + payoff_sq3 + payoff_sq4)
    return payoff
def level_2_payoff(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2):
    player_probabilities = lk_probabilities_2
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution=poisson_distribution()
    payoff_sq1=player_probabilities[0]*normal_form_game_player[0][0][0]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq2=player_probabilities[0]*normal_form_game_player[0][1][0]*(level_0_probabilities[1]*player_distribution[0]+level_1_probabilities[1]*player_distribution[1]+level_2_probabilities[1]*player_distribution[2])
    payoff_sq3=player_probabilities[1]*normal_form_game_player[1][0][0]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq4 = player_probabilities[1] * normal_form_game_player[1][1][0] * (
                level_0_probabilities[1] * player_distribution[0] + level_1_probabilities[1] * player_distribution[1] +
                level_2_probabilities[1] * player_distribution[2])
    payoff = (payoff_sq1 + payoff_sq2 + payoff_sq3 + payoff_sq4)
    return payoff

def level_0_payoff_2(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2):
    player_probabilities = lk_probabilities_0
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff_sq1=player_probabilities[0]*normal_form_game_player[0][0][1]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq2=player_probabilities[0]*normal_form_game_player[1][0][1]*(level_0_probabilities[1]*player_distribution[0]+level_1_probabilities[1]*player_distribution[1]+level_2_probabilities[1]*player_distribution[2])
    payoff_sq3=player_probabilities[1]*normal_form_game_player[0][1][1]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq4 = player_probabilities[1] * normal_form_game_player[1][1][1] * (
                level_0_probabilities[1] * player_distribution[0] + level_1_probabilities[1] * player_distribution[1] +
                level_2_probabilities[1] * player_distribution[2])
    payoff2 = payoff_sq1 + payoff_sq2 + payoff_sq3 + payoff_sq4
    return payoff2
def level_1_payoff_2(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2):
    player_probabilities = lk_probabilities_1
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff_sq1=player_probabilities[0]*normal_form_game_player[0][0][1]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq2=player_probabilities[0]*normal_form_game_player[1][0][1]*(level_0_probabilities[1]*player_distribution[0]+level_1_probabilities[1]*player_distribution[1]+level_2_probabilities[1]*player_distribution[2])
    payoff_sq3=player_probabilities[1]*normal_form_game_player[0][1][1]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq4 = player_probabilities[1] * normal_form_game_player[1][1][1] * (
                level_0_probabilities[1] * player_distribution[0] + level_1_probabilities[1] * player_distribution[1] +
                level_2_probabilities[1] * player_distribution[2])
    payoff2=payoff_sq1+payoff_sq2+payoff_sq3+payoff_sq4
    return payoff2
def level_2_payoff_2(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2):
    player_probabilities = lk_probabilities_2
    level_0_probabilities = lk_probabilities_0
    level_1_probabilities = lk_probabilities_1
    level_2_probabilities = lk_probabilities_2
    player_distribution = poisson_distribution()
    payoff_sq1=player_probabilities[0]*normal_form_game_player[0][0][1]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq2=player_probabilities[0]*normal_form_game_player[1][0][1]*(level_0_probabilities[1]*player_distribution[0]+level_1_probabilities[1]*player_distribution[1]+level_2_probabilities[1]*player_distribution[2])
    payoff_sq3=player_probabilities[1]*normal_form_game_player[0][1][1]*(level_0_probabilities[0]*player_distribution[0]+level_1_probabilities[0]*player_distribution[1]+level_2_probabilities[0]*player_distribution[2])
    payoff_sq4 = player_probabilities[1] * normal_form_game_player[1][1][1] * (
                level_0_probabilities[1] * player_distribution[0] + level_1_probabilities[1] * player_distribution[1] +
                level_2_probabilities[1] * player_distribution[2])
    payoff2 = payoff_sq1 + payoff_sq2 + payoff_sq3 + payoff_sq4
    return payoff2
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
for i in range(20):
    normal_form_game_player=normal_form_game_payoff()
    lk_probabilities_0 = level_k_probabilities_1(0, 0)
    lk_probabilities_1 = level_k_probabilities_1(1, 0)
    lk_probabilities_2 = level_k_probabilities_2(2, 0)
    probabilistic_distribution = poisson_distribution()
    print '\n\n'
    print ('Game', i)
    print  '\n'
    print 'Payoff Matrix\n'
    print normal_form_game_player[0]
    print normal_form_game_player[1]
    print 'Player 1'
    print 'Level-0 -->', lk_probabilities_0
    print 'Level-1 -->', lk_probabilities_1
    print 'Level-2 -->',lk_probabilities_2
    payoff_10 = level_0_payoff(lk_probabilities_0, lk_probabilities_1, lk_probabilities_2)
    payoff_11 = level_1_payoff(lk_probabilities_0, lk_probabilities_1, lk_probabilities_2)
    payoff_12 = level_2_payoff(lk_probabilities_0, lk_probabilities_1, lk_probabilities_2)
    payoff_1 = [payoff_10, payoff_11, payoff_12]
    print 'Avg. Payoff -->',payoff_1
    lk_probabilities_0 = level_k_probabilities_1(0, 1)
    lk_probabilities_1 = level_k_probabilities_1(1, 1)
    lk_probabilities_2 = level_k_probabilities_2(2, 1)
    print 'Player 2'
    print 'Level-0 -->', lk_probabilities_0
    print 'Level-1 -->', lk_probabilities_1
    print 'Level-2 -->', lk_probabilities_2
    payoff_20 = level_0_payoff_2(lk_probabilities_0, lk_probabilities_1, lk_probabilities_2)
    payoff_21 = level_1_payoff_2(lk_probabilities_0, lk_probabilities_1, lk_probabilities_2)
    payoff_22 = level_2_payoff_2(lk_probabilities_0, lk_probabilities_1, lk_probabilities_2)
    payoff_2 = [payoff_20, payoff_21, payoff_22]
    print 'Avg. Payoff -->',payoff_2
    level = ['0', '1', '2']
    plt.plot(level, payoff_1, color='r', label='Player-1')
    plt.plot(level, payoff_2, color='blue', label='Player-2')
    plt.legend()
    plt.title('Quantal Level-k')
    plt.grid()
    plt.xlabel('Cognitive Levels')
    plt.ylabel('Avg. Payoff')
    plt.axis('tight')
    plt.show()





