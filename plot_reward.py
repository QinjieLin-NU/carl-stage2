import matplotlib.pyplot as plt
fileids = [11,13]
len_episodes = [10,35]#num of robot
for i in range(len(fileids)):
    fileid = fileids[i]
    len_episode = len_episodes[i]
    rewards=[]
    hostname = "autoRL_%d/"%fileid
    dirname = '/clever/saved_model_ppo/' + hostname + "log"
    with open(dirname+"/cal.log", 'r') as f:
        for line in f:
            rewards.append(line)

    rewards = map(lambda s: s.strip(), rewards)
    rewards = map(float,rewards)
    num = len(rewards)
    num_episode = int(num / len_episode)
    new_rewards=[]
    for i in range(num_episode):
        averaged_reward = sum(rewards[i*len_episode:(i+1)*len_episode])/len_episode
        new_rewards.append(averaged_reward)

    x= range(len(new_rewards))
    print(len(new_rewards))
    plt.plot(x, new_rewards)
plt.show()