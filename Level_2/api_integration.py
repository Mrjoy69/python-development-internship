import requests


def fetch_task(task_id):

    url = f"https://jsonplaceholder.typicode.com/todos/{task_id}"

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status() 

        task = response.json()

        if not isinstance(task, dict):
            print("Error: The API returned unexpected data format.")
            return

        if not all(key in task for key in ["id", "title", "completed"]):
            print("Error: The API response is missing expected fields.")
            return

        print("API request successful!")
        print("Status Code:", response.status_code)
        print("Task ID:", task["id"])
        print("Task Title:", task["title"])
        print("Completed:", task["completed"])

    except requests.exceptions.Timeout:
        print("Error: The request took too long. Please try again later.")

    except requests.exceptions.ConnectionError:
        print("Error: Failed to establish a connection. Please check your internet connection.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except requests.exceptions.RequestException as error:
        print(f"An unexpected error occurred: {error}")

    except ValueError:
        print("Error: The API returned invalid JSON data.")


def main():

    print("Welcome to the Task Fetcher!")

    try:

        task_id = int(input("Please enter the task ID (1-200): "))

        if task_id < 1 or task_id >200:
            print("Error: Task ID must be between 1 and 200.")
            return

        fetch_task(task_id)

    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()
    