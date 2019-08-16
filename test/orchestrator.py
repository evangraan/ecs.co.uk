import sys
from shutil import copyfile

class Orchestrator:
    def cataloguePath(self):
        return "test/fixture/catalogue.json"

    def emptyCatalogue(self):
        try:
            copyfile("test/fixture/catalogue-empty.json", self.cataloguePath())
        except:
            print("Error orchestrating catalogue! [" + sys.exc_info() + "]")
        print("[orchestrator] Emptied")

    def fullCatalogue(self):
        try:
            copyfile("test/fixture/catalogue-full.json", self.cataloguePath())
        except:
            print("Error orchestrating catalogue! [" + sys.exc_info() + "]")
        print("[orchestrator] Filled")

    def invalidNameCatalogue(self):
        try:
            copyfile("test/fixture/catalogue-invalid-name.json", self.cataloguePath())
        except:
            print("Error orchestrating catalogue! [" + sys.exc_info() + "]")
        print("[orchestrator] Invalid name")

    def invalidPriceCatalogue(self):
        try:
            copyfile("test/fixture/catalogue-invalid-price.json", self.cataloguePath())
        except:
            print("Error orchestrating catalogue! [" + sys.exc_info() + "]")
        print("[orchestrator] Invalid price")

