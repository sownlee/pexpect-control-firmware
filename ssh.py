import pexpect
import sys
import re

def ssh_login(host, port, username, password):
    try:
        # Create an SSH session with StrictHostKeyChecking=no and custom port
        ssh = pexpect.spawn(f'ssh -o StrictHostKeyChecking=no -p {port} {username}@{host}')

        # Expect the password prompt
        ssh.expect('password: ')

        # Send the password
        ssh.sendline(password)

        # Expect the shell prompt (you can customize this based on your system)
        ssh.expect(r'\$ ')

        # Execute the 'whoami' command
        ssh.sendline('whoami')

        # Wait for the command to complete and capture the output
        ssh.expect(r'\$ ')
        output_lines = ssh.before.decode('utf-8').strip().split('\n')

        # Extract the result of 'whoami' command
        whoami_output = output_lines[-1].strip()

        # Close the SSH session
        ssh.sendline('exit')
        ssh.expect(pexpect.EOF)
        ssh.close()

        return whoami_output

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 ssh_login.py <host> <port> <username> <password>")
        sys.exit(1)

    host = sys.argv[1]
    port = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]

    whoami_result = ssh_login(host, port, username, password)
    print(f"Result of 'whoami' command: {whoami_result}")
