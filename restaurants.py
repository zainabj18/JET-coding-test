
# module to make HTTP requests with 
import requests


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
        print(f"Error retrieving restuarant data: {api_response.status_code}")
        return []


#printing the restaurant details 
def print_restaurant_data(postcode):
    #getting the restaurant data 
    restaurants = get_restaurants(postcode)
    
    #if restaurants exists, print data
    if restaurants:
        
        #only fetching the firts 10 
        for restaurant in restaurants[:10]:  
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

            print(f"Name: {restaurant_name}")
            print(f"Cuisines: {cuisine}")
            print(f"Rating: {rating}")
            print(f"Address: {address}\n")
    else:
        print(f"No restaurants found.")

if __name__ == '__main__':
    #user inputs postcode 
    postcode = input("Enter a UK postcode: ")
    print_restaurant_data(postcode)
