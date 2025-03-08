# Import necessary libraries
import streamlit as st  # Streamlit for creating the web app
import random  # For generating random passwords
import string  # For string operations

# Function to check password strength
def check_password_strength(password):
    strength = 0
    
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        strength += 1
    
    # Check if password contains at least one uppercase letter
    if any(char.isupper() for char in password):
        strength += 1
    
    # Check if password contains at least one lowercase letter
    if any(char.islower() for char in password):
        strength += 1
    
    # Check if password contains at least one digit
    if any(char.isdigit() for char in password):
        strength += 1
    
    # Check if password contains at least one special character
    if any(char in '!@#$%^&*()' for char in password):
        strength += 1
    
    # Return strength level
    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        return "Strong"
    elif strength >= 2:
        return "Moderate"
    else:
        return "Weak"

# Function to generate a random password
def generate_password(length=12):
    # Define character sets
    characters = string.ascii_letters + string.digits + '!@#$%^&*()'
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit app layout

# Set the title of the app
st.title("Simple Password Strength Checker and Generator")

def main():

    # Add a sidebar for features and developer details
    st.sidebar.title("About This App")
    st.sidebar.write("""
    ### Features:
    - **Password Strength Checker**:\n
        Check how strong your password is based on:\n
        - Length (at least 8 characters).\n
        - Presence of uppercase letters.\n
        - Presence of lower letters.\n
        - Presence of digits and\n
        - Presence of special characters.\n
    - **Password Generator**:\n
        Generate a strong, random password with customizable length.\n
    
    ### Created By:
        - Name: Muhammad Adnan
        - Email: dononlineboss@gmail.com
        - Contact: 0321-2121147 
    """)
    
# Main app functionality
# Create tabs for checker and generator
tab1, tab2 = st.tabs(["Check Password", "Generate Password"])

    # Password strength checker
with tab1:
    st.write("Check the strength of your password.")
    st.header("Check Password Strength")
    password = st.text_input("Enter your password", type="password")
    st.button("Check Strength")
    
    if password:
        strength = check_password_strength(password)
        st.write(f"Password Strength: **{strength}**")
        
        if strength == "Very Strong":
            st.success("Your password is very strong! Good job.")
        elif strength == "Strong":
            st.info("Your password is strong, but it could be better.")
        elif strength == "Moderate":
            st.warning("Your password is moderate. Consider making it stronger.")
        else:
            st.error("Your password is weak. Please choose a stronger password.")

# Password generator
with tab2:
    st.write("Generate a strong Password.")
    
    st.header("Generate a Strong Password")
    length = st.slider("Select password length", min_value=8, max_value=20, value=12)
    
    if st.button("Generate Password"):
        generated_password = generate_password(length)
        st.write(f"Generated Password: `{generated_password}`")

# Run the Streamlit app
if __name__ == "__main__":
    main()