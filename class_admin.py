import mysql.connector
import datetime
from tabulate import tabulate

# making connection to the user 
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'proj',
    password = 'proj123',
    database = 'project'
)

mc = mydb.cursor()

# create a date time instance
datetime = datetime.datetime.today()
# retrive date from date time instance  
date = datetime.date()
date = str(date)

# function to prevent empty values
def valid_input(text):
    not_valid = True
    res = ''
    while not_valid:
        res = input(text)
        res = res.strip()
        if res.split():  # if text is empty or only spaces, this creates an empty list evaluated as False
            not_valid = False
    return res

def valid_val(text):
    not_valid = True
    res = ''
    while not_valid:
        res = input(text)
        while res.isdigit() == False:
            res = input("Enter a valid number: ")
            if res.isdigit() == False:
                print("Wrong input.")
            else:
                break
        res = res.strip()
        a = res.split()
        if int(a[0]) not in range(1,):  # if input is less than or equal to 0, the function will keep on asking for an input
            not_valid = False
    return res

class admin:
        
    # adding items to the table menu
    def add_item(self):

        itm_no = valid_val("Enter number of the item: ")
        
        # check if it_no already exists
        sql_check = "select it_no from menu"
        mc.execute(sql_check)
        val = mc.fetchall()
        for i in val:
            for j in i:
                if int(itm_no) == j:
                    print("\nItem number already exists.")
                    return

        itm_name = valid_input("Enter name of the item: ")
        itm_price = valid_val("Enter price of the item: ")

        sql = "insert into menu (it_no,it_name,it_price) values (%s,%s,%s)"
        values = [(itm_no,itm_name,itm_price)]

        mc.executemany(sql,values)
        mydb.commit()
        print("\nItem added successfully.")

    # delete items from the table menu
    def delete_item(self):
        
        # check if it_no does not exists 
        itm_no = valid_val("Enter item number to delete: ")
        sql_check = "select it_no from menu"
        mc.execute(sql_check)
        value = mc.fetchall()

        # if table is empty    
        if value == []:
            print("\nMenu is Empty")

        if int(itm_no) not in value:
            print("Item not found")
        # delete only if value is present
        k = []
        for i in value:
            for j in i:
                k.append(j)
        if int(itm_no) not in k:
            print("\nItem does not exists.")
    
        else:    
            for i in value:
                for j in i:
                    if j == int(itm_no):
                        sql = "delete from menu where it_no = (%s)"
                        val = [(itm_no)]
                        mc.execute(sql,val)
                        mydb.commit()
            print("\nItem deleted successfully.")
            
    # function to update an item 
    def update_itm(self):

        itm_no = valid_val("Enter item number: ")
        
        # check if item does not exists
        sql_check = "select it_no from menu"
        mc.execute(sql_check)
        val = mc.fetchall()
        k = []
        for i in val:
            for j in i:
                k.append(j)
        if int(itm_no) not in k:
            print("\nItem does not exists.")
    
        else:
            new_name = valid_input("Enter updated name of item: ")
            new_price = float(valid_val("Enter updated pice of item: "))
            for i in val:
                for j in i:

                    sql1 = "update menu set it_name = (%s) where it_no = (%s)"
                    sql2 = "update menu set it_price = (%s) where it_no = (%s)"
                    updated_val1 = (new_name,itm_no)
                    updated_val2 = (new_price,itm_no)
                    mc.execute(sql1,updated_val1)
                    mc.execute(sql2,updated_val2)
                    mydb.commit()
            print("\nItem updated successfully.")

    # function to print list of item.
    def it_list(self):
        sql = "select * from menu"
        mc.execute(sql)
        val = mc.fetchall() 
        # prints the data in a tabular form
        print(tabulate(val, headers = ["Item_No","Item_Name","Item_Price"]))

    # function to fetch day sale.
    def day_sale(self):
        inp = input("Press '1' for current date else press enter: ")
        if inp == '1':
            temp = date.split('-')
            d = ''
            for i in temp:
                d += i
            sql = "select sum(sum) from orders where date = (%s)"
            mc.execute(sql,[d])
            sale = mc.fetchall()
            
            for i in sale:
                day_sale = i[0]
            if day_sale == None:
                day_sale = 0
            print("TOTAL SALE: " + str(day_sale))

        else:
            dt = valid_val("Enter date(YYYMMDD): ")
            sql = "select sum(sum) from orders where date = (%s)"
            if len(dt) != 8:
                print("Invalid Date")
                return
            mc.execute(sql,[dt])
            sale = mc.fetchall()

            for i in sale:
                day_sale = i[0]
            if day_sale == None:
                day_sale = 0
            print("TOTAL SALE: Rs." + str(day_sale))

    #  function for monthly sale
    def month_sale(self):
        month = valid_val("Enter Month(MM): ")
        if int(month) not in range(1,13):
            print("\nMonth does not exists.")
        else:
            month = "%" + "-" +  month + '-' + "%"
            sql = "select sum(sum) from orders where date like (%s)"
            mc.execute(sql,[month])
            sale = mc.fetchall()
            for i in sale:
                day_sale = i[0]
            if day_sale == None:
                day_sale = 0
            print("TOTAL SALE: " + str(day_sale),flush=True)

    #  function for yearly sale
    def year_sale(self):
        year = valid_val("Enter Year(YYYY): ")
        year = year + '-' + "%"
        sql = "select sum(sum) from orders where date like (%s)"
        mc.execute(sql,[year])
        sale = mc.fetchall()
        for i in sale:
            day_sale = i[0]
        if day_sale == None:
            day_sale = 0
        print("TOTAL SALE: " + str(day_sale),flush=True)


a1 = admin()
# a1.add_item()
# a1.delete_item()
# a1.update_itm()
# a1.it_list()
# a1.day_sale()
# a1.month_sale()
# a1.year_sale()