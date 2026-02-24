# Operating System Process Scheduling Simulator

A Python-based simulator for analyzing and comparing classical CPU scheduling algorithms used in Operating Systems.

This project implements and evaluates the following five scheduling algorithms:

FCFS – First Come First Serve

SJF – Shortest Job First

RR – Round Robin

PPS – Priority Preemptive Scheduling

MQS – Multilevel Queue Scheduling

The simulator calculates performance metrics and generates Gantt charts to visually compare execution behavior and efficiency.

# Objectives

Implement core CPU scheduling algorithms

Compare their behavior under the same process set

Evaluate performance using standard metrics

Visualize execution timelines using Gantt charts

Provide a clear analytical comparison of scheduling strategies

# Features

Simulation of 5 major scheduling algorithms

Preemptive and non-preemptive support

Automatic computation of:

Waiting Time

Turnaround Time

Response Time

Average metrics

Gantt chart visualization for each algorithm

Structured and modular Python implementation

Easy comparison of performance results

# Performance Metrics Used

Waiting Time (WT)
Time a process waits in the ready queue.

Turnaround Time (TAT)
Total time from arrival to completion.

Response Time (RT)
Time from arrival until first CPU allocation.

These metrics allow fair evaluation of scheduling efficiency and responsiveness.

# Gantt Chart Visualization

Each algorithm generates a Gantt chart showing:

Execution order of processes

Time intervals

Context switches (where applicable)

This makes it easier to visually analyze scheduling behavior.

# Algorithms Overview
# FCFS (First Come First Serve)

Non-preemptive

Simple and fair by arrival order

Can suffer from convoy effect

# SJF (Shortest Job First)

Non-preemptive

Minimizes average waiting time

Requires burst time knowledge

# RR (Round Robin)

Preemptive

Uses time quantum

Good for time-sharing systems

# PPS (Priority Preemptive Scheduling)

Preemptive

Higher priority processes execute first

Risk of starvation (can be improved with aging)

# MQS (Multilevel Queue Scheduling)

Multiple ready queues

Different scheduling strategies per queue

Suitable for complex systems

# Tech Stack

Language: Python 

Visualization: Matplotlib

Environment: VS Code

# Educational Value

This project is designed for:

Operating Systems coursework

Academic demonstrations

Algorithm comparison studies

Understanding scheduling trade-offs

Visual learning through simulation
