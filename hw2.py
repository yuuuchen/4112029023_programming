books = []

def add_book():
    name = input("請輸入要新增的書籍:")
    price = input("請輸入新增書籍的價錢:")
    quantity = int(input("請輸入書籍庫存: "))
    book = {"書名":name, "價格":price, "庫存":quantity}
    books.append(book)
    print(f"書籍'{name}'已成功添加到庫存!")
    
def remove_book():
    name = input("請輸入要移除的書籍:")
    for book in books:
        if book["書名"] == name:
            books.remove(book)
            print(f"書籍'{name}'已成功從庫存中移除!")
        
 
def update_book():
    name = input("請輸入要更新的書籍:")
    new_quantity = int(input("請輸入書籍新的庫存: "))
    for book in books:
        if book["書名"] == name:
           book["庫存"] = new_quantity
           print(f"書籍'{name}'的庫存已更新為{new_quantity}本!")
 
def display_books():
   print("\n當前庫存:")
   for book in books:
       print(f"書名:{book['書名']},\t價格:{book['價格']},\t庫存:{book['庫存']}")


def main():
    while True:
       print("1.新增書籍" "\n2.移除書籍" "\n3.更新庫存" "\n4.顯示庫存" "\n5.退出")
       choice = int(input("請選擇要進行的動作:"))  
       
       if choice == 1:
         add_book()
    
       elif choice == 2:
         remove_book()
    
       elif choice == 3:
         update_book()
    
       elif choice == 4:
         display_books()
        
       elif choice == 5:
         break
        
       else:
         print("無效的選擇，請重新選擇")
        

if __name__ == "__main__":
    main()

print("\n當前庫存:")
for book in books:
    print(f"書名:{book['書名']},\t價格:{book['價格']},\t庫存:{book['庫存']}")
    
order = []

def order_book():
    name = input("請輸入要訂購的書籍:")
    quantity = int(input("請輸入訂購數量:"))
    item = {"書名": name , "數量":quantity}
    order.append(item)
    
while True:
    buy = input("是否有要購買的書籍(yes/no):")
    if buy == ("no"):
        break
    elif  buy == ("yes"):
       order_book()
          
print("\n訂購清單:")
for item in order:
    print(f"書名:{item['書名']},\t數量:{item['數量']}")
    
total_amount = 0 
for item in order:
    for book in books:
        if item["書名"] == book["書名"]:
            total_amount +=  int(book["價格"]) * int(item["數量"])
      
if total_amount > 500:
    discount = 0.1
    total_amount = total_amount * (1 - discount)
    print(f"恭喜!您獲得了10%的折扣，總金額為:{total_amount}元")
else:
    print(f"您的總金額為:{total_amount}元")

