import requests
#Print menu
def print_menu():
   print("1. View item")
   print("2. Add to tracker")
   print("3. remove from tracker")
   print("4. View tracker")
   print("5. quit")
#view item function
def view_item():
   api_url = ('https://api.calorieninjas.com/v1/nutrition?query=')
   user_decision = input("What item do you want to know about")

   api_request =  requests.get(api_url + user_decision, headers={'X-Api-Key':'CdoUIla7W14Tqq8aMxcjhw==LPa05B9XMMLGbnGL'} )
   if api_request.status_code == 200:
      calories = api_request.json()
      calories_request = calories["items"][0]["calories"]
      print(calories_request)
   else: print("ERROR")



#add tracker#
def add_tracker(tracker):
   api_url = ('https://api.calorieninjas.com/v1/nutrition?query=')
   user_tracker = input("What do you want to add to the tracker")

   api_request =  requests.get(api_url + user_tracker, headers={'X-Api-Key':'CdoUIla7W14Tqq8aMxcjhw==LPa05B9XMMLGbnGL'} )
   if api_request.status_code == 200:
      calories = api_request.json()
      calories_request = calories["items"][0]["calories"]

      rounded_calories = round(calories_request)
      
      tracker.append(rounded_calories)
      
      print("Calories added to tracker:")


   else:
      
      print('error')



#view list#

         #add an option where your able to add all calories

   




#remove from tracker
def remove_tracker(tracker):
   
   
   
   if not tracker: print('you dont have anything in the tracker')
   
   else:
      view_tracker(tracker)
      user_remove = int(input("What do you want removed")) - 1
      if 0 <= user_remove and user_remove < len(tracker):
         tracker.pop(user_remove)
         print('Calorie part removed')
         
      else:
         print("error")
   



#view tracker#

def view_tracker(tracker):
   if not tracker: print("you dont have any calories added")

   else:
      print(tracker)
      total = 0
      for item, tracker in  enumerate(tracker, start=1):
      
         
            print (f"{item}. {total + tracker}" )
      

#create main by making a loop and also connect to api in main

def main():
   tracker = []
   
   while True:

      print_menu()
      
      

      user_choice = input("Choose one")

      if user_choice == "1":
         view_item()
      elif user_choice == "2":
         add_tracker(tracker)
      elif user_choice == "3":
         remove_tracker(tracker)
      elif user_choice == "4":
         view_tracker(tracker)
      elif user_choice =="5":
         break
     
      
    
if __name__ == "__main__":
 main() 


