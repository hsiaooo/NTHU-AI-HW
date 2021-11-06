# LunarLander
---
![](img/original.gif)

image credit by [Gym (openai.com)](https://gym.openai.com/envs/LunarLanderContinuous-v2/)

## You will learn to solve problem using genetic algorithm (GA).
LunarLander is a game in Open AI Gym. In this game, the task is to navigate the lander to the landing pad. By precisely controlling the lander's main engine and side engines, which produce the vertical and horizontal thrust, the lander can land on pad safely.

A safety landing on the landing pad gets a positive reward. A safety landing outside the landing pad gets no reward. Crashing the lander yields a huge negative reward. In addition, the total fuel consumption is converted into a negative reward. In other words, your lander is expected to perform a safe, precise, and fuel-efficient maneuver to maximize the reward received.

### Problem Description
In this assignment, you are asked to optimize the control policy of the lunar lander with genetic algorithm (GA). The lunar lander continuously observes its status and the environment and pilots itself according to the control policy you provided. We have implemented a GA and testing framework for you. Your task is to design and implement the evolutionary operators and tune the parameters for GA so that GA works effectively and efficiently.

- observes
- action
- control policy

---
Reference: [LunarLand GA](https://sites.google.com/gapp.nthu.edu.tw/lunarlander-ga)
