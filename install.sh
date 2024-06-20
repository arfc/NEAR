# find cycamore
echo "Give me the relative path to Cycamore"
read -p "> " path

# select archetype
echo "Which archetype would you like to build? [EVER = e, CLOVER = c, NEAR = n]"
read -p "(e/c/n): " archetype
echo "Ok, I will build that right away!"

if [ $archetype == e ]
then
    cp /EVER/ever.cc $path/src/ever.cc
    cp /EVER/ever.h $path/src/ever.h
    cp /EVER/ever_tests.cc $path/src/ever_tests.cc
    sed -i '' '/\USE_CYCLUS("cycamore" "reactor")/a\
    USE_CYCLUS("cycamore" "ever") \
    ' $path/CMakeLists.txt
fi

if [ $archetype == c ]
then
    cp /CLOVER/clover.cc $path/src/clover.cc
    cp /CLOVER/clover.h $path/src/clover.h
    cp /CLOVER/clover_tests.cc $path/src/clover_tests.cc
    sed -i '' '/\USE_CYCLUS("cycamore" "reactor")/a\
    USE_CYCLUS("cycamore" "clover") \
    ' $path/CMakeLists.txt
fi

if [ $archetype == n ]
then
    cp /near.cc $path/src/near.cc
    cp /near.h $path/src/near.h
    cp /near_tests.cc $path/src/near_tests.cc
    sed -i '' '/\USE_CYCLUS("cycamore" "reactor")/a\
    USE_CYCLUS("cycamore" "near") \
    ' $path/CMakeLists.txt
fi

python $path/install.py --clean-build --test