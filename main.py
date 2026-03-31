import logging

def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
    #2.ログメッセージの出力
    logging.info("Processing data...")
    logging.warning("something unpxected happend.")

if __name__ == "__main__":
    main()