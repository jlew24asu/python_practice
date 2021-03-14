#Python stuff by Jeff Lewis

values = [43, 56, 67, 89, 45]
weights = [4, 8, 2, 2, 4]

weights_shares = []
for i in range(0, len(weights)):
    weights_shares.append(weights[i] / sum(weights))

print(weights_shares)

weightedValues = []
for i in range(0, len(values)):
    weightedValues.append(values[i] * weights_shares[i])

print(weightedValues)