import time
from openpibo.edu_v1 import Pibo

def train_face_test():
    pibo = Pibo()
    print("Start DB:", pibo.get_facedb()["data"][0])

    # Train face
    pibo.start_camera()
    time.sleep(2)
    pibo.train_face("Kim")
    print("After Train, DB:", pibo.get_facedb()["data"][0])
    pibo.stop_camera()

    # Recognize
    pibo.start_camera()
    time.sleep(2)
    ret = pibo.search_face()
    print("Recognize: ", ret["data"])
    pibo.stop_camera()

    # Save DB
    pibo.save_facedb('./facedb')
    
    # Reset DB
    # pibo.init_facedb()
    # print('After reset db, DB: ', pibo.get_facedb()["data"][0])

    # Load DB
    pibo.load_facedb()
    print('After Load db, DB: ', pibo.get_facedb()["data"][0])

    # Delete Face
    ret=pibo.delete_face("Kim")
    print('After Delete face: ', pibo.get_facedb()["data"][0])
    
    
if __name__ == "__main__":
    train_face_test()