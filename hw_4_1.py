from pathlib import Path

def total_salary(path):
    try:
        with open(path, encoding="utf-8") as fh:
            workers = fh.readlines()
            
        workers = [worker for worker in workers if worker.strip()] # cleaning from empty lines
        workers_count = 0
        
        if workers:
            all_salary = 0 
            for index, worker in enumerate(workers):
                try:
                    _, salary = worker.split(",")
                    salary = float(salary)
                    all_salary += salary  
                    workers_count+=1
                except Exception as e:
                    print(f"In line {index + 1}:'{worker.strip()}' {e}")
        else:
            print("Could not find any workers")

    except Exception as e:
        print(e)
        return (0,0)
    
    if workers_count:    
        return (all_salary, all_salary/workers_count)
    else:
        return (0,0)

path = Path("for4_1.txt")
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")