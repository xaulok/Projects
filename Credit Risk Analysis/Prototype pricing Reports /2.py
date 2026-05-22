def value_gas_storage_contract(
    injection_dates,
    withdrawal_dates,
    injection_volumes,
    withdrawal_volumes,
    max_storage,
    max_injection_rate,
    max_withdrawal_rate,
    storage_cost_per_unit
):
    
    inventory = 0
    contract_value = 0

    # ----- INJECTION -----
    for date, volume in zip(injection_dates, injection_volumes):

        if volume > max_injection_rate:
            raise ValueError("Injection rate exceeded")

        if inventory + volume > max_storage:
            raise ValueError("Storage capacity exceeded")

        price = predict_gas_price(date)

        purchase_cost = volume * price
        storage_cost = volume * storage_cost_per_unit

        contract_value -= (purchase_cost + storage_cost)
        inventory += volume


    # ----- WITHDRAWAL -----
    for date, volume in zip(withdrawal_dates, withdrawal_volumes):

        if volume > max_withdrawal_rate:
            raise ValueError("Withdrawal rate exceeded")

        if volume > inventory:
            raise ValueError("Not enough gas in storage")

        price = predict_gas_price(date)

        sale_revenue = volume * price

        contract_value += sale_revenue
        inventory -= volume

    return round(contract_value, 2)
