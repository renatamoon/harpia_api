class DataNotInsertedOnDatabase(Exception):
    msg = "DataNotInsertedOnDatabase::LaptopMongoRepository.save_laptops_on_database:: error when trying to save data"


class NoDataWasFoundOnDatabase(Exception):
    msg = "LaptopMongoRepository.find_laptops_on_database::no data was found on database"
