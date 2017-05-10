Execute the python file: python CN_Assignment5.py input.txt

For easy usage and testing, the each host has been assigned IP addresses:

Router S1: MTU = 1500
    H1: 10.0.1.1
    H2: 10.0.1.2
    H11: 10.0.1.11

Router S2: MTU = 500
    H7: 10.0.2.7

Router S3: MTU = 1000
    H5: 10.0.3.5
    H6: 10.0.3.6
    H10: 10.0.3.10

Router S4: MTU = 500
    H3: 10.0.4.3
    H4: 10.0.4.4

Router S5: MTU = 2000
    H8: 10.0.5.8
    H9: 10.0.5.9
    H12: 10.0.5.12

Example input for the program: (Sending a message from H1 to H5)

    - Source IP Address: 10.0.1.1
    - Destination IP Address: 10.0.3.5
    - Message: Testing the program

Write the input in a txt file in the order given above and pass the file as an argument to the program.
Note: Keep the message in 1 line (even if it is long).

Output is written to output.txt