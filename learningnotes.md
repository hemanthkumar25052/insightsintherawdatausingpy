yesterday started with the data set and observed the age of the patients to understand which aged people frequenty falling ill and also what are the type of disease instructions given like no disease and low risk and high risk basically modes and then tried to compare with age groups like which age grp is observed frequenty in the low risk and high risk and other types(date 1st oct)
today in code a line which has python method called argg()
the method argg() is used  basically to write the things to apply one by one so here basically in code it was required to fin the min and max so i used i here when i write argg(min,max) it works but when i wrote argg(min,max,median) it shows error because median is not built in method it is imported from module or the library so we need to indicate using the string literals
basically why min max are why built in and why the median is not built in it is also the statistical nalaysis na 
because Python keeps its built-in namespace small and reserved for core operations. Single-Pass Efficiency: Finding the minimum or maximum value only requires looking at each item in a collection exactly once (\(O(n)\) time complexity). It uses very little memory. Universal Application: You can find the min or max of almost anything that can be compared—numbers, strings, dates, or custom objects. 
but
The median is a statistical metric, not a core language operation. Algorithmic Overhead: To find the median, Python traditionally has to sort the dataset first (\(O(n \log n)\) complexity) or use a specialized selection algorithm. Data-Type Sensitivity: Median calculations behave differently depending on whether your dataset has an odd or even number of items (requiring an average of the two middle numbers). This means it generally expects numeric data, whereas min and max work on text too. To use it in standard Python, you must import it from the standard library:
one more thing is that when we do group by 
dftemp = df[["Target", "Age of the patient"]]
groups = dftemp.groupby("Target")["Age of the patient"]
here the groups consists in the form of
├── No_Disease     → Age values
├── Low_Risk       → Age values
├── Moderate_Risk  → Age values
├── High_Risk      → Age values
└── Severe_Disease → Age values
the type of the group is not dataframe
its SeriesGroupBy that means each of them is a series , so basically a grp of