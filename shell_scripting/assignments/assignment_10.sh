#!/bin/bash
                pi=3.14159
log_file='/home/user/logs/calculate_area.log'

option="$1"

display_help() {    
    echo "Usage: $0 [-h] [-i] [--debug] [--logfile filename] [shape dimensions]"
    echo
    echo "Calculate the area of various geometric shapes."
    echo
    echo "Options:"
    echo "  -h           Display this help message."
    echo "  -i           Interactive mode."    echo "--debug Enable detailed debug logging."
    echo "--logfile Specify the file to log to."
    echo
    echo "Shapes and dimensions:"
    echo "  circle radius       Calculate the area of a circle."
    echo "  square side         Calculate the area of a square."
    echo "  rectangle length width  Calculate the area of a rectangle."
}

calculate_area() {
    local shape=$1
    local dim1=$2
    local dim2=$3

    case $shape in
            circle)
                area=$(echo "$pi * $dim1* $dim1" | bc )
                echo "Area of the circle: $area"
                ;;
            square)
                area=$(echo "$dim1* $dim1" | bc )
                echo "Area of the square: $area"
                ;;
            rectangle)
                area=$(echo "$dim1* $dim2" | bc )
                echo "Area of the rectangle: $area"
                ;;
            *)
                echo "Invalid shape: $shape"
                display_help
                exit 1
                ;;
    esac
}

interactive_mode() {

        echo "Choose the shape to calculate the area:"
        echo "1. Circle"
        echo "2. Square"
        echo "3. Rectangle"
        read -p "Enter your choice (1/2/3):" choice

        case $choice in
            1)
                read -p "Enter the radius of the circle:" radius
                calculate_area circle $radius
                echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the circle with radius $radius: $area" > $log_file
                ;;
            2)
                read -p "Enter the length of side of the square:" length
                calculate_area square $length
                echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the square with length of side $length: $area" > $log_file
                ;;
            3)
                read -p "Enter the length of the rectangle:" length
				                read -p "Enter the width of the rectangle:" width
                calculate_area rectangle $length $width
                echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the rectangle with length $length and width $width: $area" > $log_file
                ;;
            *)
                echo "Invalid option! Try again."
                display_help
                ;;
        esac
}


case $option in
        -h)
                    display_help
            exit 0
                        ;;
    circle)
        radius=$2
        area=$(echo "$pi * $radius* $radius" | bc )
        echo "Area of the circle: $area"
		echo "Area of the circle: $area"
        echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the circle with radius $radius: $area" > $log_file
        ;;
    square)
        length=$2
        area=$(echo "$length * $length" | bc )
        echo "Area of the square: $area"
        echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the square with length of side $length: $area" > $log_file
        ;;
    rectangle)
        length=$2
        width=$3
        area=$(echo "$length * $width " | bc )
        echo "Area of the rectangle: $area"
        echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the rectangle with length $length and width $width: $area" > $log_file
        ;;
    -i)
        interactive_mode
        exit 0
esac