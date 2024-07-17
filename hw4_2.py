from pathlib import Path

def get_cats_info(path):
    try:
        with open(path, encoding="utf-8") as fh:
            cats = fh.readlines()
            
        cats = [cat.strip() for cat in cats if cat.strip()] # cleaning from empty lines
        error_count = 0
        cat_count = 0
        cat_list = []# for dicts
        
        if cats:
            for index, cat in enumerate(cats):
                try:
                    id, name, age = cat.split(",")
                    cat_list.append({"id":id, "name":name, "age":age})
                except Exception as e:
                    error_count += 1
                    print(f"In line {index + 1}:'{cat.strip()}' {e}")
        else:
            print("Could not find any cats")

    except Exception as e:
        print(e)
        return []
    
    return cat_list


path = Path("for4_2.txt")
print(get_cats_info(path))

        