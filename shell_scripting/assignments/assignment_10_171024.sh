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
    echo "  -i           Interactive mode."
    echo "--debug Enable detailed debug logging."
    echo "--logfile Specify the file to log to."    echo
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

debug() {
    shape=$2
    dim1=$3
    dim2=$4
    echo "debug:: $shape $dim1 $dim2"
    calculate_area $shape $dim1 $dim2
    if [[ "$shape" == "circle" ]]; then
                echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the circle with radius $radius: $area" > $log_file
    elif [[ "$shape" == "square" ]]; then
                echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the square with length of side $length: $area" > $log_file
    elif [[ "$shape" == "rectangle" ]]; then
                echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the rectangle with length $length and width $width: $area" > $log_file
    fi
    echo "debug mode ends here..."
    exit 0

}


# This is to check if the arguments passed are more than one.
if [ $# -eq 0 ]; then
#    echo "at line 87, exiting...."
    display_help
            exit 1
fi


while [ "$1" != "" ];
do
   case $1 in
    -h)
         echo "display usage.... @118"
         display_help
         exit 0
         ;;

    -i)
         echo "interactive mode usage.... @124"
         interactive_mode
         exit 0
         ;;
    -d|--debug)
        #echo "debug mode on..."
        #debug
        shape=$2
        dim1=$3
        dim2=$4
        #echo "@134 Debug:: $shape, $dim1, $dim2"
        calculate_area $shape $dim1 $dim2
        if [[ "$shape" == "circle" ]]; then
                    echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the circle with radius $dim1: $area" > $log_file
        elif [[ "$shape" == "square" ]]; then
                    echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the square with length of side $dim1: $area" > $log_file
        elif [[ "$shape" == "rectangle" ]]; then
                    echo "[$(date +"%Y-%m-%d %H:%M:%S")] [INFO] :: Calculated area of the rectangle with length $dim1 and width $dim2: $area" > $log_file
        fi
        exit 0
        ;;
    -l|--logfile)
        echo "logfile mode is on..."
        ;;
     *)
        display_help
        exit 1;;
   esac
shift
done