
Destination = input("Enter your destination: ")
distance = float(input("Enter the distance to your destination (in miles): "))
gas_cost_per_gallon = float(input("Enter the cost of gas per gallon: $"))
fuel_efficiency = float(input("Enter your vehicle's fuel efficiency (in miles per gallon): "))
number_of_nights = int(input("enter number of nights you will stay: "))
average_hotel_cost_per_night = float(input("enter the average hotel cost per night: $"))
daily_food_budget = float(input("enter your daily food budget: $"))
gallons_needed = distance / fuel_efficiency
total_gas_cost = gallons_needed * gas_cost_per_gallon
total_hotel_cost = number_of_nights * average_hotel_cost_per_night
total_food_cost = (number_of_nights +1) * daily_food_budget
Grand_total_cost = total_gas_cost + total_hotel_cost + total_food_cost
print()
print("=== Road Trip Budget Planner ===")
print()
print(f"Destination: {Destination}")
print(f"Distance: {distance:.2f} miles")
print()
print( "--- Cost Breakdown ---")
print(f"Gas ({gallons_needed:.2f} gallons at ${gas_cost_per_gallon:.2f}/gallon): ${total_gas_cost:.2f}")
print(f"Hotel ({number_of_nights} nights at $ {average_hotel_cost_per_night:.2f}/night): ${total_hotel_cost:.2f}")
print(f"Food ({number_of_nights + 1} days at ${daily_food_budget:.2f}/day): ${total_food_cost:.2f}")
print("-" * 20)
print(f"Estimated Total: ${Grand_total_cost:.2f}")
