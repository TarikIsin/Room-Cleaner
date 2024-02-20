import random
import numpy as np


def main(p1, p2, p3):
    Agent_A_score = 0
    Agent_B_score = 0
    
    A = 'D'
    B = 'D'
    C = 'D'
    position = 'B'

    mem_A = []
    mem_B = []
    mem_C = []

    A_prob_for_A = 0
    B_prob_for_A = 0
    A_prob_for_B = 0
    B_prob_for_B = 0
    C_prob_for_B = 0
    B_prob_for_C = 0
    C_prob_for_C = 0

    with open('Agent_A_Config5_Test10.txt', 'w') as Agent_A, open('Agent_B_Config5_Test10.txt', 'w') as Agent_B:
        for time_step in range(1000):
            Agent_A.write(f'{position}, {A}, {B}, {C}\n')
            Agent_B.write(f'{position}, {A}, {B}, {C}\n')

            if len(mem_A + mem_B + mem_C) == 150:
                D_number_A = mem_A.count('D')
                D_number_B = mem_B.count('D')
                D_number_C = mem_C.count('D')

                A_prob_for_A = D_number_A / (D_number_A + D_number_B)
                B_prob_for_A = D_number_B / (D_number_A + D_number_B)

                A_prob_for_B = D_number_A / (D_number_A + D_number_B + D_number_C)
                B_prob_for_B = D_number_B / (D_number_A + D_number_B + D_number_C)
                C_prob_for_B = D_number_C / (D_number_A + D_number_B + D_number_C)

                B_prob_for_C = D_number_B / (D_number_B + D_number_C)
                C_prob_for_C = D_number_C / (D_number_B + D_number_C)

            if position == 'B':
                if len(mem_B) < 51:
                    mem_B.append(B)
                if len(mem_A + mem_B + mem_C) < 151:
                    action = 'suck' if B == 'D' else random.choice(['left', 'stay', 'right'])
                elif len(mem_A + mem_B + mem_C) >= 151:
                    choice = np.random.choice(['left', 'stay', 'right'], p=[A_prob_for_B, B_prob_for_B, C_prob_for_B])
                    action = 'suck' if B == 'D' else choice

                if action == 'suck':
                    B = 'C'
                elif action == 'left':
                    position = 'A'
                    Agent_B_score -= 0.5
                elif action == 'right':
                    position = 'C'
                    Agent_B_score -= 0.5

            elif position == 'A':
                if len(mem_A) < 51:
                    mem_A.append(A)
                if len(mem_A + mem_B + mem_C) < 151:
                    action = 'suck' if A == 'D' else random.choice(['stay', 'right'])
                elif len(mem_A + mem_B + mem_C) >= 151:
                    choice = np.random.choice(['stay', 'right'], p=[A_prob_for_A, B_prob_for_A])
                    action = 'suck' if A == 'D' else choice
                if action == 'suck':
                    A = 'C'
                elif action == 'right':
                    position = 'B'
                    Agent_B_score -= 0.5
            else:
                if len(mem_C) < 51:
                    mem_C.append(C)
                if len(mem_A + mem_B + mem_C) < 151:
                    action = 'suck' if C == 'D' else random.choice(['left', 'stay'])
                elif len(mem_A + mem_B + mem_C) >= 151:
                    choice = np.random.choice(['left', 'stay'], p=[B_prob_for_C, C_prob_for_C])
                    action = 'suck' if C == 'D' else choice
                if action == 'suck':
                    C = 'C'
                elif action == 'left':
                    position = 'B'
                    Agent_B_score -= 0.5

            if A == 'C':
                Agent_A_score += 1
                Agent_B_score += 1
            if B == 'C':
                Agent_A_score += 1
                Agent_B_score += 1
            if C == 'C':
                Agent_A_score += 1
                Agent_B_score += 1

            Agent_A.write(action + '\n')
            Agent_A.write(f'{position}, {A}, {B}, {C}\n')
            Agent_A.write(str(Agent_A_score) + '\n')
            Agent_B.write(action + '\n')
            Agent_B.write(f'{position}, {A}, {B}, {C}\n')
            Agent_B.write(str(Agent_B_score) + '\n')
            if A == 'C':
                if random.random() <= p1:
                    A = 'D'
            if B == 'C':
                if random.random() <= p2:
                    B = 'D'
            if C == 'C':
                if random.random() <= p3:
                    C = 'D'


if __name__ == '__main__':
    pA = float(input("Enter the probability of contamination of room A (0-1): "))
    pB = float(input("Enter the probability of contamination of room B (0-1): "))
    pC = float(input("Enter the probability of contamination of room C (0-1): "))
    main(pA, pB, pC)
