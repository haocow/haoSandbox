depTable = {}
installed = {}

def processCmd(cmd, params):
    check = cmd.upper()

    if check == "LIST":
        listInstalled()
    elif check == "DEPEND":
        addDep(params[0], params[1:])
    elif check == "INSTALL":
        install(params[0])
    elif check == "REMOVE":
        removeExplicit(params[0])

def listInstalled():
    packages = installed.keys()
    packages.sort()

    for p in packages:
        print "\t" + p

def addDep(package, dependencies):
    depTable[package] = dependencies

def install(package):
    if package in installed:
        print "\t" + package + " is already installed."
        return

    if (package in depTable):
        for dep in depTable[package]:
            installImplicit(dep)

    installed[package] = (depTable[package], "EXPLICIT") if package in depTable else ([], "EXPLICIT")
    print "\tInstalling " + package

def installImplicit(package):
    if package in installed:
        return

    if (package in depTable):
        for dep in depTable[package]:
            installImplicit(dep)

    installed[package] = (depTable[package], "IMPLICIT") if package in depTable else ([], "IMPLICIT")
    print "\tInstalling " + package

def removeExplicit(package):
    if package not in installed:
        print "\t" + package + " is not installed."
        return

    if checkDepNeeded(package):
        print "\t" + package + " is still needed."
    else:
        print "\tRemoving " + package
        (deps, installType) = installed[package]

        del installed[package]

        for dep in deps:
            if not checkDepNeeded(package) and dep in installed and installed[dep][1] == "IMPLICIT":
                removeImplicit(dep)

def removeImplicit(package):
    if package not in installed:
        return

    if not checkDepNeeded(package):
        print "\tRemoving " + package
        (deps, installType) = installed[package]

        del installed[package]

        for dep in deps:
            if not checkDepNeeded(package) and dep in installed and installed[dep][1] == "IMPLICIT":
                removeImplicit(dep)

def checkDepNeeded(package):
    needed = False

    for (deps, installType) in installed.values():
        if package in deps:
            needed = True
    return needed

cmdList = [
    "DEPEND TCPIP NETCARD",
    "DEPEND TELNET TCPIP SOCKET",
    "DEPEND DNS TCPIP",
    "DEPEND HTML REGEX XML",
    "DEPEND REGEX PARSING",
    "DEPEND BROWSER DNS TCPIP HTML CSS",
    "INSTALL TCPIP",
    "REMOVE NETCARD",
    "REMOVE TCPIP",
    "REMOVE NETCARD",
    "INSTALL TCPIP",
    "LIST",
    "INSTALL TCPIP",
    "INSTALL foo",
    "REMOVE TCPIP",
    "INSTALL NETCARD",
    "INSTALL TCPIP",
    "REMOVE TCPIP",
    "LIST",
    "INSTALL TCPIP",
    "INSTALL NETCARD",
    "REMOVE TCPIP",
    "LIST",
    "REMOVE NETCARD",
    "INSTALL BROWSER",
    "LIST",
    "REMOVE BROWSER",
    "LIST",
    "INSTALL HTML",
    "INSTALL TELNET",
    "REMOVE SOCKET",
    "INSTALL DNS",
    "INSTALL BROWSER",
    "REMOVE NETCARD",
    "LIST",
    "REMOVE BROWSER",
    "LIST",
    "END",
]

while (True):
    cmd = raw_input("").upper()
    # cmd = cmdList.pop(0)
    print cmd

    if cmd.upper() == "END":
        break

    cmdArr = cmd.split(' ')
    processCmd(cmdArr[0], cmdArr[1:])
