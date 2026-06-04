from data_transformation.clean_data import clean_data
from Dashboard.test_app import test_run

if __name__ == "__main__":
    clean_data()
    test_run()

    print("Pipeline executed successfully")