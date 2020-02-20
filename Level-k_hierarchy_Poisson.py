import numpy as np
import matplotlib.pyplot as plt


np.random.seed(3)
def normal_form_game_payoff(m,n):

    num=np.random.randint(1,11)
    num1=np.random.randint(1,11)
    normal_form_game = [[[num,num+n],[num1,num1+m]],[[num1+2,num1+m+1],[num+n,2]]]
    return normal_form_game


normal_form_game_player=normal_form_game_payoff(2,7)
print(normal_form_game_player)


def level_k_probabilities(k,player):
    if k==0:
        return (0.5,0.5)
    if player%2==0:
        lamda=0.1
        sum_1 = np.exp(lamda * (level_k_probabilities(k - 1, (player + 1) % 2)[0] * normal_form_game_player[0][0][0] +
                                level_k_probabilities(k - 1, (player + 1) % 2)[0] * normal_form_game_player[0][1][0]))
        sum_2 = np.exp(lamda * (level_k_probabilities(k - 1, (player + 1) % 2)[1] * normal_form_game_player[1][0][0] +
                                level_k_probabilities(k - 1, (player + 1) % 2)[1] * normal_form_game_player[1][1][0]))
        prob1 = sum_1/(sum_1+sum_2)
        prob2=sum_2/(sum_1+sum_2)
        return (prob1,prob2)
    if player%2==1:
        lamda = 0.1
        sum_1 = np.exp(lamda * (level_k_probabilities(k - 1, (player + 1) % 2)[0] * normal_form_game_player[0][0][1] +
                                level_k_probabilities(k - 1, (player + 1) % 2)[0] * normal_form_game_player[1][0][1]))
        sum_2 = np.exp(lamda * (level_k_probabilities(k - 1, (player + 1) % 2)[1] * normal_form_game_player[0][1][1] +
                                level_k_probabilities(k - 1, (player + 1) % 2)[1] * normal_form_game_player[1][1][1]))
        prob1 = sum_1 / (sum_1 + sum_2)
        prob2 = sum_2 / (sum_1 + sum_2)
        return (prob1,prob2)

def poisson_distribution(k):
    s = np.random.poisson(5, 10000)
    count, bins, ignored = plt.hist(s, 12, normed=True)
    div=12/(k+1)
    sum_level = sum(count)
    poisson_list=[]
    for i in range(k+1):
        ele=sum(count[i*div:(i+1)*div])/float(sum_level)
        poisson_list.append(ele)
    return poisson_list

def level_k_poisson_probabilities(k, player):
    probability=[]
    poisson_dist=poisson_distribution(k)
    probability.append(sum([poisson_dist[i]*level_k_probabilities(k, player)[0] for i in range(k+1)]))
    probability.append(sum([poisson_dist[i]*level_k_probabilities(k, player)[1] for i in range(k+1)]))
    return probability

s = np.random.poisson(5, 10000)
count, bins, ignored = plt.hist(s, 12, normed=True)
print count
count_list=[]
for i in range(4):
    count_list.append(sum(count[i*3:i*3+3]))
print count_list
sum_of_counts=sum(count_list)
for i in range(len(count_list)):
    count_list[i]=int(count_list[i]/sum_of_counts*1000)
print count_list

###Player 1###
avg_payoff=[]


