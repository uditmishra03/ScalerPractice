#!/bin/bash

LOG_LEVEL="INFO"
LOG_FILE="/home/user/logs/calculate_area.log"

log_message() {
    local log_level="$1"
    local message="$2"
    local log_file="${3:-$LOG_FILE}" # Use default log file if not specified

    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$log_level] :: $message" >> "$log_file"
}

display_help() {
    echo "Usage: $0 [-h] [-i] [--debug] [--logfile filename] [shape dimensions]"
    echo
    echo "Calculate the area of various geometric shapes."
    echo
    echo "Options:"
    echo "  -h        Display this help message."
    echo "  -i        Interactive mode."
    echo "  --debug   Enable detailed debug logging."
    echo "  --logfile Specify the file to log to."
    echo
    echo "Shapes:"
    echo "  circle radius           Calculate the area of a circle."
    echo "  square side             Calculate the area of a square."
    echo "  rectangle length width  Calculate the area of a rectangle."
}

calculate_circle() {
    local radius="$1"
    local area=$(echo "3.14159 * $radius * $radius" | bc -l)
    log_message "INFO" "Calculated area of the circle with radius $radius: $area"
    echo "The area of the circle is $area square units."
}

calculate_square() {
    local side="$1"
    local area=$(echo "$side * $side" | bc)
    log_message "INFO" "Calculated area of the square with side $side: $area"
    echo "The area of the square is $area square units."
}

calculate_rectangle() {
    local length="$1"
    local width="$2"
    local area=$(echo "$length * $width" | bc)
    log_message "INFO" "Calculated area of the rectangle with length $length and width $width: $area"
    echo "The area of the rectangle is $area square units."
}

while [[ "$1" =~ ^- && ! "$1" == "--" ]]; do case $1 in
  -h | --help )
    display_help
    exit
    ;;
  -i | --interactive )
    INTERACTIVE_MODE=1
    ;;
  --debug )
    LOG_LEVEL="DEBUG"
    ;;
  --logfile )
    shift; LOG_FILE="$1"
    ;;
esac; shift; done
if [[ "$1" == '--' ]]; then shift; fi

interactive_mode() {
    echo "Select the type of area to calculate:"
    echo "1. Circle"
    echo "2. Square"
    echo "3. Rectangle"
    read -p "Enter choice: " choice

    case $choice in
        1)
            read -p "Enter the radius: " radius
            calculate_circle $radius
            ;;
        2)
            read -p "Enter the side length: " side
            calculate_square $side
            ;;
        3)
            read -p "Enter the length: " length
            read -p "Enter the width: " width
            calculate_rectangle $length $width
            ;;
        *)
            echo "Invalid choice."
            exit 1
            ;;
    esac
}

if [[ "$INTERACTIVE_MODE" == "1" ]]; then
    interactive_mode
else
    case $1 in
        circle)
            calculate_circle $2
            ;;
        square)
            calculate_square $2
            ;;
        rectangle)
            calculate_rectangle $2 $3
            ;;
        *)
            display_help
            ;;
    esac
fi