# SafetyHack 2023

SafetyHACK 2023 is a hackathon co-organised by MIT Node and HKPC. The hackathon is about safety on construction sites for all members of community.

## Our solution

Our solution is to make a platform which takes data from AI cameras to motivate workers to behave safely with positive feedback loop.
We believe that positive feedback in terms of bonuses, cash, free lunches can have better effect on workers than fines. This will encourage them to wear PPE, safety harness and avoid dangerous zones.

## Code

Obviously, I cannot implement whole solution in just 1 day. That's why I implemented platform for manager on which he can see statistics of workers and calculate rewards for them.

The data generated is stored in CSV file and after that backend calculate values for real and performs operations. So if you are interested you also can run this project with your own data.

## Repo

This repo has frontend(Vue.js), backend(FastAPI) and data generation code of sample app.

Python environment(Micromamba) in `env.yaml` file. It is required by `datagen` and `backend`.

Big thanks to my friend Glenn Salter for helping to write `datagen`.