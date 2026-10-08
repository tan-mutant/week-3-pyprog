# Warehouse Inventory Management Tool

A Python script that processes a batch of customer orders against an
in-memory inventory for a distribution center.

## Features
- Stores stock levels in a dictionary
- Receives orders as a list of (item, quantity) tuples
- Full fulfillment, partial fulfillment, out-of-stock and invalid-item handling
- End-of-batch summary: final inventory, fully fulfilled order count,
  and list of items that could not be fully supplied

## Constraints followed
Uses only lists, dictionaries, tuples, loops, if-elif-else and basic
string formatting. No custom functions, classes, imports or file I/O.

## How to run
python inventory_manager.py

## Author
Tanisha Maharjan, International American University
