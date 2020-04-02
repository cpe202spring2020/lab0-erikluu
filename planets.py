def weight_on_planets():
   weight = int(input("What do you weigh on earth? "))
   
   # calcualtes your weight on Mars and Jupiter
   marsW = weight * .38
   jupiterW = weight * 2.34
   
   print("\nOn Mars you would weigh " + str(marsW) + " pounds." + "\nOn Jupiter you would weigh " + str(jupiterW) + " pounds.")
   
   
   
if __name__ == '__main__':
   weight_on_planets()
