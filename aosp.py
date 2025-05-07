import sys
import os
name = "name="
def update_manifest(original_file_path, target_file_path):
    # Read the original manifest file
    with open(original_file_path, 'r') as original_file:
        original_lines = original_file.readlines()
    # Read the target manifest file and update it
    with open(target_file_path, 'r') as target_file:
        target_lines = target_file.readlines()
    updated_lines = []
    for target_line in target_lines:
        # print(target_line)
        # exit(0)
        # if target_line.startswith('name='):
        if name in target_line:
            target_name = target_line.strip().split('name="')[1].split('"')[0].lower()
            # print("target name =====", target_name)
            for original_line in original_lines:
                # if original_line.startswith('name='):
                if name in original_line:
                    original_name = original_line.strip().split('name="')[1].split('"')[0].lower()
                    # print("originame name ======", original_name)
                    if target_name == original_name:
                        # Replace the revision number in the target line
                        target_revision = target_line.strip().split('revision="')[1].split('"')[0]
                        original_revision = original_line.strip().split('revision="')[1].split('"')[0]
                        print("|REPO NAME =|",target_name,"|NEW REVISION =|" ,target_revision,"| OLD REVISION =|", original_revision,"|")
                        updated_line = original_line.replace(original_revision, target_revision) # s
                        updated_lines.append(updated_line)
                        break
                    elif target_name.replace("-","_") ==  original_name:
                        target_revision = target_line.strip().split('revision="')[1].split('"')[0]
                        original_revision = original_line.strip().split('revision="')[1].split('"')[0]
                        print("|REPO NAME =|",target_name,"|NEW REVISION =|" ,target_revision,"| OLD REVISION =|", original_revision,"|")
                        updated_line = original_line.replace(original_revision, target_revision)
                        updated_lines.append(updated_line)
                        break
            else:
                updated_lines.append(target_line)
        else:
            updated_lines.append(target_line)
    # Write the updated manifest back to the target file    
    with open("the_new.xml", 'w') as target_file:
        target_file.writelines(updated_lines)
        print("############ AOSP MANIFEST UPDATED ############")
if len(sys.argv) !=3:
    print("Usage: ./update_aosp.py input_samsung_manifest output_previous_manifest")
    sys.exit(1)
# Replace these with the actual file paths
original_manifest_file = sys.argv[1] 
target_manifest_file = sys.argv[2]  
print("############ AOSP MANIFEST UPDATE STARTED ############`")
update_manifest(original_manifest_file, target_manifest_file)