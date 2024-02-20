#Room-Cleaner

1. Introduction:
This code creates a scenario where t
wo agents (Agent A and Agent B) try to clean dirty rooms .
The agents have different strategies and chances of cleaning, and their interactions are
simulated.
2. Agent State and Memory:
-
The agents' states (Dirty 'D' or Clean 'C') are stored in the variables `A`, `B`, and `
-
Each agent keeps its own memory (`mem_A`, `mem_B`, and `mem_C`) for first 50 visit to
remember previous actions and situations.
3. Events and
Scoring:
-
The agents' states and actions are recorded in 'Agent_A.txt' and 'Agent_B.txt' files at each
time step.
-
The agents' scores (`Agent_A_score` and `Agent_B_score`) are updated based on their
cleaning actions.
4. Strategic Decisions:
-
Agents make decisions based on their past performance. For example, the chance of a dirty
room in a certain location affects the agent's action choice.
-
The cleaning robot checks and records the contamination status of rooms A, B and C during
its first 50 visits. After these records, it calculates the probability according to the statistical
data it obtains and makes the choice of the room to go accordingl y.
5. Automatic Cleaning:
-
The main cleaning action is 'suck,' which means removing dirt.
-
Agents can also move left or right or stay in the room.
6. Probabilistic Cleaning:
-
Agents use chances to decide actions, considering the historical success of cleaning in
different scenarios.
-
Chances (`A_prob_for_A`, `B_prob_for_A`, `A_prob_for_B`, etc.) determine the likelihood of
choosing 'suck' or movement actions.
7. Probability of Recontamination:
7. Probability of Recontamination:
-
- The parameters `p1`, `p2`, and `p3` decide the chance of recontamination after a region has The parameters `p1`, `p2`, and `p3` decide the chance of recontamination after a region has been cleaned.been cleaned.
-
- The agents do not know the probabilities of recontamination. They provide their own The agents do not know the probabilities of recontamination. They provide their own estimates based on their perceptions.estimates based on their perceptions.
8.
8. Results and Output:Results and Output:
-
- The simulation runs for The simulation runs for 1000 time1000 time steps, capturing the steps, capturing the room situation, room situation, agents' actions,agents' actions, room room situation after situation after agents' actionsagents' actions, and scores., and scores.
-
- The 'Agent_A.txt' and 'Agent_B.txt' files document the simulation results for further analysis.The 'Agent_A.txt' and 'Agent_B.txt' files document the simulation results for further analysis.
9. Conclusion
9. Conclusion::
-
- The code aims to model the complex interactions of cleaning agents in a dirty The code aims to model the complex interactions of cleaning agents in a dirty environment. environment. By incorporating strategic decisions, memory, and probabilistic elements, it provides a versatile By incorporating strategic decisions, memory, and probabilistic elements, it provides a versatile simulation framework. Future enhancements could involve refining the learning mechanisms simulation framework. Future enhancements could involve refining the learning mechanisms of agents and introducing additional environmental factoof agents and introducing additional environmental factors for a more realistic simulation.rs for a more realistic simulation.
