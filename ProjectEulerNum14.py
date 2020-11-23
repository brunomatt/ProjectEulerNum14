#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz(num):
    iterations = 0
    new_num = num
    while new_num != 1:
        if new_num % 2 == 0:
            new_num = new_num / 2
            iterations += 1
        else:
            new_num = 3 * new_num + 1
            iterations += 1
    return iterations, num

possible_answers = []

for k in range(1,1000000):
    possible_answers.append(collatz(k))

answer = max(possible_answers)

print(answer[1])