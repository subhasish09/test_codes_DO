import requests

def main():
    user_input = input("Enter 'hello': ").strip().lower()

    if user_input == 'hello':
        api_url = 'http://localhost:5000/'  # Replace with the actual Flask backend URL
        response = requests.post(api_url, json={'user_input': user_input})

        if response.status_code == 200:
            data = response.json()
            reply = data.get('reply', 'Unknown response')
            print(reply)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    else:
        print("Invalid input. Please enter 'hello'.")

if __name__ == '__main__':
    main()
