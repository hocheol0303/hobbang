i=0

find . -name "hi*" | while read line; do
    if [ "$line" == "./hi$i" ]; then
        # echo "$line hi$i"
        rm "hi$i"
        ((i++))
    fi
done