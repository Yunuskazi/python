import sys

def update_manifest(source_manifest_path, destination_manifest_path):
    tag_key = 'name='

    # Read source (newer) manifest
    with open(source_manifest_path, 'r') as source_file:
        source_lines = source_file.readlines()

    # Read destination (older) manifest
    with open(destination_manifest_path, 'r') as destination_file:
        destination_lines = destination_file.readlines()

    updated_manifest_lines = []

    for dest_line in destination_lines:
        if tag_key in dest_line:
            try:
                dest_name = dest_line.strip().split('name="')[1].split('"')[0].lower()

                # Look for a matching name in the source manifest
                matched = False
                for source_line in source_lines:
                    if tag_key in source_line:
                        source_name = source_line.strip().split('name="')[1].split('"')[0].lower()

                        # Match names directly or using - and _
                        if dest_name == source_name or dest_name.replace("-", "_") == source_name:
                            new_revision = source_line.strip().split('revision="')[1].split('"')[0]
                            old_revision = dest_line.strip().split('revision="')[1].split('"')[0]

                            print(f"| REPO = {dest_name} | OLD = {old_revision} | NEW = {new_revision} |")

                            updated_line = dest_line.replace(old_revision, new_revision)
                            updated_manifest_lines.append(updated_line)
                            matched = True
                            break

                if not matched:
                    updated_manifest_lines.append(dest_line)

            except IndexError:
                updated_manifest_lines.append(dest_line)
        else:
            updated_manifest_lines.append(dest_line)

    # Write updated lines to a new file
    with open('updated_AOSP.xml', 'w') as updated_file:
        updated_file.writelines(updated_manifest_lines)

    print("✅ Manifest successfully updated → 'updated_AOSP.xml'")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python update_aosp.py <source_manifest.xml> <destination_manifest.xml>")
        sys.exit(1)

    source_manifest = sys.argv[1]
    destination_manifest = sys.argv[2]

    print("🚀 Starting AOSP manifest update...")
    update_manifest(source_manifest, destination_manifest)
