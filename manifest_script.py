import sys

if len(sys.argv) != 3:
    print("Usage: python create-manifest.py input_manifest.xml output_manifest.xml")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Case-sensitive keywords
keywords = ['path="build/make"', 'path="build/bazel_common_rules"', '<?', '<manifest>', '</manifest>']

with open(input_filename, "r") as input_file, open(output_filename, "w") as output_file:
    include_line = False

    for line in input_file:
        stripped_line = line.strip()

        # Only include <manifest> and </manifest> explicitly (not similar ones like <manifest-server>)
        if stripped_line == "<manifest>" or stripped_line == "</manifest>":
            output_file.write(line)
            continue

        # If line matches any keyword, include it and future related lines
        if any(keyword in line for keyword in keywords):
            include_line = True
            output_file.write(line)

        elif include_line and (stripped_line.startswith("<linkfile") or stripped_line.startswith("</project>")):
            output_file.write(line)

        else:
            include_line = False

print(f"Filtered manifest written to {output_filename}")
