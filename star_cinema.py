class Star_Cinema:
    hall_list = []   
    
    def entry_hall(self,hall):
        self.hall_list.append(hall)         
        
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.__rows = rows
        self.__cols = cols
        self._hall_no = hall_no  
        super().entry_hall(hall_no)  
        
    def entry_show(self, id, movie_name, time): 
        self.show_list.append((id, movie_name, time ))   
       
        self.seats[id] =   [[j for j in range(self.__rows)] for i in range(self.__cols)]
        
    def book_seats(self, customer_name, phone_number, show_id, row, col):
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.show_id = show_id
        if show_id in self.seats:
            

            if(self.seats[show_id][row][col] != 'x'):
                    self.seats[show_id][row][col] = 'x'
                    print("                ")
                    print("SUCCESSFULLY BOOKED THE TICKET")
            elif(self.seats[show_id][row][col] == 'x'):
                    print("                ")
                    print("SORRY \nTHIS SEAT IS ALREADY BOOKED")
                   
                
         
       
        else:
           print("                               ")
           print("INVALID ID")
           
    def view_show_list(self):
        print("\n")
        print("CURRENTLY RUNNING : ")
        
        print("--------------------------------------------")
        for i in (self.show_list):
          print (f'MOVIE_ID : {i[0]}\nMOVIE NAME: {i[1]}\nTIME: {i[2]}\n')      
        print("--------------------------------------------")
    def view_available_seats(self, id):
              for i in (self.show_list):
                    if id in i:
                     print(f'\nMOVIE NAME: {i[1]}\nTIME: {i[2]}\n')


              flag = 1
              for i in (self.seats): 
                  
                 
                  if id in i:  
                      flag = 0
              
                      print("View Available Seats: ")  
             
                      for xx in self.seats[i]:
                        
                                print("                       ".join(map(str, xx)))
              if (flag == 1):
                     print("INVALID MOVIE ID")               



bijoy_hall = Hall(3,3,3)    
  
bijoy_hall.entry_show("abc121", "Black adam", "12 December 2022 8:30 PM")
bijoy_hall.entry_show("xyz123", "Avatar", "12 December 2022 5:30 PM")



print("WELCOME TO STAR CINEMA HALL")
while True:
    
    print("\n") 
    print("1.VIEW ALL SHOWS TODAY")
    print("2.VIEW AVAILABLE SEATS")
    print("3.BOOK SEATS")

    choice = int(input("ENTER YOUR CHOICE : "))
    
    if choice == 1:
        bijoy_hall.view_show_list()
    elif choice == 2:
        print("\n") 
        id = (input("ENTER MOVIE ID : "))
        bijoy_hall.view_available_seats(id)   
        print("\n") 
    elif choice == 3:
        print("\n") 
        customer_name = (input("ENTER YOUR NAME : "))
        phone_number = (input("ENTER YOUR PHONE NUMBER : "))
        show_id = (input("ENTER MOVIE ID : "))
        
        row = int(input("SELECT ROW : "))
        col = int(input("SELECT YOUR COL : "))
        bijoy_hall.book_seats(customer_name, phone_number, show_id, row, col)   
       
        print("\n")     
    else:
        print("")
        print("Closing......")
        break     
