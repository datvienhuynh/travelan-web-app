from app import app, db
from app.models import Destination

db.drop_all()
db.create_all()

# Setup initial SQL database
destinations = [
    ['Coron', 'Coron is a tropical island in the province of Palawan in the Philippines. Coron is best known for world-class World War II-era wreck diving, the island also offers limestone karst landscapes, beautiful beaches, crystal-clear freshwater lakes, and shallow-water coral reefs.',
        'coron_1.jpg coron_2.jpeg coron_3.jpg', 26, 'June', 2019, 'Philipines', True],
    ['Hoi An', 'Hoi An Town is an exceptionally well-preserved example of a Southeast Asian trading port dating from the 15th to the 19th century. Its buildings and its street plan reflect the influences, both indigenous and foreign, that have combined to produce this unique heritage site.',
        'hoian_1.jpeg hoian_2.jpg hoian_3.jpg', 7, 'October', 2019, 'Vietnam', True],
    ['Lempuyang Temple', 'Pura Penataran Agung Lempuyang is a Balinese Hindu temple or pura located in the slope of Mount Lempuyang in Karangasem, Bali. Pura Penataran Agung Lempuyang is considered as part of a complex of pura surrounding Mount Lempuyang, one of the highly regarded temples of Bali.',
        'lempuyang_1.jpg lempuyang_2.jpg lempuyang_3.jpg', 14, 'January', 2020, 'Indonesia', True],
    ['Everest Basecamp', 'Everest is more than a mountain and the journey to its base camp is more than just a trek. Every bend in the trail provides another photo opportunity - beautiful forests, Sherpa villages, glacial moraines, and foothills.', 
        'everest_1.jpg everest_2.jpg everest_3.jpg', 18, 'September', 2021, 'Nepal', False]
]

for destination in destinations:
    new_dest = Destination(name=destination[0], caption=destination[1], image_names=destination[2], 
                            date=destination[3], month=destination[4], year=destination[5], country=destination[6], visited=destination[7])
    db.session.add(new_dest)
db.session.commit()