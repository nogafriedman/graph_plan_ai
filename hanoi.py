import sys


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    "*** YOUR CODE HERE ***"

    # Write propositions
    domain_file.write("Propositions:\n")
    for disk in disks:
        for peg in pegs:
            domain_file.write(f"{disk}_{peg} ")  # disk d_i is on peg p_j
            domain_file.write(f"not_{disk}_{peg} ")  # disk d_i is not on peg p_j

    domain_file.write("\n")

    # Write actions
    domain_file.write("Actions:\n")
    # for disk in disks:
    for i in list(range(n_)):
        disk = "d_" + str(i)
        for from_peg in pegs:
            for to_peg in pegs:
                if from_peg != to_peg:
                    domain_file.write(f"Name: Move_{disk}_from_{from_peg}_to_{to_peg}\n")
                    # domain_file.write(f"Name: Move_{disk}_from_{from_peg}_to_{to_peg}\n")

                    pre_str = f"pre: {disk}_{from_peg} "

                    for j in range(i):
                        disk_j = "d_" + str(j)
                        pre_str += f"not_{disk_j}_{to_peg} "
                        pre_str += f"not_{disk_j}_{from_peg} "

                    domain_file.write(pre_str + "\n")
                    domain_file.write(f"add: {disk}_{to_peg} not_{disk}_{from_peg}\n")
                    domain_file.write(f"delete: {disk}_{from_peg} not_{disk}_{to_peg}\n")

    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    "*** YOUR CODE HERE ***"
    # disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    # pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    # problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file

    # Write initial state
    problem_file.write("Initial state: ")
    for disk in disks:
        problem_file.write(f"{disk}_p_0 ")
        for peg in pegs[1:]:
            problem_file.write(f"not_{disk}_{peg} ")
    problem_file.write("\n")

    # Write goal state
    problem_file.write("Goal state: ")
    for disk in disks:
        problem_file.write(f"{disk}_p_{m_ - 1} ")  # All disks are on the last peg (p_{m_-1})
        for peg in pegs[:-1]:
            problem_file.write(f"not_{disk}_{peg} ")  # All other pegs are clear

    problem_file.write("\n")
    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
