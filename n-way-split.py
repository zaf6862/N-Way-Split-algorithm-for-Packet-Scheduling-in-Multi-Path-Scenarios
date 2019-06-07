import math
import numpy as np




class path:
    def __init__(self, id_in, owd, bw):
        self.id = id_in
        self.owd = owd
        self.bw = bw
        self.allocation_vector = []

def send(i):
    print("this is being sent: " + str(i))

def sendForward(path,buff):
    for i in path.allocation_vector:
        send(buff[i])



def sendBackward(path,buff):
    for i in reversed(path.allocation_vector):
        send(buff[i])



def scheduler(buff, paths):
    num_paths = len(paths)
    chunk_size = math.ceil(len(buff) / num_paths)
    forward_base_seq_num = 0
    reverse_base_seq_num = len(buff)

    for i in range(0, num_paths):
        if (i % 2 == 0):
            paths[i].allocation_vector = range(forward_base_seq_num, forward_base_seq_num + chunk_size)
            forward_base_seq_num += chunk_size
        else:
            paths[i].allocation_vector = range(reverse_base_seq_num - chunk_size, reverse_base_seq_num)
            reverse_base_seq_num -= chunk_size

    for p in paths:
        print("Path : " + str(p.id) + " is going to send the following bytes in the following order")
        if(p.id % 2 != 0):
            sendForward(p,buff)
        else:
            sendBackward(p,buff)

    return



if __name__ == "__main__":
    # buff = np.array(range(1,11))
    buff = np.random.random_integers(1, 10, 10)
    print("This is the data chunk to be transfered : \n" + str(buff))

    paths = []
    for i in range(1,4):
        each_path = path(i,i,i)
        paths.append(each_path)
    print("Total number of paths : " + str(len(paths)))
    scheduler(buff, paths)

