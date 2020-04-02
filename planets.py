def weight_on_planets():
   weight = int(input("How much do you weigh on Earth?"))
   
   # calcualtes your weight on Mars and Jupiter
   marsW = weight * .38
   jupiterW = weight * 2.34
   
   print("\nOn Mars you would weigh " + marsW + " pounds." 
         + "\nOn Jupiter you would weigh " + jupiterW + " pounds.")
   
   
   
if __name__ == '__main__':
   weight_on_planets()
