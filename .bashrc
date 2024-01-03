[...]

update_latency() {
    if [ -f /tmp/latency_data.txt ]; then
        LATENCY=$(cat /tmp/latency_data.txt)
    else
        LATENCY="No Latency Data"
    fi
}

cpu_latency() {
    if [ -f /tmp/cpu_data.txt ]; then
        CPU1=$(cat /tmp/cpu_data.txt)
    else
        CPU1="No CPU Data"
    fi
}

PROMPT_COMMAND=("update_latency" "cpu_latency")
PS1="\$LATENCY ms - $CPU1 $PS1"
