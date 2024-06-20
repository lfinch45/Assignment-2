from runners import Runners


bot = Runners()

def main():
    bot.run_csv()
    bot.run_browser()
    bot.run_outlook()


if __name__ == "__main__":
    main()