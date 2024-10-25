#!/bin/bash

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

calculate_area() {
    local shape=$1
    local dim1=$2
    local dim2=$3

    case $shape in
        circle)
            echo "Area of the circle: $(echo "scale=2; 3.14159 * $dim1 * $dim1" | bc)"
            ;;
        square)
            echo "Area of the square: $(echo "scale=2; $dim1 * $dim1" | bc)"
            ;;
        rectangle)
            echo "Area of the rectangle: $(echo "scale=2; $dim1 * $dim2" | bc)"
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
    read -p "Enter your choice (1/2/3): " choice

    case $choice in
        1)
            read -p "Enter the radius of the circle: " radius
            calculate_area circle $radius
            ;;
        2)
            read -p "Enter the side length of the square: " side
            calculate_area square $side
            ;;
        3)
            read -p "Enter the length of the rectangle: " length
            read -p "Enter the width of the rectangle: " width
            calculate_area rectangle $length $width
            ;;
        *)
            echo "Invalid choice"
            ;;
    esac
}

if [ $# -eq 0 ]; then
    display_help
    exit 1
fi

while getopts "hi" opt; do
    case $opt in
        h)
            display_help
            exit 0
            ;;
        i)
            interactive_mode
            exit 0
            ;;
        *)
            display_help
            exit 1
            ;;
    esac
done

if [ $# -ge 2 ]; then
    shape=$1
    dim1=$2
    dim2=$3
    calculate_area $shape $dim1 $dim2
else
    display_help
    exit 1
fi