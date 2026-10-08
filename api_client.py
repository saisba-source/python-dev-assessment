
import requests


def fetch_and_display_users(num_users):
    """Fetch sample contacts and display their details."""
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(
                f"Request failed with status code: "
                f"{response.status_code}"
            )
            return

        users = response.json()

        if not isinstance(users, list):
            print("Unexpected response: expected a list of contacts.")
            return

        for user in users[:num_users]:
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]

                print(f"Contact: {name}")
                print(f"Email address: {email}")
                print(f"Home city: {city}")
                print("-" * 35)

            except (KeyError, TypeError):
                print("Skipping a contact with incomplete details.")

    except requests.exceptions.RequestException as error:
        print(f"Could not connect to the API: {error}")
    except ValueError:
        print("The API returned invalid JSON data.")


# Test with four contacts
print("=== Contact Directory ===")
fetch_and_display_users(4)

# Test requesting more contacts than may be available
print("\n=== Extended Contact Directory ===")
fetch_and_display_users(16)
