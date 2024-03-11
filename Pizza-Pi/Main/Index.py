import math

# class used for taking user input and showing desired output
class pizza_pi():

    # constants for the minimum and maximum values
    minimum_pizza_diameter = 8
    maximum_pizza_diameter = 24

    # constants for Diameter limits for each size of pizza
    extra_small_diameter_limit = 12
    small_diameter_limit = 14
    medium_diameter_limit = 16
    large_diameter_limit = 20

    # float variable for the diameter of user's pizza
    pizza_diameter = 0.0

    # list for the Total amount of slices
    slices_possible = ()

    # fuction used to take user input 
    def user_input(self):
        self.pizza_diameter = float(input("Please enter the diameter of your pizza (0 to end program): "))

    # fuction used to check pizza diameter condition
    def exit_condition_check(self):
        if(self.pizza_diameter == 0):
            raise SystemExit
        if( not (self.pizza_diameter>= self.minimum_pizza_diameter <= self.maximum_pizza_diameter) ):
            raise SystemError

    # fuction used to calculate number of slices possible
    def slices_possible_check(self):
        if self.pizza_diameter < self.extra_small_diameter_limit:
            self.slices_possible = (6,)
        elif self.pizza_diameter < self.small_diameter_limit:
            self.slices_possible = (6,8)
        elif self.pizza_diameter < self.medium_diameter_limit:
            self.slices_possible = (6,8,10)
        elif self.pizza_diameter < self.large_diameter_limit:
            self.slices_possible = (6,8,10,12)
        else:
            self.slices_possible = (6,8,10,12,16)

    # fuction used to print user output
    def user_output(self):
        print(f"\nPizza Diameter: {self.pizza_diameter}\"")
        for pizza_slices in self.slices_possible:
            print(f"This Cuts {pizza_slices} slices and gives an area of {self.pizza_slice_area_calculator(self.pizza_diameter,pizza_slices):.2f}\" for each slice.")
        print("\n")
        
    # fuction used to calculate slice area
    def pizza_slice_area_calculator(self, pizza_diameter, number_of_slices):
        return (math.pi*(pizza_diameter/2)**2 )/number_of_slices

    # fuction to print user output
    def ErrorMeassage(self, error_message):
        print("\nENTRY ERROR.")
        print(error_message)
        print("Please try again.\n")

#main function of the P=program
def main(): 

    # pizza pi class object creation 
    pizza_pi_object = pizza_pi()  

    # loop for running the program until user want to terminate   
    while(True):
        try:  
            # taking user input  
            pizza_pi_object.user_input()

            # validating user input
            pizza_pi_object.exit_condition_check()

            #calculating number of possible slices
            pizza_pi_object.slices_possible_check()

            # displaying area of slice for all possible combination
            pizza_pi_object.user_output()

        # except to show error related to float conversion 
        except ValueError:
            pizza_pi_object.ErrorMeassage("Please enter suitable numeric value.")
            continue

        # except to show error related to min max value
        except SystemError:
            pizza_pi_object.ErrorMeassage("Pizza must have a diameter in the range of 12\" to 24\" inclusive.")
            continue

        # except to close the program
        except SystemExit:
            break

    # pizza pi class object deletion            
    del pizza_pi_object

#starting point of program 
if __name__ == "__main__":
    main()






