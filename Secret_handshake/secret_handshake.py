def commands(binary_str):
    """Returns the list of commands based on the binary string.

    Args:
        binary_str (str): A string of binary digits (0s and 1s).
    Returns:
        list: A list of commands corresponding to the binary string.
    """
    cmds = ['wink', 'double blink', 'close your eyes', 'jump']

    reverse_flag = len(binary_str) >= 5 and binary_str[-5] == '1'

    result = [
        cmd
        for pos, cmd in enumerate(cmds)                         
        if pos < len(binary_str) and binary_str[-1 - pos] == '1'  
    ]

    if reverse_flag:
        result.reverse()

    return result
