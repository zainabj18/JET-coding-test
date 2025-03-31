
# module to make HTTP requests with 
import requests
import random

# fetching restaurant data using a postcode 
def get_restaurants(postcode):
    restaurant_url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    
    #necessary HTTP header to avoid 403 forbidden error 
    user_agent_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    
    #GET request to the API
    api_response = requests.get(restaurant_url, headers=user_agent_header)
    
    #checking if the HTTPS response code is OK 200 (successful request)
    if api_response.status_code == 200:
        #returning the restaurants data from the response (JSON)
        restuarant_data = api_response.json()
        return restuarant_data.get('restaurants', [])
    else:
        #if unable to fetch restaurants data, prints the error code 
        print(f"Error retrieving restaurant data: {api_response.status_code}")
        return []
    

#printing the restaurant details 
def print_restaurant_data(postcode, sort_by):
    #getting the restaurant data 
    restaurants = get_restaurants(postcode)
    
    #if restaurants exists, print data
    if restaurants:
        
        #filtering to focus on restaurant data only
        restaurant_focused_keywords = ['Food', 'Drink', 'Dessert', 'Bakery', 'Breakfast', 'Sandwiches', 'Restaurant', 'Pizza', 'Burger', 'Sushi', 'Cafe', 'Bar', 'Grill', 'Italian', 'Kebab']
        #looping through the restaurants list and checking if food related words are found 
        restaurants_filtered = [ restaurant for restaurant in restaurants
                                if any(
                                    #comparing the food keywords 
                                    food_keyword.lower() in cuisine['name'].lower()
                                    for cuisine in restaurant.get('cuisines', [])
                                    for food_keyword in restaurant_focused_keywords
                                    )
                                ]
        #sorting and displaying as user's choice 
        if sort_by == "rating":
            restaurants_filtered.sort(key=lambda x: x.get('rating', {}).get('starRating', 0), reverse=True)
        elif sort_by == "random":
            random.shuffle(restaurants_filtered)
            
            
        #only fetching the firts 10 
        for restaurant in restaurants_filtered[:10]:  
            #extracting the 4 restaurants data points 
            restaurant_name = restaurant.get('name', 'Name not found')   
            
            #getting the list of cuisines and extracting the names of cuisines into a list
            cuisine_data = restaurant.get('cuisines', [])
            #using .join for better readability 
            cuisine = ', '.join(cuisine['name'] for cuisine in cuisine_data) if cuisine_data else 'Cuisine not found.'
            
            #extracting the rating 
            rating_info = restaurant.get('rating', {})
            rating = f"{rating_info.get('starRating', 'Rating not found.')} ({rating_info.get('count', 0)} reviews)"
            
            #extracting the address 
            address_info = restaurant.get('address', {})
            address = f"{address_info.get('firstLine', 'Address not found.')}, {address_info.get('city', 'City not found.')}, {address_info.get('postalCode', 'Post code not found.')}"

            print(f'\033[1m' + 'Name: ' + '\033[0m' + f"{restaurant_name}")
            print('\033[1m' + 'Cuisines: ' + '\033[0m' + f"{cuisine}")
            print('\033[1m' + 'Rating: ' + '\033[0m' + f"{rating}")
            print('\033[1m' + 'Address: ' + '\033[0m' + f"{address}\n")
    else:
        print(f"No restaurants found.")

if __name__ == '__main__':
    #user inputs postcode 
    postcode = input("Enter a UK postcode: ")
    sort_by_choice = input("Would you like to sort the restaurants by rating or random? Enter '1' for rating or '2' for random: ").strip().lower()
    if sort_by_choice == "1":
        sort_by = "rating"
    elif sort_by_choice == "2":
        sort_by = "random"
    print_restaurant_data(postcode, sort_by)
