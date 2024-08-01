from collections import defaultdict
import heapq

def rearranging_string(s: str) -> str:
    count_of_letter = defaultdict(int)
    for letter in s:
        count_of_letter[letter] += 1
    
    #using -count because by default min heap is present
    max_heap = [(-count, letter) for letter, count in count_of_letter.items()]
    heapq.heapify(max_heap)
    
    prev_count, prev_letter = 0, ''
    rearranged_str = []
    
    while max_heap:
        count, letter = heapq.heappop(max_heap)
        rearranged_str.append(letter)
        # If prev_count is less than 0, push it back to the heap
        if prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_letter))
        # Update previous character count and letter
        prev_count, prev_letter = count + 1, letter
    
    rearranged_str = ''.join(rearranged_str)
    # If the rearranged string is not of the same length as the input string, it's not possible to rearrange
    if len(rearranged_str) != len(s):
        return ""
    
    return rearranged_str

if __name__ == '__main__':
    s = input("Enter the string: ")
    result = rearranging_string(s)
    print(result)
