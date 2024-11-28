import requests  # Import the requests library to make HTTP requests
from time import sleep

def fetch_json_data():
    # URL of the open-source API
    url = "https://jsonplaceholder.typicode.com/posts"

    # Make a GET request to fetch the raw JSON data
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        json_data = response.json()
        return json_data
    else:
        # If the request failed, print the status code
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
        return None

def main():
    # Fetch JSON data from the API
    data = fetch_json_data()

    # Check if data was fetched successfully
    if data:
        # Loop 1000 times to print the data
        for i in range(20):
            print(f"--- Iteration {i+1} ---")
            # Print each post's details in the loop
            for post in data:
                print(f"ID: {post['id']}")
                print(f"Title: {post['title']}")
                print(f"Body: {post['body']}")
                print("-" * 40)  # Separator between posts for better readability
                sleep(1)
    else:
        print("No data to display.")

# Execute the main function
if __name__ == "__main__":
    main()