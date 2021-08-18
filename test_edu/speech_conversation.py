from openpibo.edu_v1 import Pibo

def talk_test():
    pibo = Pibo()

    print('대화를 시작합니다. (q: 종료)')
    while True:
        question = input('나: ')
        if question == 'q':
            break

        ans = pibo.conversation(question)
        print('파이보: ', ans["data"])

if __name__ == "__main__":
    talk_test()