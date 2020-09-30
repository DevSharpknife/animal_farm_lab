import pdb
from models.animal import Animal    
from models.owner import Owner

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository

# animal_repository.delete_all()
# owner_repository.delete_all()

owner_1 = Owner("Geoff")
owner_repository.save(owner_1)
owner_2 = Owner("Clive")
owner_repository.save(owner_2)

owner_repository.select_all()

animal_1 = Animal("Bear", "Gentle Ben", owner_1)
animal_repository.save(animal_1)

animal_2 = Animal("Ferret", "Nibbles", owner_1)
animal_repository.save(animal_2)

animal_3 = Animal("Rabbit", "Jessica", owner_2)
animal_repository.save(animal_3)

animal_4 = Animal("Hedgehog", "Spike", owner_2)
animal_repository.save(animal_4)

animal_repository.select_all()

pdb.set_trace()