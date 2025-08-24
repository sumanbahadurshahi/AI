data = [
    ["Person", "Covid", "Flu", "Fever"],
    [1, "yes", "yes", "yes"],
    [2, "no", "no", "no"],
    [3, "yes", "yes", "yes"],
    [4, "yes", "no", "yes"],
    [5, "no", "no", "no"]
]

def prob(col_name, val):
    header = data[0]
    col_idx = header.index(col_name)
    count = 0
    total = len(data) - 1
    for row in data[1:]:
        if row[col_idx] == val:
            count += 1
    return count / total

def prob_given(col_name1, val1, col_name2, val2):
    
    header = data[0]
    idx1 = header.index(col_name1)
    idx2 = header.index(col_name2)
    
    count_both = 0
    count_val2 = 0
    for row in data[1:]:
        if row[idx2] == val2:
            count_val2 += 1
            if row[idx1] == val1:
                count_both += 1
    if count_val2 == 0:
        return 0
    return count_both / count_val2

def naive_bayes_predict(flu_val, fever_val):
    # Classes for Covid: yes or no
    classes = ["yes", "no"]
    
    header = data[0]
    idx_covid = header.index("Covid")
    
    total = len(data) -1
    
    posteriors = {}
    for c in classes:
        
        prior = prob("Covid", c)
        
        likelihood_flu = prob_given("Flu", flu_val, "Covid", c)
    
        likelihood_fever = prob_given("Fever", fever_val, "Covid", c)
        
        posterior = prior * likelihood_flu * likelihood_fever
        posteriors[c] = posterior
        
    
    predicted_class = max(posteriors, key=posteriors.get)
    
    print(f"Given Flu={flu_val} and Fever={fever_val}, predicted Covid: {predicted_class}")
    print(f"Posterior probabilities: {posteriors}")
naive_bayes_predict("yes", "yes")
naive_bayes_predict("no", "no")
naive_bayes_predict("yes", "no")
