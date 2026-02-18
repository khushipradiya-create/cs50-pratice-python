
# Coke Machine Simulator
- Description

  A Python program that simulates a vending machine selling Coca-Cola bottles for 50 cents, accepting only 25¢, 10¢, and 5¢ coins.

# Features:

    Accepts coins one at a time

    Tracks amount due after each insertion

    Ignores invalid denominations

    Calculates exact change owed when 50¢ is paid

# How it Works

    Starts with 50 cents due

    Prompts for coin insertion repeatedly

    Accepts only: 25, 10, 5 (ignores others)

    Updates remaining amount after each valid coin

    When payment ≥ 50¢, outputs change owed and stops

# Example Usage

text
$ python coke.py
Amount due: 50
25
Amount due: 25
10
Amount due: 15
10
Amount due: 5
5
Change owed: 0

