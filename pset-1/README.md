README – MIT 6.0002 Problem Set 1
This repository contains my solutions to MIT 6.0002 (Intro to Computational Thinking and Data Science) Problem Set 1.
The project has two parts:

Part A – Space Cows: Transport mutant cows to space using greedy and brute‑force algorithms.

Part B – Golden Eggs: Find the minimum number of golden eggs to reach a target weight using dynamic programming.

📁 Files
File	Description
ps1a.py	Loads cow data, implements greedy and brute‑force transport.
ps1b.py	Dynamic programming solution for the egg‑weight problem.
ps1_partition.py	Helper to generate set partitions (used by brute‑force).
ps1_cow_data.txt / ps1_cow_data_2.txt	Cow datasets (name,weight).
MIT6_0002F16_ProblemSet1.pdf	Original problem statement (reference).
🚀 How to Run
Ensure all files are in the same folder.

Run Part A:

bash
python ps1a.py
Run Part B:

bash
python ps1b.py
No external libraries are needed – only Python 3 standard library.

🧠 Algorithm Highlights
Part A – Space Cows
Greedy: Each trip takes the heaviest cow that still fits. Fast but not always optimal.

Brute‑force: Enumerates all set partitions (via get_partitions) and returns the first valid grouping – guaranteed optimal, but slower (exponential).

Part B – Golden Eggs
Top‑down DP with memoization:
dp(weight) = min( dp(weight - egg) + 1 ) over all egg weights.
Base: dp(0)=0.
Solves the “minimum coins” problem, where eggs are coins and you want the fewest to hit the target.

📊 Example Output
Part A (on ps1_cow_data.txt):

text
Greedy trips: 4, time: 0.0002 sec
Brute trips: 4, time: 0.45 sec
Part B:

text
Egg weights = (1, 5, 10, 25), n = 99
Actual output: 9   (3×25 + 2×10 + 4×1
