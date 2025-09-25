#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的Q-learning强化学习示例
环境：4x4网格世界
智能体从(0,0)出发，目标到达(3,3)
障碍物在(1,1)和(2,2)
"""

import numpy as np
import random

class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.actions = ['up', 'down', 'left', 'right']
        self.goal = (3, 3)  # 目标位置
        self.obstacles = [(1, 1), (2, 2)]  # 障碍物位置
        
    def reset(self):
        """重置环境，返回初始状态"""
        self.state = (0, 0)  # 起始位置
        return self.state
    
    def step(self, action):
        """执行动作，返回(next_state, reward, done)"""
        x, y = self.state
        
        # 执行动作
        if action == 'up':
            x = max(0, x - 1)
        elif action == 'down':
            x = min(self.size - 1, x + 1)
        elif action == 'left':
            y = max(0, y - 1)
        elif action == 'right':
            y = min(self.size - 1, y + 1)
        
        next_state = (x, y)
        
        # 检查是否到达目标
        if next_state == self.goal:
            reward = 10  # 到达目标的奖励
            done = True
        # 检查是否碰到障碍物
        elif next_state in self.obstacles:
            reward = -5  # 碰到障碍物的惩罚
            done = False
        # 普通移动
        else:
            reward = -1  # 每步的代价
            done = False
        
        self.state = next_state
        return next_state, reward, done
    
    def get_valid_actions(self, state):
        """获取当前状态下有效的动作"""
        return self.actions  # 在这个简单环境中，所有动作都有效

class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.3):
        self.env = env
        self.lr = learning_rate  # 学习率
        self.gamma = discount_factor  # 折扣因子
        self.epsilon = exploration_rate  # 探索率
        
        # 初始化Q表
        self.q_table = {}
        for i in range(env.size):
            for j in range(env.size):
                state = (i, j)
                self.q_table[state] = {action: 0.0 for action in env.actions}
    
    def choose_action(self, state):
        """ε-greedy策略选择动作"""
        if random.random() < self.epsilon:
            # 探索：随机选择动作
            return random.choice(self.env.actions)
        else:
            # 利用：选择Q值最大的动作
            q_values = self.q_table[state]
            max_q = max(q_values.values())
            # 如果有多个动作具有相同的最大Q值，随机选择一个
            best_actions = [action for action, q_val in q_values.items() if q_val == max_q]
            return random.choice(best_actions)
    
    def learn(self, state, action, reward, next_state, done):
        """更新Q值"""
        current_q = self.q_table[state][action]
        
        if done:
            target = reward
        else:
            # 下一个状态的最大Q值
            next_max_q = max(self.q_table[next_state].values())
            target = reward + self.gamma * next_max_q
        
        # Q-learning更新公式
        self.q_table[state][action] = current_q + self.lr * (target - current_q)
    
    def get_policy(self):
        """获取最优策略"""
        policy = {}
        for state in self.q_table:
            q_values = self.q_table[state]
            best_action = max(q_values, key=q_values.get)
            policy[state] = best_action
        return policy

def train_agent(episodes=1000):
    """训练Q-learning智能体"""
    env = GridWorld()
    agent = QLearningAgent(env)
    
    print("开始训练Q-learning智能体...")
    print(f"训练回合数: {episodes}")
    print("-" * 50)
    
    for episode in range(episodes):
        state = env.reset()
        total_reward = 0
        steps = 0
        done = False
        
        while not done and steps < 100:  # 防止无限循环
            # 选择动作
            action = agent.choose_action(state)
            
            # 执行动作
            next_state, reward, done = env.step(action)
            
            # 学习
            agent.learn(state, action, reward, next_state, done)
            
            state = next_state
            total_reward += reward
            steps += 1
        
        # 每100回合打印进度
        if (episode + 1) % 100 == 0:
            print(f"回合 {episode + 1}: 总奖励 = {total_reward}, 步数 = {steps}")
    
    print("训练完成!")
    print("-" * 50)
    
    return agent

def test_agent(agent):
    """测试训练好的智能体"""
    env = GridWorld()
    state = env.reset()
    done = False
    path = [state]
    total_reward = 0
    steps = 0
    
    print("测试智能体性能:")
    print(f"起点: {state}, 目标: {env.goal}, 障碍物: {env.obstacles}")
    
    policy = agent.get_policy()
    
    while not done and steps < 20:
        action = policy[state]  # 使用最优策略
        next_state, reward, done = env.step(action)
        
        path.append(next_state)
        total_reward += reward
        steps += 1
        state = next_state
        
        print(f"步骤 {steps}: 状态 {state}, 动作 {action}, 奖励 {reward}")
    
    print(f"\n最终路径: {path}")
    print(f"总奖励: {total_reward}")
    print(f"总步数: {steps}")
    
    if state == env.goal:
        print("✅ 成功到达目标!")
    else:
        print("❌ 未能到达目标")
    
    return path

def display_q_table(agent):
    """显示Q表"""
    print("\nQ表 (部分显示):")
    print("状态\t\t动作\t\tQ值")
    print("-" * 40)
    
    # 显示前几个状态
    states_to_show = [(0, 0), (0, 1), (1, 0), (2, 3), (3, 2), (3, 3)]
    
    for state in states_to_show:
        if state in agent.q_table:
            for action, q_val in agent.q_table[state].items():
                print(f"{state}\t{action}\t{q_val:.3f}")
        print("-" * 40)

def main():
    """主函数"""
    # 训练智能体
    agent = train_agent(episodes=1000)
    
    # 测试智能体
    print("\n" + "="*60)
    test_agent(agent)
    
    # 显示部分Q表
    display_q_table(agent)
    
    # 显示最优策略
    print("\n最优策略:")
    policy = agent.get_policy()
    for state, action in policy.items():
        print(f"状态 {state}: 最佳动作 {action}")

if __name__ == "__main__":
    main()