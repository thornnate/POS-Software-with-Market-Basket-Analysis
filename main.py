from class_admin import *
from class_manager import *
from class_employee import *
from class_apriori import *
import maskpass


ch1 = 0
while(ch1 != 5): 
    print("\nLOGIN MENU")
    print(
        "1.ADMIN \n"
        "2.MANAGER \n"
        "3.EMPLOYEE \n"
        "4.Market Basket Analysis \n"
        "5.EXIT \n")
    ch1 = int(input("Enter your choice: "))

    if ch1 == 1:
        pswd = 'admin@123'
        password = maskpass.askpass()
        if pswd == password: 
            ch2 = 0
            while(ch2 != 8): 
                print()
                print("OPERATIONS MENU")
                print("1.Add Item \n"
                     "2.Delete Item \n"
                     "3.Update Item \n"
                     "4.Print Item List \n"
                     "5.Day Sale \n"
                     "6.Month Sale \n"
                     "7.Year Sale \n"
                     "8.EXIT \n")
                ch2 = int(input("Enter your choice: "))

                if ch2 == 1:
                    a1.add_item()
                elif ch2 == 2:
                    a1.delete_item()
                elif ch2 == 3:
                    a1.update_itm()
                elif ch2 == 4:
                    a1.it_list()
                elif ch2 == 5:
                    a1.day_sale()
                elif ch2 == 6:
                    a1.month_sale()
                elif ch2 == 7:
                    a1.year_sale()
                elif ch2 == 8:
                    break
                else:
                    print("\nPlease Enter Valid Choice.")
        
        else:
            print("\nIncorrect Password")
    
    elif ch1 == 2:
        pswd = 'man@123'
        password = maskpass.askpass()
        if pswd == password:
            ch3 = 0
            while(ch3 != 6): 
                print()
                print("OPERATIONS MENU")
                print("1.New Order \n"
                      "2.Delete Order \n"
                      "3.Edit Order \n"
                      "4.Print Bill \n"
                      "5.Day Sale \n"
                      "6.EXIT \n")
                ch3 = int(input("Enter your choice: "))

                if ch3 == 1:
                    m1.order()
                elif ch3 == 2:
                    m1.delete_order()
                elif ch3 == 3:
                    m1.edit_order()
                elif ch3 == 4:
                    m1.print_bill()
                elif ch3 == 5:
                    m1.day_sale()
                elif ch3 == 6:
                    break
                else:
                    print("\nPlease Enter Valid Choice.")

        else:
            print("\nIncorrect Password.")

    elif ch1 == 3:
        pswd = 'emp@123'
        password = maskpass.askpass()
        if pswd == password:
            ch4 = 0
            while(ch4 != 4): 
                print()
                print("OPERATIONS MENU")
                print("1.New Order \n"
                      "2.Edit Order \n"
                      "3.Print Bill \n"
                      "4.EXIT \n")
                
                ch4 = int(input("Enter your choice: "))

                if ch4 == 1:
                    e1.order()
                elif ch4 == 2:
                    e1.edit_order()
                elif ch4 == 3:
                    e1.print_bill()
                elif ch4 == 4:
                    break
                else:
                    print("\nPlease Enter Valid Choice.")
 
        else:
            print("\nIncorrect Password.")
        
    elif ch1 == 4:
        ap.market_basket_analysis()

    elif ch1 == 5:
        print("\nGOOD-BYE")
        break

    else:
        print("\nPlease Enter Correct Option.")
        