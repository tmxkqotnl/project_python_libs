from datetime import date
import re
import my_logger

logger = my_logger.CustomLogger().create(log_folder='Log')

DATE = re.compile("^[0-9]{4} [0-9]{1,2} [0-9]{1,2}$")


def is_date_correct(my_date: str):
    if not re.match(DATE, my_date):
        logger.error("유효하지 않은 입력 양식 - {}".format(my_date))
        raise ValueError("입력한 날짜의 양식을 다시 확인해주세요.")

    y_m_d = my_date.split()

    today = date.today()
    target_date = date(*map(int, y_m_d))

    return (target_date - today).days


def get_day_interval():
    while True:
        try:
            my_date = input("\n0000(년) 00(월) 00(일) 순으로 입력해주세요(종료 q) : ")
            if my_date == "q":
                logger.info('종료')
                break

            return is_date_correct(my_date)
        except ValueError:
            logger.info("다시 입력 받습니다..")


print(get_day_interval())
