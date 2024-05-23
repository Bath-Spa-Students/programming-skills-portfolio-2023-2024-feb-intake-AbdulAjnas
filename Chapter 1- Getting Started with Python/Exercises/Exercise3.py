from datetime import datetime

def display_current_date_time():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Display the date and time
    print("Current date and time:", current_time)

display_current_date_time()
