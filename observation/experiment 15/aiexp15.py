class SimpleDecisionTree:
    def predict(self, features):
        
        petal_width = features[3]
        petal_length = features[2]

        if petal_width <= 0.8:
            return 0  
        else:
            if petal_width <= 1.75:
                if petal_length <= 4.95:
                    return 1 
                else:
                    return 2 
            else:
                return 2 


tree = SimpleDecisionTree()


test_samples = [
    [5.1, 3.5, 1.4, 0.2], 
    [6.0, 2.7, 5.1, 1.6],
    [6.3, 3.3, 6.0, 2.5]  
]

print("Decision Tree Predictions:\n")
for i, sample in enumerate(test_samples, 1):
    prediction = tree.predict(sample)
    print(f"Sample {i} {sample} ---> Predicted Class: {prediction}")
