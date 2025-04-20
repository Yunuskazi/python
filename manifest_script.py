import sys

if len(sys.argv) != 3:
    print("Usage: ./create-manifest.py input_manifest output_file_name")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

# You can add/edit keywords here — case-insensitive match
keywords = ['path="Android"', 'path="tools"']

with open(input_filename, "r") as input_file, open(output_filename, "w") as output_file:
    include_line = False

    for line in input_file:
        if any(keyword.lower() in line.lower() for keyword in keywords) or "<manifest>" in line or "</manifest>" in line:
            include_line = True
            output_file.write(line)

        elif include_line and (line.startswith(" ") or "</project>" in line):
            output_file.write(line)

            if "</project>" in line:
                include_line = False

        else:
            include_line = False

print(f"Lines with keywords copied to {output_filename}")
