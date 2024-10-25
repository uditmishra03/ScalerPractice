#!/bin/bash

# Function to check password strength
check_password_strength() {
    local password="$1"
    local length=${#password}
    
    # Initialize flags
    local has_upper=false
    local has_lower=false
    local has_digit=false
    local has_special=false
    local has_space=false

    # Check each character in the password
    for (( i=0; i<length; i++ )); do
        char="${password:i:1}"
        
        if [[ "$char" =~ [A-Z] ]]; then
            has_upper=true
        elif [[ "$char" =~ [a-z] ]]; then
            has_lower=true
        elif [[ "$char" =~ [0-9] ]]; then
            has_digit=true
        elif [[ "$char" =~ [^A-Za-z0-9] ]]; then
            has_special=true
            # Additional check for space
            if [[ "$char" == " " ]]; then
                has_space=true
            fi
        fi
    done

    # If the password contains spaces, it's automatically weak
    if $has_space; then
        echo "Weak password: It contains spaces."
        return
    fi

    # Check for strong password
    if [[ "$length" -ge 12 ]] && $has_upper && $has_lower && $has_digit && $has_special; then
        echo "Strong password."

    # Check for moderate password (8-11 characters, but all conditions met)
    elif [[ "$length" -ge 8 && "$length" -le 11 ]] && $has_upper && $has_lower && $has_digit && $has_special; then
        echo "Moderate password."

    # Otherwise, it's a weak password
    else
        echo "Weak password."
    fi
}

# Read password from user
read -sp "Enter a password: " user_password
echo  # For a new line

# Check the password strength
check_password_strength "$user_password"
