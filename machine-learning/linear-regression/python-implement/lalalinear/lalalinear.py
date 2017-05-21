"""This is a python implementation of
the linear regresion that I have learned from coursea"""

# First thing load the data from ex1data.txt that is copy of the machine-learning-ex1's traing data
def open_data(file_position):

    """this function is defined to read the targe file and return with an matries"""
    with open(file_position) as file:

        data=[];
        for line in file:
            
            item=line.split(',');
            data.append(item);
    file.closed;

    return data;
