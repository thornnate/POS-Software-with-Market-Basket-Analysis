import mysql.connector
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd

# making connection to the user 
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'proj',
    password = 'proj123',
    database = 'project'
)

mc = mydb.cursor()

class apriori_algo:    

    # market basket analysis
    def market_basket_analysis(self):
        # converting database to dataframe
        df = pd.read_excel(r"C:\Users\LENEVO\Desktop\PROJECT\data_set.xlsx")
    
        basket = (df.fillna(0))
        # placing 1 for items bought and 0 for items not bought
        def encode_units(x):
            if isinstance(x,str):
                return 1
            else:
                return 0

        basket_sets = basket.applymap(encode_units)
        # generating frequent itemsets
        frequent_itemsets = apriori(basket_sets, min_support=0.1, use_colnames=True)
        # initialising minimum support, confidence and lift
        rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.5)
        # rules = rules[(rules['lift'] >= 1.0) & (rules['confidence'] >= 0.6 )]
        rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])
        print(rules)
        print()

ap = apriori_algo()
# ap.market_basket_analysis()