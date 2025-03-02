import os
import random
from core import utility

def get_item_list():
    source_dir = 'output/tags/item_list'

    if not os.path.exists(source_dir):
        print(f"The source directory {source_dir} does not exist.")
        return []

    item_list = []

    for filename in os.listdir(source_dir):
        tag, _ = os.path.splitext(filename)
        source_file_path = os.path.join(source_dir, filename)

        if os.path.isfile(source_file_path):
            with open(source_file_path, 'r') as src_file:
                content = src_file.read()

            item_list.append((content, tag))

    return item_list


# get 3 random filenames and include in 'see also'
def get_see_also(all_filenames):
    if len(all_filenames) < 3:
        print("Not enough files to select 3 random filenames.")
        return []

    random_filenames = random.sample(all_filenames, 3)

    see_also = sorted(os.path.splitext(filename)[0] for filename in random_filenames)

    return see_also


def write_to_file(tag, item_content, see_also):
    dest_dir = 'output/articles/tags/'
    filename = tag + ".txt"

    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    file_path = os.path.join(dest_dir, filename)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"{{{{Header|Modding|Item tags}}}}\n{{{{Page version|{utility.version}}}}}\n{{{{Autogenerated|tags}}}}\n")

        file.write(f"'''{tag}''' is an [[item tag]].\n\n")

        file.write("==Usage==\n[enter a list of where and how this tag is used]\n\n")

        file.write(f"==List of items==\n{item_content}\n\n")

        file.write("==See also==\n")
        file.write('\n'.join(f"*[[{t} (tag)]]" for t in see_also))
        file.write("\n")


def main():
    item_list = get_item_list()
    if item_list:
        all_tags = [tag for _, tag in item_list]

        for content, tag in item_list:
            see_also = get_see_also(all_tags)
            write_to_file(tag, content, see_also)

        print("Output successful: 'output/articles/tags/'")

if __name__ == "__main__":
    main()
