class WeaponModInfo:
    def __init__(self, name, recoil, ergo):
        self.name = name
        self.recoil = recoil
        self.ergo = ergo

    def getName(self):
        return self.name

    def getRecoil(self):
        return self.recoil

    def getErgo(self):
        return self.ergo
