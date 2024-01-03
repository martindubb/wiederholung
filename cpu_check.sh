#!/bin/bash

CPU_FILE="/tmp/cpu_data.txt"

write_cpu_to_file() {
    local cpu_stat=$(mpstat | awk '$12 ~ /[0-9.]+/ { print 100 - $12"%" }')
    echo $cpu_stat > $CPU_FILE
}

main() {
    write_cpu_to_file
}

main