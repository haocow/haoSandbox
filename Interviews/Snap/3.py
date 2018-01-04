class loadBalancer:
    def __init__(self, servers):
        self.allServers = servers
        self.liveServers = self.allServers[:]
        self.numServers = len(servers)
        self.numLiveServers = len(servers)

    def getServer(self, user):
        server = self.allServers[abs(hash(user)) % self.numServers]
        if server not in self.liveServers:
            server = self.liveServers[abs(hash(user)) % self.numLiveServers]
        return server

    def removeServer(self, server):
        if server in self.liveServers:
            self.liveServers.remove(server)
            self.numLiveServers -= 1

    def getServers(self):
        return self.allServers

servers = ["s1", "s2", "s3", "s4"]
lb = loadBalancer(servers)

print lb.getServer("")
print lb.getServer("jon")
print lb.getServer("amrit")

print "~~~~~~~~~~~~~"
lb.removeServer("s1")

print lb.getServer("")
print lb.getServer("jon")
print lb.getServer("amrit")

print lb.getServers()
