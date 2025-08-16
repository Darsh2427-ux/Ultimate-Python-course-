import micropython

# Removed alloc_emergency_exception_buf as it is not available in this environment
def Micro():
    print("Micropython module imported successfully.")
    print("Platform:", getattr(micropython, "platform", "Unknown"))
    print("Stack use:", getattr(micropython, "stack_use", lambda: "N/A")())