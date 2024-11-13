# a=$(find . -name "hi*")
# i=0

# for line in $a; do
#     echo "$line $i"
#     ((i++))
# done

# echo "####################    make hi$i"
# touch "hi$i"



num=0
i=0
found=$(find . -name "hi*")

while true; do
    exist=0
    for line in $found; do
        if [ "$line" == "./hi$i" ]; then
            echo "찾았다: $line"
            exist=1
            ((i++))
            break
        fi
    done
    if [ $exist -eq 0 ]; then
        num=$i
        break
    fi
done

echo "없는놈: hi$num"
touch "hi$num"