###Level-0###
total_payoff=0
probability = level_k_poisson_probabilities(0, 0)
probability1 = level_k_poisson_probabilities(0, 1)
for j in range(count_list[0]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(1, 1)
for j in range(count_list[1]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(2, 1)
for j in range(count_list[2]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(3, 1)
for j in range(count_list[3]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    print payoff
    total_payoff = total_payoff + payoff
    print total_payoff
avg_payoff.append(float(total_payoff)/999)
###Level-1###
print ('  ')
total_payoff=0
probability = level_k_poisson_probabilities(1, 0)
probability1 = level_k_poisson_probabilities(0, 1)
for j in range(count_list[0]):

    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(1, 1)
for j in range(count_list[1]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(2, 1)
for j in range(count_list[2]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(3, 1)
for j in range(count_list[3]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    print payoff
    total_payoff = total_payoff + payoff
    print total_payoff
avg_payoff.append(float(total_payoff)/999)
###Level-2###
print ('  ')
total_payoff=0
probability = level_k_poisson_probabilities(2, 0)
probability1 = level_k_poisson_probabilities(0, 1)
for j in range(count_list[0]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(1, 1)
for j in range(count_list[1]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(2, 1)
for j in range(count_list[2]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(3, 1)
for j in range(count_list[3]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    print payoff
    total_payoff = total_payoff + payoff
    print total_payoff
avg_payoff.append(float(total_payoff)/999)
###Level-3###
print ('  ')
total_payoff=0
probability = level_k_poisson_probabilities(3, 0)
probability1 = level_k_poisson_probabilities(0, 1)
for j in range(count_list[0]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(1, 1)
for j in range(count_list[1]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(2, 1)
for j in range(count_list[2]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(3, 1)
for j in range(count_list[3]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][0]
    print payoff
    total_payoff = total_payoff + payoff
    print total_payoff
avg_payoff.append(float(total_payoff)/999)

total_payoff = [i * 999 for i in avg_payoff]
level=['0','1','2','3']
plt.plot(level, total_payoff, color='b', label='Player-1')
plt.xlabel('level-k')
plt.ylabel('Total Payoff')
plt.axis([0,4,9000,13000])
print total_payoff
###Player 2###
avg_payoff=[]
###Level-0###
total_payoff=0
probability = level_k_poisson_probabilities(0, 1)
probability1 = level_k_poisson_probabilities(0, 0)
for j in range(count_list[0]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(1, 0)
for j in range(count_list[1]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(2, 0)
for j in range(count_list[2]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(3, 0)
for j in range(count_list[3]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    print payoff
    total_payoff = total_payoff + payoff
    print total_payoff
avg_payoff.append(float(total_payoff)/999)
###Level-1###
print ('  ')
total_payoff=0
probability = level_k_poisson_probabilities(1, 1)
probability1 = level_k_poisson_probabilities(0, 0)
for j in range(count_list[0]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(1, 0)
for j in range(count_list[1]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(2, 0)
for j in range(count_list[2]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(3, 0)
for j in range(count_list[3]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    print payoff
    total_payoff = total_payoff + payoff
    print total_payoff
avg_payoff.append(float(total_payoff)/999)
###Level-2###
print ('  ')
total_payoff=0
probability = level_k_poisson_probabilities(2, 1)
probability1 = level_k_poisson_probabilities(0, 0)
for j in range(count_list[0]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(1, 0)
for j in range(count_list[1]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(2, 0)
for j in range(count_list[2]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(3, 0)
for j in range(count_list[3]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    print payoff
    total_payoff = total_payoff + payoff
    print total_payoff
avg_payoff.append(float(total_payoff)/999)
###Level-3###
print ('  ')
total_payoff=0
probability = level_k_poisson_probabilities(3, 1)
probability1 = level_k_poisson_probabilities(0, 0)
for j in range(count_list[0]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(1, 0)
for j in range(count_list[1]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(2, 0)
for j in range(count_list[2]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    total_payoff = total_payoff + payoff
probability1 = level_k_poisson_probabilities(3, 0)
for j in range(count_list[3]):
    random_number = np.random.uniform(0, 1)
    if random_number <= probability[0]:
        action0 = 0
    else:
        action0 = 1
    random_number1 = np.random.uniform(0, 1)
    if random_number1 <= probability1[0]:
        action1 = 0
    else:
        action1 = 1
    payoff = normal_form_game_player[action0][action1][1]
    print payoff
    total_payoff = total_payoff + payoff
    print total_payoff
avg_payoff.append(float(total_payoff)/999)
total_payoff = [i * 999 for i in avg_payoff]
print total_payoff
level=['0','1','2','3']
plt.plot(level, total_payoff, color='r', label='Player-2')
plt.legend()
plt.title('Level-k(Poisson)')
plt.axis([0,4,9000,13000])
plt.show()
