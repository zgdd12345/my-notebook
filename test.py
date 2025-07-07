import os

def generate_tree(path, indent='', deep=0, suffix=['os', 'jpg', 'png']):
    print(indent + os.path.basename(path))

    if os.path.isdir(path):
        for item in os.listdir(path):
            if item == '.ipynb_checkpoints':
                continue
            elif item == '__pycache__':
                continue
            elif item == '.git':
                continue
            elif item.split('.')[-1] in suffix:
                continue
            deep += 1
            indent = '|---'
            generate_tree(os.path.join(path, item), '|    ' * (deep-1) +indent, deep=deep, suffix=suffix)
            deep -= 1

path = '/Users/fsm/Library/Mobile Documents/iCloud~md~obsidian/Documents/my-notebook'
generate_tree('./', suffix=['os', 'jpg', 'png'])