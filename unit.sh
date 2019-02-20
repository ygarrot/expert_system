for file in test/*
do
	python3 parse.py $file
	echo "\n\n"
done
