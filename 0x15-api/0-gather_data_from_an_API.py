import requests
import sys

def get_employee_data(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()
        return user_data, todo_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

def display_todo_progress(employee_id, user_data, todo_data):
    employee_name = user_data['name']
    completed_tasks = [task['title'] for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"    {task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todo_data = get_employee_data(employee_id)
    display_todo_progress(employee_id, user_data, todo_data)

