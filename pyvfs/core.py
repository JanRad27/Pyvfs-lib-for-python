# Pyvfs core file
import uuid

class VFSCoreError(Exception):
    # Core error class
    def __init__(message):
        super().__init__(message)

virtualfilesystems = [] # Core VFS list

def get_vfs_by_uuid(target_uuid) -> dict: # Get VFS
    for vfs in virtualfilesystems:
        if vfs["uuid"] == target_uuid:
            return vfs # Returning target
    return None

def new_vfs(object): # Add VFS
    try:
        new_uuid = uuid.uuid4() # UUID
        virtualfilesystems.append({"uuid":new_uuid, "object":object}) # Adding
        return new_uid
    except Exception as e:
        raise VFSCoreError(f"An error occured while creating VFS! Exception log: {e}") # Running error!

def delete_vfs(target_uuid): # Remove VFS
    try:
        vfs = get_vfs_by_uuid(target_uuid) # Get the VFS
        if vfs is None:
            return False # If VFS not exists - returning False
        virtualfilesystems.remove(vfs) # Removing VFS
        return True
    except Exception as e:
        raise VFSCoreError(f"An error occured while deleting VFS! Exception log: {e}") # Running error!
