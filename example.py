from pyrateer.factors import NumericFactor, CategoricalFactor, ConstantFactor
import pickle


asset_size = NumericFactor(
    "Asset Size",
    {
        1: 1065,
        1_000_000: 1_819,
        2_500_000: 3_966,
        5_000_000: 3_619,
        10_000_000: 4_291,
        15_000_000: 4_905,
        20_000_000: 5_120,
        25_000_000: 5_499,
        50_000_000: 6_279,
        75_000_000: 6_966,
        100_000_000: 7_156,
        250_000_000: 8_380,
    }
)

limit_retention_dict = {
   0: -0.760,
    1_000: -0.600,
    2_500: -0.510,
    5_000: -0.406,
    7_500: -0.303,
    10_000: -0.231,
    15_000: -0.128,
    20_000: -0.064,
    25_000: 0.000,
    35_000: 0.105,
    50_000: 0.175,
    75_000: 0.277,
    100_000: 0.350,
    125_000: 0.406,
    150_000: 0.452,
    175_000: 0.491,
    200_000: 0.525,
    225_000: 0.555,
    250_000: 0.581,
    275_000: 0.605,
    300_000: 0.627,
    325_000: 0.648,
    350_000: 0.666,
    375_000: 0.684,
    400_000: 0.700,
    425_000: 0.715,
    450_000: 0.730,
    475_000: 0.743,
    500_000: 0.756,
    525_000: 0.807,
    550_000: 0.819,
    575_000: 0.831,
    600_000: 0.842,
    625_000: 0.853,
    650_000: 0.864,
    675_000: 0.874,
    700_000: 0.883,
    725_000: 0.893,
    750_000: 0.902,
    775_000: 0.910,
    800_000: 0.919,
    825_000: 0.927,
    850_000: 0.935,
    875_000: 0.943,
    900_000: 0.950,
    925_000: 0.957,
    950_000: 0.964,
    975_000: 0.971,
    1_000_000: 1.000,
    2_000_000: 1.415,
    2_500_000: 1.526,
    3_000_000: 1.637,
    4_000_000: 1.820,
    5_000_000: 1.986,
}

limit = NumericFactor("Limit", limit_retention_dict)
retention = NumericFactor("Retention", limit_retention_dict)
industry = CategoricalFactor(
    "Industry",
    {
        "Hazard Group 1": 1.0,
        "Hazard Group 2": 1.25,
        "Hazard Group 3": 1.5,
    }
)
loss_cost = ConstantFactor("Loss Cost", 1.7)

rate_plan = asset_size * (limit - retention) * industry * loss_cost

json_input = {
    "Asset Size": 1_200_000,
    "Limit": 5_000_000,
    "Retention": 1_000_000,
    "Industry": "Hazard Group 2",
}

rate = rate_plan.calculate(**json_input)

print(rate)

with open("rate_plan.pkl", "wb") as f:
    pickle.dump(rate_plan, f)