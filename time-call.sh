#!/bin/bash
rm sample.txt
touch sample.txt
end=$((SECONDS+600))
while [ $SECONDS -lt $end ]; do
	echo "$(date)" >> sample.txt && python http-rest.py >> sample.txt
done


