# cron이라고 주기적으로 실행하게 만드는 명령어 있는데 작업 끝날 때마다 특정 파일 생성하게 만들어서 다음 작업 실행하도록 할 수 있겠다 싶어요~

a=$(find . -name "hi*")

i=(0)
for line in $a; do
    echo "$line"
    echo "$i"
    ((i++))
done

# echo "${a[0]}" # 0번에 모든 결과가 담겨있네

# /Volumes/horive/ai/boostcamp/project/cv13/hi/hi라는 파일이 존재하면 통과
if [ -f ./hi0 ]; then
    # 첫 번째 작업이 완료되었다면 두 번째 작업 실행
    echo '안녕안녕 나는 지슈야~'
    echo "./hi0 있어서 출력되었지~"
else
    echo "First task not completed."
fi
