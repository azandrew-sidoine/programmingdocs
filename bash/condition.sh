#! /bin/sh

count=10

if [ $count -eq 10 ]; then
	echo "Condition is true"
else
	echo "Condition is false"
fi


age=18

if [ $age -gt 18 ]; then
	echo 'You are older than the average'
elif [ $age -eq 18 ]; then
	echo 'You are average'
else 
	echo 'You are younger'
fi

if [[ $age -lt 18 ]]; then
	echo 'You are younger'
elif [[ $age -ge 18 ]] && [[ $age -lt 40 ]]; then
	echo 'You are adult'
else
	echo 'You are Too old'
fi
