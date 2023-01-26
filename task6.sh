#!/bin/bash

read x 

echo ${x,,}

if [[ "${x,,}" == "y" ]]
then
    echo "YES"
else
    echo "NO"
fi