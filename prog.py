#! env/bin/python3

import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKGREEN, '\nProgram Started..\n', bcolors.ENDC)

def get_data(filename):
    f = open(filename, 'r')
    inp = f.read()
    f.close()
    return inp

def generateFile(inp, outfilename):
    reward = 0
    temp_reward = 0
    submission_slices = np.array([], dtype='int64')
    submission_pizza_types = 0

    arr = np.array([int(s) for s in inp.split() if s.isdigit()])

    M_participant = arr[:1][0]
    N_pizza_types = arr[1:2][0]
    pizza_slices = arr[2:]

    print('---------\n\n')
    print('Participant : ', M_participant)
    print('Pizza types : ', N_pizza_types)
    print('Pizza slice/type : ', pizza_slices, '\n') 

    index = N_pizza_types - 1
    left_pizza_slices = np.array([], dtype='int64')

    while(index != -1):
        temp_reward = reward + pizza_slices[index]
        if (temp_reward == M_participant):
            reward = temp_reward
            submission_slices = np.insert(submission_slices, 0, index)
            submission_pizza_types += 1
            index = -1
        if (temp_reward < M_participant):
            reward = temp_reward
            submission_slices = np.insert(submission_slices, 0, index)
            submission_pizza_types += 1
            index -= 1
        if (temp_reward > M_participant):
            left_pizza_slices = np.insert(left_pizza_slices, 0, index)
            index -= 1 

    participant_left = M_participant - reward

    print('Final reward : ', reward)
    print('Final sum of pizza types used : ', submission_pizza_types)
    print('Final pizza slices : ', submission_slices)
    print('Participant left : ', participant_left) 
    print('\n\n')
    
    # More optimisation

    if (len(left_pizza_slices) >= 2):
        print('Some more efforts !')

        i = N_pizza_types - submission_pizza_types - 1
        j = submission_pizza_types - 1

        while(i != 0):
            for ii in range(i, 1, -1):
                chosen_index = submission_slices[j]
                chosen_value = pizza_slices[chosen_index]
                left_index = left_pizza_slices[i]
                left_value = pizza_slices[left_index]
                second_index = left_pizza_slices[i - ii]
                second_value = pizza_slices[second_index]
                temp_left = participant_left + chosen_value

                sums = left_value + second_value
                edited_left = temp_left - sums

                if (edited_left > 0): 
                    adjusted_reward = reward - chosen_value + left_value + second_value
                    if (edited_left < participant_left):
                        # Case we should readjust
                        print(bcolors.WARNING, 'This bloc can be improved ! ', bcolors.ENDC)
                        print('Reward : ', reward)
                        print('Adjusted reward : ', adjusted_reward)
                        print('First value : ', left_value)
                        print('Second value : ', second_value)
                        print('Origin left : ', participant_left)
                        print('Edited left : ', edited_left)
                        print('Reward to satisfy : ', temp_left)
                        print('Sum of both values : ', sums, '\n\n')

            i -= 1

    submission_file = open(outfilename, 'w')
    submission_file.write(str(submission_pizza_types))
    submission_file.write('\n')
    for i in range(0, submission_pizza_types):
        submission_file.write(str(submission_slices[i]))
        submission_file.write(' ')

    submission_file.close()

if __name__ == '__main__':

    fa = get_data('a_example.in')
    fb = get_data('b_small.in')
    fc = get_data('c_medium.in')
    fd = get_data('d_quite_big.in')
    fe = get_data('e_also_big.in')

    generateFile(fa, 'submissionfile_a')
    generateFile(fb, 'submissionfile_b')
    #generateFile(fc, 'submissionfile_c')
    #generateFile(fd, 'submissionfile_d')
    #generateFile(fe, 'submissionfile_e')

    print(bcolors.OKGREEN, '\nSubmission files generated !\n\n', bcolors.ENDC)
