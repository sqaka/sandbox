from roboter.csv_writer import restaurant_to_csv
from roboter.suggester import suggest_checker
from roboter.textmaker import ask_name, show_name, show_goodbye


ask_name()
user_name = input("Enter: ")

suggest_checker()
show_name(user_name)

restaurant = input("Enter: ")
restaurant_to_csv(restaurant)

show_goodbye(user_name)