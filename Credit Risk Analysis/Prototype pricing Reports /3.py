contract_val = value_gas_storage_contract(

    injection_dates = ["2024-03-01", "2024-04-01"],
    withdrawal_dates = ["2024-09-01", "2024-10-01"],

    injection_volumes = [500, 500],
    withdrawal_volumes = [400, 600],

    max_storage = 1000,
    max_injection_rate = 600,
    max_withdrawal_rate = 600,

    storage_cost_per_unit = 0.15
)

print("Contract Value:", contract_val)
