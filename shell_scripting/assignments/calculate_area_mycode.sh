#!/bin/bash

pi=3.14159

option="$1"

display_help() {
    echo "Usage: $0 [option] [shape] [dimension1] [dimension2]"
    echo
    echo "Calculate the area of various geometric shapes."
    echo
    echo "Options:"
    echo "  -h           Display this help message."
    echo "  -i           Interactive mode."
    echo
    echo "Shapes and dimensions:"
    echo "  circle radius       Calculate the area of a circle."
    echo "  square side         Calculate the area of a square."
    echo "  rectangle length width  Calculate the area of a rectangle."
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
        ;;
    square)
        length=$2
        area=$(echo "$length * $length" | bc )
        echo "Area of the square: $area"
        ;;
    rectangle)
        length=$2
        width=$3
        area=$(echo "$length * $width " | bc )
        echo "Area of the rectangle: $area"
        ;;
                -i)
        echo "Choose the shape to calculate the area:"
		echo "1. Circle"
		echo "2. Square"
		echo "3. Rectangle"
        read -p "Enter your choice (1/2/3):" choice
        if [[ "$choice" == 1 ]]; then
            read -p "Enter the radius of the circle:" radius
            area=$(echo "$pi * $radius* $radius" | bc )
            echo "Area of the circle: $area"
        fi
        if [[ "$choice" == 2 ]]; then
            read -p "Enter the length of side of the square:" length
            area=$(echo "$length * $length" | bc )
            echo "Area of the square: $area"
        fi
        if [[ "$choice" == 3 ]]; then
            read -p "Enter the length of the rectangle:" length
            read -p "Enter the width of the rectangle:" width
            area=$(echo "$length * $width " | bc )
            echo "Area of the rectangle: $area"
        fi
        ;;
    *)
        echo "Invalid option! Try again."
		display_help
        ;;
esac