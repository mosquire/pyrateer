import pickle

with open("rate_plan.pkl", "rb") as fp:
    rate_plan = pickle.load(fp)

json_input = {
    "Asset Size": 1_200_000,
    "Limit": 5_000_000,
    "Retention": 1_000_000,
    "Industry": "Hazard Group 2",
}

rate = rate_plan.calculate(**json_input)

print(rate)