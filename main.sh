#!/bin/bash

show_spinner() {
  local duration=$1
  local message=$2
  local spinner="|/-\\"
  local end=$((SECONDS + duration))

  # Show the spinner until the duration has passed
  while [ $SECONDS -lt $end ]; do
    for i in $(seq 0 $((${#spinner} - 1))); do
      printf "\r%s %s" "$message" "${spinner:$i:1}"
      sleep 0.1
    done
  done

  printf "\r%s Done!\n" "$message"
}


python3 New_LEX.py
echo ">> find your tokens in the output.txt file"
show_spinner 5 "Loading..."
echo
echo
echo ">> Now loading the tokens to execute for the Semantic check "
show_spinner 5 "Loading..."
echo "#############"
echo ">> Semantics result can be seen in the semantic logs file click file:///home/rafay/AbdulRafay_personal/CC/Compiler_Construction/semantic_logs.txt"
echo "#############"
python3 Semantic_Analyzer\ -Temp.py > semantic_logs.txt
echo "Now opening the file in vs code for your convinience."
show_spinner 5 "Loading..."
code semantic_logs.txt