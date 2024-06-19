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
fi

if [ $archetype == c ]
then
    cp /CLOVER/clover.cc $path/src/clover.cc
    cp /CLOVER/clover.h $path/src/clover.h
    cp /CLOVER/clover_tests.cc $path/src/clover_tests.cc
fi

if [ $archetype == n ]
then
    cp /NEAR/near.cc $path/src/near.cc
    cp /NEAR/near.h $path/src/near.h
    cp /NEAR/near_tests.cc $path/src/near_tests.cc
fi

python $path/install.py --clean-build --test