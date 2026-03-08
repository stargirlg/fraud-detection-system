def detect_fraud(transactions):
    fraud_list = []

    for amount in transactions:
        if amount > 10000:
            fraud_list.append(amount)

    return fraud_list


transactions = [200, 5000, 12000, 300, 25000, 700]

fraud_transactions = detect_fraud(transactions)

if fraud_transactions:
    print("Fraud Alert!")
    print("Suspicious Transactions:", fraud_transactions)
else:
    print("No fraud detected.")