import logging

logging.basicConfig(filename='logging_info.log',
                    format='%(asctime)s-%(name)s-%(levelname)s\t%(message)s',
                    # format='[%(asctime)-15s] [%(levelname)s] - %(message)s',
                    filemode='w',  # clear the log. if you don't want this, set it to 'a'
                    level=logging.DEBUG)


def my_print(inf_):
    # my print function
    print(inf_)  # print to screen
    logging.info(inf_)  # print to log file
