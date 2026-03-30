import random

class BusinessEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.money = 10000
        self.employees = 1
        self.revenue = 1000
        self.step_count = 0
        return self.state()

    def state(self):
        return {
            "money": self.money,
            "employees": self.employees,
            "revenue": self.revenue,
            "step": self.step_count
        }

    def step(self, action):
        if action == "hire" and self.money >= 1000:
            self.employees += 1
            self.money -= 1000

        elif action == "invest" and self.money >= 500:
            self.revenue += 500
            self.money -= 500

        elif action == "save":
            self.money += self.revenue

        # random market change
        if random.random() < 0.3:
            self.revenue -= 200

        self.money += self.revenue
        self.step_count += 1

        reward = self.money + self.revenue
        done = self.step_count >= 5

        return self.state(), reward, done


# DEMO RUN (IMPORTANT)
if __name__ == "__main__":
    env = BusinessEnv()
    state = env.reset()

    print("START:", state)

    for i in range(5):
        action = random.choice(["hire", "invest", "save"])
        state, reward, done = env.step(action)

        print("\nStep:", i+1)
        print("Action:", action)
        print("State:", state)
        print("Reward:", reward)

        if done:
            break
