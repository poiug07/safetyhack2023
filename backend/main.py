from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd

app = FastAPI()
data = pd.read_csv('data.csv')

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/workers")
async def get_workers():
    # print(list(map(int, data["worker_id"].unique())))
    return list(map(int, data["worker_id"].unique()))

@app.get("/api/sumstat/{worker_id}")
async def get_ppe_total(worker_id):
    worker_data = data[data["worker_id"]==int(worker_id)]

    resp = {
        "ppe": int(worker_data["ppe"].sum()),
        "danger": int(worker_data["danger"].sum()),
        "safety_harness": int(worker_data["safety_harness"].sum()),
    }

    return resp

def get_reward_func(worker_id):

    worker_data = data[data["worker_id"]==int(worker_id)]
    # print(worker_data["ppe"].sum())
    # print(worker_data["danger"].sum())
    # print(worker_data["safety_harness"].sum())
    reward = max(3 * worker_data["ppe"].sum() - 2 * worker_data["danger"].sum() - 2 * worker_data["safety_harness"].sum(), 0) // 100

    resp = {"reward": int(reward)}
    # print(resp)
    return resp

@app.get("/api/workers/{worker_id}/reward")
async def get_reward(worker_id):
    return get_reward_func(worker_id)

@app.get("/api/summary")
async def get_summary():
    workers = list(map(int, data["worker_id"].unique()))
    a = map(get_reward_func, workers)
    rewards = list(map(lambda x: x["reward"], a))
    resp = {
        "total": sum(rewards),
        "best": max(rewards),
        "worst": min(rewards)
    }
    return resp
