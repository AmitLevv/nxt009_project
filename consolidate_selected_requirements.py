import os

# List of paths to the requirements.txt files you want
selected_requirement_paths = [
    './nxt009_runtime/tools/nxt009_hw_features/requirements.txt',  # Example file
    './applications/nextrunner/requirements.txt',                   # Example file
    './nxt009-soc-sw/tests/requirements.txt',                       # Example file
    # Add more paths here as needed...
]

consolidated_requirements = set()

for path in selected_requirement_paths:
    if os.path.exists(path):
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    consolidated_requirements.add(line)

# Writing consolidated requirements to the main requirements.txt
with open('requirements.txt', 'w') as main_req_file:
    for req in sorted(consolidated_requirements):
        main_req_file.write(req + '\n')

print("Selected requirements consolidated successfully.")
