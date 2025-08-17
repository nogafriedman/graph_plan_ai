Introduction to Artificial Intelligence - Exercise 4: GraphPlan

This project, part of the Introduction to Artificial Intelligence course, focuses on implementing and extending the GraphPlan algorithm for automated planning. The assignment includes building planning graphs with mutex relations, applying GraphPlan to the Dock-Worker Robot (DWR) domain, deriving heuristics from planning graphs for A*, and generating domain and problem files for the Tower of Hanoi puzzle.
The primary goals of this project are:
Implementing GraphPlan with action and proposition mutex relations.
Using planning graphs to generate heuristics such as max-level and level-sum.
Comparing heuristics theoretically and empirically.
Automatically generating domain and problem files for Tower of Hanoi with arbitrary disk and peg counts.

Files:
graph_plan.py - Main GraphPlan implementation
plan_graph_level.py - Representation of planning graph levels (actions, propositions, mutexes)
planning_problem.py - Planning problem representation, A* integration, and heuristics
hanoi.py - Automatic generation of Tower of Hanoi domain and problem files
action.py, proposition.py - Core planning objects
action_layer.py, proposition_layer.py - Support for graph levels
util.py - Supporting data structures

How to Run:

Run GraphPlan on DWR domain:
python3 graph_plan.py dwrDomain.txt dwrProblem.txt 
Expected solution: plan with 6 actions (excluding noOps)

Run GraphPlan on custom instances:
python3 graph_plan.py dwrDomain.txt dwr1.txt
python3 graph_plan.py dwrDomain.txt dwr2.txt
* dwr1.txt should require at least 8 actions
* dwr2.txt should be unsolvable

Run Planning Problem with heuristics:
Null heuristic:
python3 planning_problem.py dwrDomain.txt dwrProblem.txt zero

Max-level heuristic:
python3 planning_problem.py dwrDomain.txt dwrProblem.txt max

Level-sum heuristic:
python3 planning_problem.py dwrDomain.txt dwrProblem.txt sum

Generate Tower of Hanoi domain and problem files:
python3 hanoi.py [n] [m]
