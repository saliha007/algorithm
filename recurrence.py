# recurrence.py 
 
import math 
 
# Recursive function to compute T(n) 
def T(n): 
    if n == 1: 
        return 1 
    return 4 * T(n // 2) + n * n 
 
 
def main(): 
    input_sizes = [1, 2, 4, 8, 16, 32, 64] 
     
    results = [] 
     
    print("n\tT(n)\t\tT(n)/(n^2 log n)") 
    print("-" * 50) 
     
    for n in input_sizes: 
        value = T(n) 
         
        if n > 1: 
            ratio = value / (n * n * math.log2(n)) 
        else: 
            ratio = 0 
         
        results.append((n, value, ratio)) 
         
        print(f"{n}\t{value}\t\t{ratio:.4f}") 
     
    # Save results to file 
    with open("substitution_results.txt", "w") as f: 
        f.write("Recurrence: T(n) = 4T(n/2) + n^2\n") 
        f.write("Theoretical Time Complexity: Theta(n^2 log n)\n\n") 
        f.write("n\tT(n)\t\tT(n)/(n^2 log n)\n") 
        f.write("-" * 50 + "\n") 
         
        for n, value, ratio in results: 
            f.write(f"{n}\t{value}\t\t{ratio:.4f}\n") 
         
        f.write("\nObservation:\n") 
        f.write("The ratio T(n)/(n^2 log n) approaches a constant.\n") 
        f.write("Hence, T(n) = Theta(n^2 log n).\n") 
     
    print("\nResults saved to substitution_results.txt") 
 
 
if __name__ == "__main__": 
    main() 