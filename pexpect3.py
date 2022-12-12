import pexpect

child = pexpect.spawn("cat")

child.semdline("Welcome World")

print(child.expect(["hello", "Welcome World"]))
