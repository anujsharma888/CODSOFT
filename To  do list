import streamlit as st
import csv

CSV_FILE = "tasks.csv"

def main():
    st.title("To-Do List")
    st.markdown(
         f'''
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?cs=srgb&dl=pexels-adrien-olichon-2387793.jpg&fm=jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         ''',
         unsafe_allow_html=True
     )

    task_list = load_tasks()

    task_input = st.text_input("Add a new task:")
    if st.button("Add"):
        if task_input != "":
            task_list.append(task_input)
            save_tasks(task_list)
            task_input = ""
            display(task_list)

    

    if st.button("Clear all tasks"):
           task_list.clear()
        save_tasks(task_list)
        display(task_list)        

def load_tasks():
  
    try:
        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)
            task_list = [row[0] for row in reader]
    except FileNotFoundError:
        task_list = []
    return task_list
def display(task_list):
    if len(task_list) == 0:
        st.write("No tasks added yet.")
    else:
        st.write("Current tasks:")
        for i, task in enumerate(task_list):
            st.write(f"{i+1}. {task}")
def save_tasks(task_list):
    """
    Save the tasks to the CSV file.
    """
    with open(CSV_FILE, "w", newline="") as f:
        f.truncate(0)
        writer = csv.writer(f)
        writer.writerows([[task] for task in task_list])

if __name__ == "_main_":
    main()
