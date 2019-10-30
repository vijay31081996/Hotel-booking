#write a program to execute hotel bookings

class hotelbooking:

    def __init__(self, rt='',rr=0,fb=0,lb=0,a=1800, name='', address='', cindate='', coutdate='', rno=201, ):

        print("                      *****   WELCOME TO THE MALASIYAN HOTEL   *****      ")
        self.rt = rt

        self.rr = rr



        self.fb = fb

        self.lb = lb

        self.a = a

        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nEnter your name:")
        self.address = input("\nEnter your address:")
        self.cindate = input("\nEnter your check in date:")

        print("your booking date is not available")
        self.cindate = input("\nEnter your Another check in date:")
        self.coutdate = input("\nEnter your checkout date:")
        print("Your room no.:", self.rno, "\n")


    def roomrent(self):  # sel1353

      print("We have the following rooms for you:-")

      print("1.  type A-(LARGE-3BEDROOM)--->rs 6000 PN\-")

      print("2.  type B-(MEDIUM-2 BEDROOM)--->rs 5000 PN\-")

      print("3.  type C-(SMALL-1-BEDROOM)--->rs 4000 PN\-")

      x = int(input("Enter Your Choice Please->"))

      n = int(input("For How Many Nights Did You Stay:"))


      if (x == 1):

        print("you have opted room type A")

        self.rr= 6000 * n

      elif (x == 2):

         print("you have opted room type B")

         self.rr= 5000 * n

      elif (x == 3):

         print("you have opted room type C")

         self.rr = 4000 * n


      else:

         print("please choose a room")

         print("your room rent is =", self.s, "\n")


    def restaurentbill(self):
         print("*****RESTAURANT MENU*****")

         print("1.water----->Rs20", "2.tea/Coffee----->Rs10", "3.breakfast combo1/combo2--->Rs90", "4.lunch---->Rs110", "5.dinner--->Rs150",
          "6.Exit")

         while (1):

          c = int(input("Enter your choice:"))

          if (c == 1):
            d = int(input("Enter the quantity:"))
            self.fb = self.fb + 20 * d

          elif (c == 2):
            d = int(input("Enter the quantity:"))
            self.fb = self.fb + 10 * d

          elif (c == 3):
            d = int(input("Enter the quantity:"))
            self.fb = self.fb + 90 * d

          elif (c == 4):
            d = int(input("Enter the quantity:"))
            self.fb = self.fb + 110 * d

          elif (c == 5):
            d = int(input("Enter the quantity:"))
            self.fb = self.fb + 150 * d

          elif (c == 6):
             break;
          else:
            print("Invalid option")

            print("Total food Cost=Rs", self.r, "\n")


    def laundrybill(self):
         print("******LAUNDRY MENU*******")

         print("1.Shorts----->Rs5", "2.Trousers----->Rs8", "3.Shirt--->Rs10", "4.Jeans---->Rs12", "5.Exit")

         while (1):
         # brought to you by code-projects.org

             e = int(input("Enter your choice:"))

             if (e == 1):
              f = int(input("Enter the quantity:"))
              self.lb = self.lb + 5 * f

             elif (e == 2):
              f = int(input("Enter the quantity:"))
              self.lb = self.lb + 8 * f

             elif (e == 3):
               f = int(input("Enter the quantity:"))
               self.lb = self.lb + 10 * f

             elif (e == 4):
               f = int(input("Enter the quantity:"))
               self.lb = self.lb + 12 * f

             elif (e == 5):
               break;
             else:

               print("Invalid option")

               print("Total Laundary Cost=Rs", self.lb, "\n")



    def display(self):
        print("******HOTEL BILL******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check in date:", self.cindate)
        print("Check out date", self.coutdate)
        print("Room no.", self.rno)
        print("Your Room rent is:", self.rr)
        print("Your Food bill is:", self.fb)
        print("Your laundary bill is:", self.lb)


        self.rt = self.rr + self.fb + self.lb

        print("Your sub total bill is:", self.rt)
        print("Additional Service Charges is", self.a)
        print("Your grandtotal bill is:", self.rt + self.a, "\n")
        self.rno += 1


def main():
    a = hotelbooking()

    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate rommrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Show total cost")

        print("6.EXIT")

        b = int(input("\nEnter your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):
            a.roomrent()

        if (b == 3):
            a.restaurentbill()

        if (b == 4):
            a.laundrybill()


        if (b == 5):
            a.display()

        if (b == 6):
            quit()

main()



#user will provide number of adults


#date,room type-S,M,L


#Confirmation


#if dates are already booked,Then show its not available