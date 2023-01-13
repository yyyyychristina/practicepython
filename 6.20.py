def feet_to_steps(user_feet):   # Define your function here 
    user_steps = int(user_feet / 2.5)
    return user_steps
    

if __name__ == '__main__':
    user_feet = float(input())  # Type your code here.
    print(feet_to_steps(user_feet))
    
