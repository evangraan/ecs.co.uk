import sys
from shutil import copyfile

class Orchestrator:
    def __seedData(self, data, path):
        try:
            copyfile("orchestration/fixture/" + data + ".json", path)
        except:
            print("Error [" + sys.exc_info() + "]")
        print("[orchestrator] " + data)

    def seedCatalogue(self, key):
        self.__seedData("catalogue-" + key, self.cataloguePath())

    def seedOffers(self, key):
        self.__seedData("offers-" + key, self.offersPath())

    def cataloguePath(self):
        return "orchestration/fixture/catalogue.json"

    def offersPath(self):
        return "orchestration/fixture/offers.json"
