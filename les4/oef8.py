logs = [
    "2025-01-01 INFO Server started",
    "2025-01-01 ERROR Disk full",
    "2025-01-01 INFO Request OK",
    "2025-01-01 ERROR Timeout",
    ]

def count_errors(lines):
    count = 0
    for line in lines:

        if "ERROR" in line:
            print (line)
            count += 1   
    return count
print(count_errors(logs))
    
