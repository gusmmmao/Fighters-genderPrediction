# from sklearn import tree
# from sklearn import discriminant_analysis
from sklearn import naive_bayes

# [height, weight, arm length]
# data was taken from the individual wikipedia of each ufc fighter on the rank (06/04/24)
X = [
    [177, 70, 179], [193, 112, 214], [182, 77, 187], [193, 93, 200], [170, 66, 175], [180, 61, 182], [177, 70, 188],
    [168, 66, 182], [185, 83, 193], [165, 57, 170], [165, 56, 168], [163, 52, 160], [165, 56, 170], [170, 57, 165],
    [168, 61, 175], [163, 57, 168], [170, 61, 171], [165, 57, 165], [165, 52, 167], [165, 52, 160]
]
Y = [
    'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male',
    'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female'

]

clf = naive_bayes.GaussianNB()
# clf = discriminant_analysis.LinearDiscriminantAnalysis()
# clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

height = int(input('Altura: '))
weight = int(input('Peso: '))
arm_length = int(input('Envergadura: '))

prediction = clf.predict([[height, weight, arm_length]])
print(prediction)