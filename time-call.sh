#!/bin/bash
rm sample.txt
touch sample.txt
end=$((SECONDS+5))
while [ $SECONDS -lt $end ]; do
	echo "$(date)" >> sample.txt && /bin/python3 http-rest.py >> sample.txt
done


