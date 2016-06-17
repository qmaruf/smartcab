import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
from collections import Counter
from random import randint
import sys

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here        
        self.actions = ['forward', 'left', 'right',None]        
        self.q_table = Counter()        
        self.alpha = 0.5
        self.gamma = 0.2


    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required

    def get_best_action(self, state):
        best_profit = -999
        best_action = None
        for a in self.actions:
            profit = self.q_table[(state, a)]            
            if profit > best_profit:
                best_profit = profit
                best_action = a
        return best_action, best_profit


    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # TODO: Update state
        self.state = (inputs['light'],inputs['oncoming'], self.next_waypoint)       

        if randint(0,10) < 3:
            action = self.actions[randint(0, 3)]
        else:        
            action, _ = self.get_best_action(self.state)
        
        reward = self.env.act(self, action)

        next_inputs = self.env.sense(self)
        next_next_waypoint = self.planner.next_waypoint()
        next_state = (next_inputs['light'],next_inputs['oncoming'], next_next_waypoint)      
       
        _, best_profit = self.get_best_action(next_state)
        self.q_table[(self.state, action)] = (1-self.alpha)*self.q_table[(self.state, action)] + (self.alpha * (reward + self.gamma * best_profit))

       
        # print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    #e.set_primary_agent(a, enforce_deadline=False)  # set agent to track
    e.set_primary_agent(a, enforce_deadline=True)
    # Now simulate it
    sim = Simulator(e, update_delay=1.0/1000000)  # reduce update_delay to speed up simulation
    sim.run(n_trials=100)  # press Esc or close pygame window to quit

if __name__ == '__main__':
    run()