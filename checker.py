import numpy as np
import pandas as py
import matplotlib.pyplot as plt
df=py.read_csv("rawdata1.csv")
print(df.shape)
print(df.columns)
# counti=df["Target"].value_counts();
# print(type(counti))
# plt.bar(counti.index,counti.values)
# plt.xlabel("types in the target")
# plt.ylabel("the count of each type in the target")
# plt.show()
# plt.hist(df["Age of the patient"],bins=7,edgecolor="black")
# plt.xlabel("age gropus")
# plt.ylabel("count of the patients")
# plt.show()
# print(df["Age of the patient"].value_counts())
# print(df["Age of the patient"].describe())
# print(df["Age of the patient"].max())
# print(df["Age of the patient"].min())
# print(df["Age of the patient"].median())
# dftemp=df[["Target","Age of the patient"]]
# print(dftemp.groupby("Target").mean())
# print(dftemp.groupby("Target").agg([max,min,"median","std"]))   