# POS-Software

**ABSTRACT** 
The objective of this project is to increase the speed of billing and have easy access to all the transactions however old they may be.

**EXISTING SYSTEM** 
The current systems used in restaurants and supermarkets are too complex for a new user to use and they can’t hold the records of much older transaction. Customers have to wait for quite a long time in queues for billing.

**PROPOSED SYSTEM** 
The system proposed works on a command line interface for faster transactions. Being a CLI it is easy to understand and use by new users. The records are stored using MYSQL in tables within a database and in a excel file too which can be used as a dataset for machine learning processes such as market basket analysis, etc. The bills are stored in a text file which can be accessed either by entering the bill number or by directly accessing the directory in which it has been saved. The software has been built with market basket analysis algorithm for the user to understand their sales better and set their outlet in a manner which can increase their sales. The project consists of four main modules and each module is password protected:

**Admin** 
Admin will add the products with their price and item number (for easy and faster access). He can modify or even delete the data i.e. item information. Admin can also fetch the item list, day sale, monthly sale and yearly sale.

**Manager** 
Manager is one of the employees so he can take orders, he can also edit the orders, print bill and most importantly delete an order if the customer wants to cancel the order. Manager can also check the day sale to tally the balance sheet.

**Employee** 
Employee can only place and modify orders and print the bill.

**Market Basket Analysis** 
This is a machine learning technique that uses apriori algorithm which uses association rule to find the dependency of one item on another. Using this algorithm supermarket owner/managers can increase their sales by better understanding customer purchasing pattern.

PROJECT-1/README.md at main · thornnate/PROJECT-
