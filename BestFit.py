def best_fit(blocks, processes):
    """
    Implements the Best Fit memory allocation algorithm.
    
    Args:
        blocks: List of available memory block sizes
        processes: List of process sizes needing allocation
        
    Returns:
        List of allocation results showing block assignments
    """
    allocation = []
    remaining_blocks = blocks.copy()
    
    for process in processes:
        # Find the smallest adequate block
        best_block = min(
            (block for block in remaining_blocks if block >= process),
            default=None
        )
        
        if best_block is not None:
            remaining = best_block - process
            allocation.append(f"{best_block} KB (Remaining: {remaining} KB)")
            remaining_blocks[remaining_blocks.index(best_block)] = remaining
        else:
            allocation.append("Not allocated (No suitable block)")
    
    return allocation

def print_table(blocks, processes, allocation):
    """Prints the allocation results in a formatted table"""
    print("\nBest Fit Memory Allocation")
    print(f"Available Blocks: {blocks} KB")
    print("-" * 45)
    print("{:<10} {:<10} {:<25}".format(
        "Process", "Size (KB)", "Allocation Status"))
    print("-" * 45)
    
    for i, (process, alloc) in enumerate(zip(processes, allocation)):
        print("{:<10} {:<10} {:<25}".format(
            f"P{i+1}", 
            process, 
            alloc))
    print("-" * 45)

def get_user_input():
    """Gets user input for blocks and processes"""
    blocks = list(map(int, input("Enter memory block sizes (KB, space-separated): ").split()))
    processes = list(map(int, input("Enter process sizes (KB, space-separated): ").split()))
    return blocks, processes

if __name__ == "__main__":
    print("Best Fit Memory Allocation Algorithm")
    print("----------------------------------")
    
    blocks, processes = get_user_input()
    allocation = best_fit(blocks, processes)
    print_table(blocks, processes, allocation)
