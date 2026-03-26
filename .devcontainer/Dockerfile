FROM ghcr.io/anthropics/claude-code/devcontainer:latest

# Install Stockfish chess engine
RUN sudo apt-get update \
    && sudo apt-get install -y --no-install-recommends stockfish \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/*
