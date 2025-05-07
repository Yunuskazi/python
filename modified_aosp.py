import sys

def update_manifest(original_file_path, target_file_path):
    # Read the original manifest file (e.g., from Samsung)
    with open(original_file_path, 'r') as original_file:
        original_lines = original_file.readlines()

    # Read the target manifest file (e.g., existing manifest to be updated)
    with open(target_file_path, 'r') as target_file:
        target_lines = target_file.readlines()

    updated_lines = []

    for target_line in target_lines:
        if 'name="' in target_line:
            try:
                # Extract project name from target
                target_name = target_line.strip().split('name="')[1].split('"')[0].lower()

                updated = False
                for original_line in original_lines:
                    if 'name="' in original_line:
                        original_name = original_line.strip().split('name="')[1].split('"')[0].lower()

                        if target_name == original_name or target_name.replace("-", "_") == original_name:
                            # Extract revision fields
                            if 'revision="' in original_line and 'revision="' in target_line:
                                original_revision = original_line.strip().split('revision="')[1].split('"')[0]
                                target_revision = target_line.strip().split('revision="')[1].split('"')[0]

                                # Replace revision in original line with target's revision
                                updated_line = original_line.replace(original_revision, target_revision)

                                print("|REPO NAME =|", target_name, "|NEW REVISION =|", target_revision, "| OLD REVISION =|", original_revision, "|")

                                updated_lines.append(updated_line)
                                updated = True
                                break
                if not updated:
                    updated_lines.append(target_line)
            except Exception as e:
                print("Error processing line:", target_line)
                print("Exception:", str(e))
                updated_lines.append(target_line)
        else:
            updated_lines.append(target_line)

    # Write the updated manifest to a new file
    with open("the_new.xml", 'w') as target_file:
        target_file.writelines(updated_lines)

    print("############ AOSP MANIFEST UPDATED ############")

if len(sys.argv) != 3:
    print("Usage: ./update_aosp.py input_samsung_manifest output_previous_manifest")
    sys.exit(1)

original_manifest_file = sys.argv[1]
target_manifest_file = sys.argv[2]

print("############ AOSP MANIFEST UPDATE STARTED ############")
update_manifest(original_manifest_file, target_manifest_file)