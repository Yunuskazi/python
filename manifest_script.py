import sys

if len(sys.argv) != 3:
    print("Usage: ./create-manifest.py input_manifest output_file_name")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Add all relevant keywords (case-insensitive match)
keywords = ['path="kernel/android"']

with open(input_filename, "r") as input_file, open(output_filename, "w") as output_file:
    output_file.write("<manifest>\n")
    include_line = False

    for line in input_file:
        # Check if line starts a project we care about
        if "<project" in line and any(keyword.lower() in line.lower() for keyword in keywords):
            include_line = True
            output_file.write(line)

        elif include_line:
            output_file.write(line)
            if "</project>" in line or "<project" in line:  # Reset if new project starts or ends
                include_line = False

    output_file.write("</manifest>\n")

print(f"Filtered manifest written to {output_filename}")
