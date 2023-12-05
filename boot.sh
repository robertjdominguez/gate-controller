#!/bin/bash

# Load environment variables from .env file
source .env

# Start a new tmux session
tmux new-session -d -s gatekeeper

# Split the window into two panes
tmux split-window -h
tmux split-window -v

# Select pane 0 and leave it for terminal use
tmux select-pane -t 0

# Select pane 1 and run ngrok command
tmux select-pane -t 1
tmux send-keys 'sudo docker compose up' C-m

# Select pane 2 and run docker-compose up
tmux select-pane -t 2
tmux send-keys "sudo ngrok http --domain=$NGROK_DOMAIN 80" C-m

# Attach to the tmux session
tmux attach-session -t gatekeeper